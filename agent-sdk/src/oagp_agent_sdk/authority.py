"""Tier-1 / Tier-2 authority construction.

Bounded authority is STRUCTURAL, not prompt-level. The hard layer is the tool
list the agent is constructed with; the bind-context authority block only
*explains* the construction.

- Tier 1 (default): propose-only. The toolset contains no Director-capable
  tools (push/merge/commit/tag/release — in Claude Code, that capability rides
  on `Bash`). The agent drafts files; a human commits/merges. The agent is
  constructed unable, not asked to refrain.
- Tier 2 (explicit Director elevation): a deliberate `grant_director_actions`
  list adds the capable tools (hard layer) AND is recorded in a bind-event
  memo (audit layer). Never silent; never prompt-only.

Tier 3 (non-delegable dispatch) is enforced in guard.py, not here.
"""

from typing import Literal


# Tools that can mutate shared/published state (commit, push, merge, tag,
# release) — in Claude Code these all ride on shell access. Extensible: add
# network/MCP mutation tools here as they arise.
DIRECTOR_CAPABLE_TOOLS: frozenset[str] = frozenset({"Bash"})

# Default propose-only toolset when the caller requests none. File-level
# drafting + reading; no shell. Writing drafts is proposing; a human commits.
DEFAULT_PROPOSE_TOOLS: tuple[str, ...] = ("Read", "Write", "Edit", "Glob", "Grep")

# Director actions a Tier-2 grant may name. The list is the audit record; the
# tool addition is the hard layer.
RECOGNIZED_DIRECTOR_ACTIONS: frozenset[str] = frozenset(
    {"commit", "push", "merge", "tag", "release", "shell"}
)

Tier = Literal[1, 2]


class Tier1ViolationError(ValueError):
    """Raised when a Tier-1 (propose-only) dispatch is asked to include
    Director-capable tools without an explicit Tier-2 grant."""


class UnknownDirectorActionError(ValueError):
    """Raised when grant_director_actions names an unrecognized action."""


def resolve_tier(grant_director_actions: list[str] | None) -> Tier:
    """Tier 2 if a non-empty grant is present; Tier 1 otherwise."""
    if grant_director_actions:
        return 2
    return 1


def validate_director_actions(grant_director_actions: list[str] | None) -> list[str]:
    """Normalize + validate a grant list. Returns the (possibly empty) list.

    Raises UnknownDirectorActionError if any action is unrecognized — fail loud
    rather than silently granting something ambiguous.
    """
    if not grant_director_actions:
        return []
    normalized = [a.strip().lower() for a in grant_director_actions]
    unknown = [a for a in normalized if a not in RECOGNIZED_DIRECTOR_ACTIONS]
    if unknown:
        raise UnknownDirectorActionError(
            f"Unrecognized Director action(s): {unknown}. "
            f"Recognized: {sorted(RECOGNIZED_DIRECTOR_ACTIONS)}."
        )
    return normalized


def construct_toolset(
    requested_tools: list[str] | None,
    grant_director_actions: list[str] | None,
) -> tuple[list[str], Tier, list[str]]:
    """Build the agent's actual toolset for the resolved tier.

    Returns (toolset, tier, withheld). `withheld` is the set of
    Director-capable tools that were NOT granted (empty at Tier 2).

    Tier 1: requested tools minus nothing — but if the caller requested any
    Director-capable tool without a grant, raise (constructed-unable means the
    caller must go through Tier 2 explicitly, not smuggle capability in via the
    tools list).

    Tier 2: requested tools plus the capable tools the grant implies (Bash is
    added if absent, since granted git actions need a shell).
    """
    tier = resolve_tier(grant_director_actions)
    requested = list(requested_tools) if requested_tools else list(DEFAULT_PROPOSE_TOOLS)
    capable_in_request = [t for t in requested if t in DIRECTOR_CAPABLE_TOOLS]

    if tier == 1:
        if capable_in_request:
            raise Tier1ViolationError(
                f"Tier-1 propose-only dispatch cannot include Director-capable "
                f"tools {capable_in_request}. Pass grant_director_actions=[...] "
                f"for explicit, audited Tier-2 elevation."
            )
        return requested, tier, sorted(DIRECTOR_CAPABLE_TOOLS)

    # Tier 2: capable tools permitted; ensure shell present so the granted
    # actions are actually executable.
    toolset = list(requested)
    for capable in sorted(DIRECTOR_CAPABLE_TOOLS):
        if capable not in toolset:
            toolset.append(capable)
    return toolset, tier, []


def propose_only_block() -> str:
    """Tier-1 bind-context authority block. Explains the construction; the
    tool omission is the actual enforcement."""
    return (
        "# Authority — Tier 1 (propose-only)\n\n"
        "You are dispatched with PROPOSE-ONLY authority. You have no commit, "
        "push, merge, tag, or release capability: those tools are absent from "
        "your toolset by construction, not by request, and not because you were "
        "asked to refrain. Do your work by writing files (proposals, memos, "
        "drafts) into the working tree; a human Director reviews and "
        "commits/merges your output. You also cannot dispatch, bind, or elevate "
        "another agent (non-delegable dispatch floor; no override exists)."
    )


def elevated_block(actions: list[str]) -> str:
    """Tier-2 bind-context authority block. States the granted authority
    honestly. The tool addition is the actual capability."""
    return (
        "# Authority — Tier 2 (Director-elevated)\n\n"
        f"The human Director has explicitly granted you these actions: "
        f"{', '.join(actions)}. You act as the Director's delegated instrument "
        f"for them; the Director remains accountable, and a bind-event memo "
        f"records this grant (who, what, when, against which org-state). Use the "
        f"authority only as your brief directs. You still cannot dispatch, bind, "
        f"or elevate another agent (non-delegable dispatch floor; no override)."
    )


def authority_block(tier: Tier, actions: list[str]) -> str:
    """The bind-context authority block for the resolved tier."""
    return elevated_block(actions) if tier == 2 else propose_only_block()
