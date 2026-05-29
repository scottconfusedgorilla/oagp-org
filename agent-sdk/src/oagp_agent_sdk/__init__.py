"""OAGP agent-sdk.

Public surface:
    bind(orgdef_path, position_id, ...) -> BindResult
        Interactive: bind an OAGP position to a Claude Code subagent file.
    run_seat(orgdef_path, position_id, ...) -> DispatchRecord
        Autonomous dispatch with structural bounded authority (Tier 1/2/3).

Graduated from prototype at s:/scratch/oagp-agent-prototype/ per
thingalog-strategist's 2026-05-23-1600 recommendation; v0.1 ratified by
oagp-strategist 2026-05-28; v0.2 (autonomous dispatch) built per the
2026-05-29 consolidated build-direction memo. See ../README.md.
"""

from .bind import bind, BindResult, RoledefResolutionError
from .run_seat import run_seat, DispatchRecord
from .backends import DispatchBackend, StubBackend, WorkflowsBackend, select_backend
from .launch import (
    launch_seat,
    LaunchRecord,
    LaunchHandle,
    SessionLauncher,
    StubSessionLauncher,
    ClaudeCliLauncher,
    Tier2GateError,
    verify_package_absent,
)
from .guard import (
    BoundAgentDispatchError,
    is_bound_agent_context,
    assert_dispatch_allowed,
)
from .authority import (
    Tier1ViolationError,
    UnknownDirectorActionError,
    DIRECTOR_CAPABLE_TOOLS,
    RECOGNIZED_DIRECTOR_ACTIONS,
)

__all__ = [
    "bind",
    "BindResult",
    "RoledefResolutionError",
    "run_seat",
    "DispatchRecord",
    "DispatchBackend",
    "StubBackend",
    "WorkflowsBackend",
    "select_backend",
    "launch_seat",
    "LaunchRecord",
    "LaunchHandle",
    "SessionLauncher",
    "StubSessionLauncher",
    "ClaudeCliLauncher",
    "Tier2GateError",
    "verify_package_absent",
    "BoundAgentDispatchError",
    "is_bound_agent_context",
    "assert_dispatch_allowed",
    "Tier1ViolationError",
    "UnknownDirectorActionError",
    "DIRECTOR_CAPABLE_TOOLS",
    "RECOGNIZED_DIRECTOR_ACTIONS",
]
__version__ = "0.2.0"
