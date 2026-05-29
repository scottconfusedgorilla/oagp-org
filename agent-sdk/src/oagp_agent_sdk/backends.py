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
    ) -> DispatchHandle:
        """Launch the dispatched agent. `env` MUST be applied to the dispatched
        agent's environment (it carries the Tier-3 bound-agent marker)."""
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
    ) -> DispatchHandle:
        handle = DispatchHandle(
            backend=self.name,
            agent_file=agent_file,
            env=dict(env),
            brief=brief,
            launched=False,
            detail={"note": "stub backend — dispatch recorded, not launched"},
        )
        self.dispatches.append(handle)
        return handle


class WorkflowsBackend(DispatchBackend):
    """Claude Code native Workflows-class dispatcher backend.

    Deferred per PO direction 2026-05-29 (governance core + stub first; live
    Workflows wiring is a focused follow-up). When wired, this composes over
    the native dispatcher rather than bespoke subprocess plumbing, and MUST:
    - set the Tier-3 bound-agent env marker in the dispatched environment,
    - NOT expose oagp_agent_sdk to the dispatched agent (package-absence floor).
    """

    name = "workflows"

    def dispatch(
        self,
        agent_file: Path,
        *,
        brief: str | None,
        env: dict[str, str],
    ) -> DispatchHandle:
        raise NotImplementedError(
            "WorkflowsBackend is deferred (v0.2 follow-up). The governance core "
            "runs on StubBackend; conformance test 8 (Workflows delegation) is "
            "pending this wiring."
        )


def select_backend(runtime: str = "auto") -> DispatchBackend:
    """Select a dispatch backend for the runtime.

    Currently returns StubBackend in all cases (the live Workflows path is a
    deferred follow-up). When wired, "auto" detects Claude Code and returns
    WorkflowsBackend; other runtimes get their own backends.
    """
    return StubBackend()
