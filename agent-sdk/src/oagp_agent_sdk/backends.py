"""Dispatch-backend abstraction.

`run_seat()` is the runtime-neutral seam; a backend actually launches the
dispatched agent. Per the v0.2 amendment, the Claude Code backend composes
over the native Workflows-class dispatcher rather than building bespoke
subprocess/CLI plumbing.

This module ships:
- DispatchBackend (ABC): the seam.
- StubBackend: records the dispatch intent without launching. Used for the
  governance-core build + conformance tests before the live Workflows backend
  is wired.
- WorkflowsBackend: placeholder for the Claude Code native-dispatcher path
  (deferred per PO direction 2026-05-29; raises until wired).
"""

import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class DispatchHandle:
    """Opaque handle returned by a backend's dispatch(). Shape is
    backend-specific; the stub records enough to assert against in tests."""
    backend: str
    agent_file: Path
    env: dict[str, str]
    brief: str | None
    launched: bool
    detail: dict[str, Any] = field(default_factory=dict)


class DispatchBackend(ABC):
    """Launches a dispatched bound-agent session from a subagent file."""

    name: str = "abstract"

    @abstractmethod
    def dispatch(
        self,
        agent_file: Path,
        *,
        brief: str | None,
        env: dict[str, str],
        tier: int = 1,
        granted_authority: list[str] | None = None,
    ) -> DispatchHandle:
        """Launch (or prepare) the dispatched agent. `env` carries the Tier-3
        bound-agent marker; backends that can set subagent env MUST apply it.
        `tier` / `granted_authority` are passed for backends that surface them
        in generated artifacts (e.g. workflow meta)."""
        raise NotImplementedError


class StubBackend(DispatchBackend):
    """Records the dispatch intent without launching anything.

    The governance core (tiers, bind-event memo, fail-closed resolution) is
    fully exercisable against this backend. Swap for WorkflowsBackend when the
    live Claude Code dispatch path is wired.
    """

    name = "stub"

    def __init__(self) -> None:
        self.dispatches: list[DispatchHandle] = []

    def dispatch(
        self,
        agent_file: Path,
        *,
        brief: str | None,
        env: dict[str, str],
        tier: int = 1,
        granted_authority: list[str] | None = None,
    ) -> DispatchHandle:
        handle = DispatchHandle(
            backend=self.name,
            agent_file=agent_file,
            env=dict(env),
            brief=brief,
            launched=False,
            detail={
                "note": "stub backend — dispatch recorded, not launched",
                "tier": tier,
                "granted_authority": granted_authority or [],
            },
        )
        self.dispatches.append(handle)
        return handle


def _js_string(s: str) -> str:
    """JSON-encode a string for safe embedding in a generated JS script."""
    return json.dumps(s)


def render_dispatch_workflow(
    *,
    agent_name: str,
    brief: str | None,
    tier: int,
    granted_authority: list[str],
) -> str:
    """Render a Claude Code workflow script that dispatches the bound agent.

    The script composes over the native Workflows dispatcher: it calls
    `agent(brief, {agentType: <name>})`, which resolves the bound subagent file
    written to `.claude/agents/<name>.md`. Using `agentType` is REQUIRED — it is
    what carries the bound agent's `tools:` frontmatter (the Tier-1 structural
    constraint). Passing the prompt inline instead would give the agent the
    workflow's default broad toolset and break bounded authority.
    """
    authority = "propose-only" if not granted_authority else ", ".join(granted_authority)
    brief_js = _js_string(brief or f"You are dispatched as {agent_name}. Read your bind context and act per your roledef. Stop when your output contract is satisfied.")
    return f"""export const meta = {{
  name: {_js_string(f"oagp-seat-{agent_name}")},
  description: {_js_string(f"OAGP autonomous bound-agent dispatch: {agent_name} (Tier-{tier}, {authority}). Composes over the native Workflows dispatcher via agentType so the bound toolset (the structural authority bound) is enforced.")},
  phases: [{{ title: "Engage", detail: {_js_string(f"{agent_name} runs its bound engagement")} }}]
}};

// Tier-3 note: the bound agent is dispatched via agentType, inheriting the
// tools: frontmatter of .claude/agents/{agent_name}.md (the hard authority
// layer). The OAGP_BOUND_AGENT env marker cannot be injected into a
// workflow-spawned subagent; the Tier-3 non-delegable floor for this path
// therefore rests on PACKAGE-ABSENCE (oagp_agent_sdk must not be importable in
// the dispatch environment) plus the bound toolset. See README + the
// implementer status memo for the coordination finding.

phase("Engage");
const BRIEF = {brief_js};
const result = await agent(BRIEF, {{
  agentType: {_js_string(agent_name)},
  label: {_js_string(agent_name)},
  phase: "Engage",
}});
return {{ agent_name: {_js_string(agent_name)}, tier: {tier}, granted_authority: {json.dumps(granted_authority)}, result }};
"""


class WorkflowsBackend(DispatchBackend):
    """Claude Code native Workflows-class dispatcher backend.

    The agent-sdk is a Python package and cannot itself invoke the Claude Code
    Workflow tool. So this backend GENERATES a workflow script (the artifact the
    native dispatcher runs) next to the bound agent file, and returns a handle
    naming it. The harness/human runs it via Claude Code Workflows; the run is
    "live" in that executing the generated script actually dispatches the agent.

    The script dispatches via `agentType` (NOT an inline prompt) so the bound
    agent file's `tools:` frontmatter — the Tier-1 structural authority bound —
    is what governs the dispatched agent's capabilities.

    Session-start caveat (empirical, from the 2026-05-23 PoC): a subagent file
    written mid-session may not be resolvable until a session that loads after
    it exists. Run the generated workflow from a fresh session if agentType does
    not resolve.

    Tier-3 caveat: the OAGP_BOUND_AGENT env marker cannot be injected into a
    workflow-spawned subagent. For this path the non-delegable floor rests on
    package-absence (do not expose oagp_agent_sdk in the dispatch environment)
    plus the bound toolset. Surfaced as a coordination finding to oagp-strategist.
    """

    name = "workflows"

    def dispatch(
        self,
        agent_file: Path,
        *,
        brief: str | None,
        env: dict[str, str],
        tier: int = 1,
        granted_authority: list[str] | None = None,
    ) -> DispatchHandle:
        agent_name = agent_file.stem
        script = render_dispatch_workflow(
            agent_name=agent_name,
            brief=brief,
            tier=tier,
            granted_authority=granted_authority or [],
        )
        script_path = agent_file.parent / f"{agent_name}.workflow.js"
        script_path.write_text(script, encoding="utf-8")
        return DispatchHandle(
            backend=self.name,
            agent_file=agent_file,
            env=dict(env),
            brief=brief,
            launched=False,
            detail={
                "workflow_script": str(script_path),
                "run_with": f"Claude Code Workflows on {script_path.name} "
                            f"(or Workflow tool scriptPath); dispatches agentType "
                            f"'{agent_name}'.",
                "tier3_floor": "package-absence + bound toolset (env marker does "
                               "not reach workflow-spawned subagents)",
            },
        )


def _in_claude_code() -> bool:
    """Best-effort detection of a Claude Code runtime via env markers."""
    import os
    for var in ("CLAUDECODE", "CLAUDE_CODE", "CLAUDE_AGENT_SDK"):
        if os.environ.get(var, "").strip():
            return True
    return False


def select_backend(runtime: str = "auto") -> DispatchBackend:
    """Select a dispatch backend for the runtime.

    - "stub": StubBackend (records intent; for tests / governance-core runs).
    - "workflows" / "claude-code": WorkflowsBackend (generates a Claude Code
      workflow script that dispatches the bound agent via agentType).
    - "auto": WorkflowsBackend if a Claude Code runtime is detected, else Stub.
    """
    if runtime in ("workflows", "claude-code"):
        return WorkflowsBackend()
    if runtime == "stub":
        return StubBackend()
    # auto
    return WorkflowsBackend() if _in_claude_code() else StubBackend()
