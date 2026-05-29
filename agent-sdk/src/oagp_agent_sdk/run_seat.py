"""run_seat() — autonomous-dispatch entry point (v0.2).

Dispatches an agent bound to an OAGP position as an UNATTENDED session, with
bounded authority enforced STRUCTURALLY:

- Tier 1 (default): propose-only by construction (no Director-capable tools).
- Tier 2: explicit, audited Director elevation via grant_director_actions.
- Tier 3: non-delegable dispatch — run_seat()/bind() are inert inside a
  bound-agent context (guard.py).

Built on v0.1 bind(). The dispatch backend is the cross-vendor seam; on Claude
Code it composes over the native Workflows-class dispatcher (deferred wiring;
StubBackend for now). Roledef resolution is fail-closed in autonomous mode.
"""

import subprocess
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from .authority import (
    authority_block,
    construct_toolset,
    validate_director_actions,
)
from .backends import DispatchBackend, DispatchHandle, select_backend
from .bind import bind, BindResult
from .bind_event import emit_bind_event_memo
from .guard import BOUND_AGENT_ENV_MARKER, assert_dispatch_allowed


@dataclass
class DispatchRecord:
    """Returned by run_seat(). The full audit-relevant record of one autonomous
    dispatch."""
    agent_name: str
    position_id: str
    org_state_sha: str | None
    tier: int
    granted_authority: list[str]          # [] == propose-only
    toolset: list[str]
    withheld_tools: list[str]             # Director-capable tools NOT granted
    bind_event_memo: Path | None
    agent_file: Path
    backend: str
    bind_result: BindResult
    dispatch_handle: DispatchHandle
    extra: dict[str, Any] = field(default_factory=dict)


def _git_sha(repo_dir: Path) -> str | None:
    """Best-effort current commit SHA of the org's repo (the org-state the
    dispatched agent will see). None if not a git repo / git unavailable."""
    try:
        out = subprocess.run(
            ["git", "-C", str(repo_dir), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if out.returncode == 0:
            return out.stdout.strip()
    except Exception:
        pass
    return None


def run_seat(
    orgdef_path: str | Path,
    position_id: str,
    *,
    brief: str | None = None,
    grant_director_actions: list[str] | None = None,
    tools: list[str] | None = None,
    backend: DispatchBackend | None = None,
    runtime: str = "auto",
    director_seat: str = "director",
    agents_root: str | Path = ".claude/agents",
    context_tag: str | None = None,
    model: str = "inherit",
    max_turns: int | None = None,
    color: str | None = None,
    allow_embedded_fallback: bool = False,
    emit_memo: bool = True,
    now: datetime | None = None,
) -> DispatchRecord:
    """Dispatch an agent bound to an OAGP position as an unattended session.

    Parameters
    ----------
    orgdef_path, position_id : as in bind().
    brief : the engagement brief (becomes the dispatched agent's initial prompt).
    grant_director_actions : None/[] -> Tier 1 (propose-only). A non-empty list
        (e.g. ["commit", "push"]) -> Tier 2: adds Director-capable tools AND
        fires a bind-event memo recording the grant. Never silent.
    tools : requested toolset. At Tier 1, must not include Director-capable
        tools (raises Tier1ViolationError). Defaults to a propose-safe set.
    backend : a DispatchBackend; defaults to select_backend(runtime).
    director_seat : the dispatching human's seat (bind-event memo `from`).
    allow_embedded_fallback : autonomous roledef resolution is fail-closed; set
        True to permit the embedded job_definition when a URL fetch fails.
    emit_memo : emit the bind-event audit memo (default True; every autonomous
        dispatch should). now : injected dispatch time (defaults to clock).

    Returns
    -------
    DispatchRecord

    Raises
    ------
    BoundAgentDispatchError : if invoked inside a bound-agent context (Tier-3).
    Tier1ViolationError : if Tier-1 dispatch requests Director-capable tools.
    RoledefResolutionError : if fail-closed resolution aborts.
    """
    # Tier-3 floor: fail fast before any work.
    assert_dispatch_allowed("run_seat")

    if now is None:
        now = datetime.now()

    granted = validate_director_actions(grant_director_actions)
    toolset, tier, withheld = construct_toolset(tools, granted)

    orgdef_path = Path(orgdef_path).resolve()
    project_root = orgdef_path.parent.parent
    org_state_sha = _git_sha(project_root)

    # The authority block is the prose layer; the toolset is the hard layer.
    authority = authority_block(tier, granted)

    result = bind(
        orgdef_path=orgdef_path,
        position_id=position_id,
        agents_root=agents_root,
        context_tag=context_tag,
        initial_prompt=brief,
        tools=toolset,
        model=model,
        permission_mode="acceptEdits",
        max_turns=max_turns,
        color=color,
        extra_context=authority,
        roledef_fail_closed=True,
        allow_embedded_fallback=allow_embedded_fallback,
    )

    memos_dir = project_root / "memos"
    bind_event_path: Path | None = None
    if emit_memo:
        bind_event_path = emit_bind_event_memo(
            memos_dir,
            from_seat=director_seat,
            to_seat=position_id,
            agent_name=result.agent_name,
            position_id=position_id,
            org_state_sha=org_state_sha,
            granted_authority=granted,
            tier=tier,
            brief=brief,
            now=now,
            roledef_id=result.roledef_id,
            roledef_version=result.roledef_version,
            roledef_source=result.roledef_source,
        )

    backend = backend or select_backend(runtime)
    # The dispatched environment carries the Tier-3 bound-agent marker so a
    # nested bind()/run_seat() inside it refuses. (Package-absence is the
    # backend's complementary deployment-layer floor.)
    dispatch_env = {BOUND_AGENT_ENV_MARKER: "1"}
    handle = backend.dispatch(
        result.agent_file,
        brief=brief,
        env=dispatch_env,
        tier=tier,
        granted_authority=granted,
    )

    return DispatchRecord(
        agent_name=result.agent_name,
        position_id=position_id,
        org_state_sha=org_state_sha,
        tier=tier,
        granted_authority=granted,
        toolset=toolset,
        withheld_tools=withheld,
        bind_event_memo=bind_event_path,
        agent_file=result.agent_file,
        backend=backend.name,
        bind_result=result,
        dispatch_handle=handle,
    )
