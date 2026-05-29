"""Launcher — the canonical autonomous-dispatch operational layer (v0.2).

Ratified by decisions/proposal-agent-sdk-v0.2-governance-addendum-autonomous-
dispatch-constraints.md. The launcher is the single locus of two MUST-conventions:

- **Ruling A — launcher-per-dispatch.** Autonomous dispatch MUST use the
  fresh-session / `agentType` path: a launcher starts a clean session per
  dispatch, against which the bound agent file pre-exists and resolves (so its
  `tools:` frontmatter — the Tier-1 structural bound — is actually loaded).
  Inline / same-session dispatch MUST NOT be used for autonomous runs (it
  substitutes the workflow's broad default toolset and breaks the bound). The
  launcher therefore always dispatches via the WorkflowsBackend (agentType);
  it does not accept an inline backend.

- **Ruling B — Tier-2 gating.** Tier-2 (elevated) autonomous dispatch is
  PROHIBITED unless the launcher verifies the dispatch environment cannot import
  `oagp_agent_sdk` (package-absence). In the Workflows path the OAGP_BOUND_AGENT
  env marker cannot reach a workflow-spawned subagent, so for a Bash-capable
  elevated agent the only barrier to self-dispatch is package-absence — and a
  no-override floor (Tier-3) cannot rest on a merely-documented guarantee. The
  launcher converts it into an in-band preflight: verify, or refuse.

  Tier-1 needs no gate (safe by toolset: no Bash → no path to a dispatcher).

The actual fresh-session spawn is environment-dependent (the `claude` CLI
surface). `StubSessionLauncher` (default) records the launch intent + the
command that would run; `ClaudeCliLauncher` constructs/executes the real
invocation. The Tier-2 gate and the agentType-only enforcement are runtime-
independent and fully tested regardless.
"""

import shutil
import subprocess
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from .authority import resolve_tier, validate_director_actions
from .backends import select_backend
from .run_seat import DispatchRecord, run_seat


class Tier2GateError(RuntimeError):
    """Raised when a Tier-2 autonomous dispatch is requested but the launcher
    cannot verify the dispatch environment is package-absent (Ruling B)."""


def verify_package_absent(
    python_executable: str = "python",
    *,
    env: dict[str, str] | None = None,
    timeout: int = 15,
) -> bool:
    """Return True iff `oagp_agent_sdk` is NOT importable in the target dispatch
    environment (i.e. the package-absence gate is satisfied).

    Runs `<python> -c "import oagp_agent_sdk"` and treats a non-zero exit as
    absence. Fail-safe: if the check itself cannot run (python missing, timeout),
    return False (NOT verified absent → caller must refuse Tier-2).
    """
    exe = shutil.which(python_executable) or python_executable
    try:
        proc = subprocess.run(
            [exe, "-c", "import oagp_agent_sdk"],
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
        )
    except (FileNotFoundError, subprocess.SubprocessError):
        return False  # cannot verify → fail-safe to "not absent"
    return proc.returncode != 0


@dataclass
class LaunchHandle:
    """Returned by a SessionLauncher. Records how the fresh session was (or would
    be) started to run the generated dispatch workflow via agentType."""
    launcher: str
    workflow_script: Path
    agent_name: str
    command: list[str]
    launched: bool
    detail: dict[str, Any] = field(default_factory=dict)


class SessionLauncher(ABC):
    """Starts a clean session per dispatch to run the generated workflow."""

    name: str = "abstract"

    @abstractmethod
    def launch(self, workflow_script: Path, *, agent_name: str) -> LaunchHandle:
        raise NotImplementedError


class StubSessionLauncher(SessionLauncher):
    """Records the launch intent + the command that would run; does not spawn.

    Default launcher — the gate and agentType-only enforcement are fully
    exercisable against it. Swap for ClaudeCliLauncher to actually spawn.
    """

    name = "stub"

    def __init__(self) -> None:
        self.launches: list[LaunchHandle] = []

    def launch(self, workflow_script: Path, *, agent_name: str) -> LaunchHandle:
        handle = LaunchHandle(
            launcher=self.name,
            workflow_script=workflow_script,
            agent_name=agent_name,
            command=ClaudeCliLauncher.build_command(workflow_script, agent_name),
            launched=False,
            detail={"note": "stub launcher — fresh-session spawn recorded, not executed"},
        )
        self.launches.append(handle)
        return handle


class ClaudeCliLauncher(SessionLauncher):
    """Spawns a fresh Claude Code session to run the generated dispatch workflow.

    A fresh `claude` invocation loads the agent registry AFTER the agent file
    exists, so `agentType` resolves and the bound `tools:` frontmatter binds —
    the session-start rule, used as the enforcement rather than worked around.

    The exact CLI surface is environment-dependent; `build_command()` constructs
    a best-effort invocation. With execute=True the launcher runs it via
    subprocess; otherwise it returns the command for an operator/cron to run.
    """

    name = "claude-cli"

    def __init__(self, *, execute: bool = False, claude_bin: str = "claude") -> None:
        self.execute = execute
        self.claude_bin = claude_bin

    @staticmethod
    def build_command(workflow_script: Path, agent_name: str) -> list[str]:
        # Fresh, backgrounded session running the generated workflow. The flag
        # surface is environment-dependent; adjust per the installed CLI.
        return ["claude", "--bg", "workflow", "run", str(workflow_script)]

    def launch(self, workflow_script: Path, *, agent_name: str) -> LaunchHandle:
        command = self.build_command(workflow_script, agent_name)
        command[0] = self.claude_bin
        launched = False
        detail: dict[str, Any] = {}
        if self.execute:
            if shutil.which(self.claude_bin) is None:
                raise RuntimeError(
                    f"ClaudeCliLauncher(execute=True): '{self.claude_bin}' not on PATH. "
                    f"Run the command manually from a fresh session: {' '.join(command)}"
                )
            proc = subprocess.Popen(command)
            launched = True
            detail["pid"] = proc.pid
        else:
            detail["note"] = "command constructed; not executed (execute=False)"
        return LaunchHandle(
            launcher=self.name,
            workflow_script=workflow_script,
            agent_name=agent_name,
            command=command,
            launched=launched,
            detail=detail,
        )


@dataclass
class LaunchRecord:
    """The full record of one autonomous dispatch: the generated dispatch
    artifacts plus how the fresh session was launched."""
    tier: int
    granted_authority: list[str]
    dispatch: DispatchRecord
    launch_handle: LaunchHandle
    tier2_gate_checked: bool
    tier2_gate_passed: bool | None  # None when tier==1 (no gate needed)


def launch_seat(
    orgdef_path,
    position_id,
    *,
    brief: str | None = None,
    grant_director_actions: list[str] | None = None,
    session_launcher: SessionLauncher | None = None,
    package_absence_verifier: Callable[[], bool] | None = None,
    dispatch_python: str = "python",
    **run_seat_kwargs,
) -> LaunchRecord:
    """Canonical autonomous-dispatch entry point (Ruling A + Ruling B).

    Always dispatches via the WorkflowsBackend (agentType) — inline dispatch is
    not a sanctioned autonomous path. For Tier-2 (a non-empty
    grant_director_actions), verifies the dispatch environment is package-absent
    before proceeding; refuses with Tier2GateError otherwise.

    The fresh-session spawn is delegated to `session_launcher` (default
    StubSessionLauncher, which records the intent + command). Pass
    ClaudeCliLauncher(execute=True) to actually spawn.
    """
    granted = validate_director_actions(grant_director_actions)
    tier = resolve_tier(granted)

    tier2_gate_checked = False
    tier2_gate_passed: bool | None = None
    if tier == 2:
        tier2_gate_checked = True
        verifier = package_absence_verifier or (lambda: verify_package_absent(dispatch_python))
        tier2_gate_passed = bool(verifier())
        if not tier2_gate_passed:
            raise Tier2GateError(
                "Tier-2 autonomous dispatch refused: could not verify the dispatch "
                "environment is package-absent (oagp_agent_sdk must NOT be importable "
                "there). The Tier-3 non-delegable floor cannot be guaranteed otherwise. "
                "Provide a package-absent dispatch environment, or use Tier-1 "
                "(propose-only) autonomous dispatch."
            )

    # Ruling A: autonomous dispatch is always agentType (WorkflowsBackend).
    record = run_seat(
        orgdef_path,
        position_id,
        brief=brief,
        grant_director_actions=granted,
        backend=select_backend("workflows"),
        **run_seat_kwargs,
    )

    launcher = session_launcher or StubSessionLauncher()
    workflow_script = Path(record.dispatch_handle.detail["workflow_script"])
    handle = launcher.launch(workflow_script, agent_name=record.agent_name)

    return LaunchRecord(
        tier=tier,
        granted_authority=granted,
        dispatch=record,
        launch_handle=handle,
        tier2_gate_checked=tier2_gate_checked,
        tier2_gate_passed=tier2_gate_passed,
    )
