"""OAGP agent-sdk.

Public surface:
    bind(orgdef_path, position_id, ...) -> BindResult
        Bind an OAGP position to a Claude Code subagent file.

Graduated from prototype at s:/scratch/oagp-agent-prototype/ per
thingalog-strategist's 2026-05-23-1600 recommendation memo and
oagp-strategist's ratification (see ../README.md for provenance chain).
"""

from .bind import bind, BindResult

__all__ = ["bind", "BindResult"]
__version__ = "0.1.0"
