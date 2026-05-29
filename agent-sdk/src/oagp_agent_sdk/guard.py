"""Tier-3 non-delegable-dispatch floor.

The hard governance floor: no bound agent — however elevated — may dispatch,
bind, or elevate another agent. This keeps every agent exactly one hop from a
human Director and prevents runaway proliferation.

Enforced ENVIRONMENTALLY, not by tool-omission or prompt text (an elevated
agent with a shell and an importable dispatcher could otherwise reach bind()
directly). Two layers, defense-in-depth:

1. **Env marker** — run_seat()'s backend sets OAGP_BOUND_AGENT=1 in the
   dispatched agent's environment. bind() and run_seat() refuse when it is set.
2. **Package-absence** — the dispatch environment should not expose
   oagp_agent_sdk to the bound agent at all (a backend/deployment concern;
   documented here, enforced at dispatch-environment construction). The env
   marker is the in-package enforceable layer; package-absence is the
   deployment-layer backstop.

There is NO parameter that grants dispatch authority to a bound agent. The
floor has no override.
"""

import os


BOUND_AGENT_ENV_MARKER = "OAGP_BOUND_AGENT"


class BoundAgentDispatchError(RuntimeError):
    """Raised when bind()/run_seat() is invoked from within a bound-agent
    execution context (Tier-3 floor violation)."""


def is_bound_agent_context() -> bool:
    """True if the current process is a dispatched bound-agent context.

    Detection is the env marker the dispatch backend sets on the dispatched
    agent. Truthy values: "1", "true", "yes" (case-insensitive). Absent or
    falsey → not a bound-agent context (normal dispatcher / interactive use).
    """
    val = os.environ.get(BOUND_AGENT_ENV_MARKER, "").strip().lower()
    return val in ("1", "true", "yes")


def assert_dispatch_allowed(operation: str = "dispatch") -> None:
    """Raise BoundAgentDispatchError if called inside a bound-agent context.

    Call this at the top of any dispatch/bind/elevate entry point. The Tier-3
    floor is non-negotiable and has no override parameter.
    """
    if is_bound_agent_context():
        raise BoundAgentDispatchError(
            f"Tier-3 floor: a bound agent cannot {operation} another agent. "
            f"This is a non-delegable hard floor with no override. "
            f"(Detected {BOUND_AGENT_ENV_MARKER} in the environment.)"
        )
