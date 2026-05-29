"""oagp_agent_sdk.bind — graduate of the bind() prototype.

Emits a Claude Code subagent file from an OAGP position + roledef so the
bound role can be dispatched as the main agent of a background session via
the Claude Code agent view (`claude agents` / VSCode panel).

Empirical lessons preserved from the prototype (see ../../README.md and
memos/2026-05-23-1600 §5 for the field-derived rationale):

    1. Claude Code's agent view is the canonical observation surface;
       this module does NOT build a separate UI.
    2. Subagent file shape: `.claude/agents/<name>.md` with YAML
       frontmatter; required fields name + description; useful fields
       tools, model, permissionMode, color, initialPrompt, maxTurns.
    3. Flat path; single-hyphen names. The VSCode agent view does not
       recurse into subdirectories; the `name:` frontmatter rejects
       double-hyphens.
    4. permissionMode "acceptEdits" is the sensible default for
       interactive use; "bypassPermissions" cannot be loaded from
       frontmatter without prior interactive acceptance (security
       floor enforced by Claude Code).
    5. Time-travel mechanics: per-commit granularity is natural for
       OAGP (substrate IS commits). bind() against a `git worktree
       add <path> <sha>` directory works as-is.
    6. Bind-event memo discipline is deferred until first unattended
       use (scheduler, run_seat(), cron). For interactive use, the
       audit trail is the agent view's session list itself.

Out of scope for v0.1 graduation:
    - CLI dispatch wrapper (`claude --bg --agent <name>`) — deferred.
    - run_seat() / scheduler — deferred.
    - bind-event memo filing — deferred per lesson 6.
    - Caller-provided inline roledef override — not surfaced as a need.
"""

import json
import re
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

from .guard import assert_dispatch_allowed


# Map roledef id -> color for visual identification in the agent view panel.
# Anything not in this map gets `cyan` (see bind() color fallback).
_ROLE_COLOR: dict[str, str] = {
    "blackhat-tester": "red",
    "senior-project-oriented-software-engineer": "blue",
    "product-strategist": "purple",
    "implementer": "green",
}


RoledefSource = Literal["url", "embedded"]


class RoledefResolutionError(RuntimeError):
    """Raised in fail-closed mode when a roledef URL fetch fails and embedded
    fallback is not explicitly permitted. Prevents an autonomous agent from
    silently booting with the wrong identity."""


@dataclass
class BindResult:
    """Returned by bind(). Tells the caller where the subagent file landed
    and how to dispatch it via the agent view panel."""
    agent_file: Path
    agent_name: str
    description: str
    org_name: str
    org_id: str | None
    orgdef_path: str
    position_id: str
    position_name: str
    position_status: str
    roledef_id: str
    roledef_version: str
    roledef_source: RoledefSource
    roledef_url: str | None
    dispatch_hint: str  # ready-to-copy: "@<name> <brief>" or just "@<name>"


def _load_orgdef(orgdef_path: Path) -> dict[str, Any]:
    with orgdef_path.open(encoding="utf-8") as f:
        return json.load(f)


def _find_position(orgdef: dict[str, Any], position_id: str) -> dict[str, Any]:
    for item in orgdef.get("items", []):
        if item.get("type") == "orgdef:Position" and item.get("id") == position_id:
            return item
    raise ValueError(
        f"Position '{position_id}' not found in orgdef "
        f"(saw: {[i.get('id') for i in orgdef.get('items', []) if i.get('type') == 'orgdef:Position']})"
    )


def _resolve_roledef(
    position: dict[str, Any],
    *,
    fail_closed: bool = False,
    allow_embedded_fallback: bool = True,
) -> tuple[dict[str, Any], RoledefSource, str | None]:
    """Return (roledef, source, url). Tries URL fetch first.

    Resolution modes:
    - fail_closed=False (default; v0.1 interactive behavior): URL fetch failure
      prints a warning and falls back to the embedded `job_definition`.
    - fail_closed=True (autonomous mode): URL fetch failure raises
      RoledefResolutionError UNLESS allow_embedded_fallback=True, in which case
      it falls back to embedded with a warning.

    A position that declares ONLY an embedded job_definition (no URL) always
    resolves to embedded — that is the declared source, not a silent fallback.
    """
    role_def = position.get("role_definition") or {}
    url = role_def.get("url")
    embedded = role_def.get("job_definition")
    if url:
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "oagp-agent-sdk/0.2 (+https://oagp.org)"},
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode("utf-8")), "url", url
        except Exception as e:
            if fail_closed and not allow_embedded_fallback:
                raise RoledefResolutionError(
                    f"Roledef URL fetch failed ({url}) in fail-closed mode and "
                    f"embedded fallback is not permitted. Pass "
                    f"allow_embedded_fallback=True to opt into the embedded copy, "
                    f"or fix the URL. Original error: {e}"
                ) from e
            print(f"[bind] URL fetch failed ({url}): {e}; trying embedded fallback")

    if embedded:
        return embedded, "embedded", url

    raise ValueError(
        f"Position '{position.get('id')}' has no resolvable roledef "
        f"(no URL fetch and no embedded job_definition)"
    )


def _synthesize_body(
    roledef: dict[str, Any],
    org_name: str,
    position_name: str,
    position_status: str,
    orgdef_path: Path,
    memos_dir: Path,
    extra_context: str,
) -> str:
    """Render the markdown body that becomes the subagent's system prompt.

    Section order: Bind context, Identity, Voice, Guardrails,
    Conversation rules, Workflow, Output contract, Additional context.
    Sections absent from the roledef are skipped silently.
    """
    sections: list[str] = []

    sections.append(
        f"# Bind context\n\n"
        f"You are bound to the **{position_name}** position in **{org_name}** "
        f"(seat status: {position_status}).\n\n"
        f"Org state on disk: `{orgdef_path}`\n"
        f"Memos directory: `{memos_dir}`\n\n"
        f"Read the org state and any action-required memos addressed to your "
        f"position before acting. File memos via `memos/<ISO-timestamp>--"
        f"<from-position>--<to-position>--<subject>.openthing` plus a "
        f"`.body.md` companion when the body is non-trivial."
    )

    sections.append(f"# Identity\n\n{roledef.get('identity', '(no identity provided)')}")

    if voice := roledef.get("voice"):
        sections.append(f"# Voice\n\n{voice}")

    if guardrails := roledef.get("guardrails"):
        sections.append("# Guardrails\n\n" + "\n".join(f"- {g}" for g in guardrails))

    if rules := roledef.get("conversation_rules"):
        sections.append("# Conversation rules\n\n" + "\n".join(f"- {r}" for r in rules))

    if workflow := roledef.get("workflow"):
        sections.append("# Workflow\n\n```json\n" + json.dumps(workflow, indent=2) + "\n```")

    if contract := roledef.get("output_contract"):
        lines = ["# Output contract\n"]
        for o in contract:
            lines.append(f"## {o.get('name')}\n")
            lines.append(o.get("description", ""))
            if schema := o.get("schema"):
                lines.append(f"\n**Schema:** {schema}")
            if dest := o.get("destination"):
                lines.append(f"\n**Destination:** {dest}")
            lines.append("")
        sections.append("\n".join(lines))

    if extra_context:
        sections.append(f"# Additional context\n\n{extra_context}")

    return "\n\n---\n\n".join(sections)


def _slugify(s: str) -> str:
    """Lowercase + hyphens for the `name` field. Claude Code's subagent
    discovery rejects names with characters outside [a-z0-9-] and rejects
    double-hyphen separators (empirically verified in the prototype)."""
    s = s.lower()
    s = re.sub(r"[^a-z0-9-]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def _yaml_escape(s: str) -> str:
    """Escape a string for a single-line YAML scalar."""
    s = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return f'"{s}"'


def _render_frontmatter(fields: dict[str, Any]) -> str:
    """Render a small YAML frontmatter block. Only scalar and string-list
    values are needed for the Claude Code subagent schema. `initialPrompt`
    is rendered as a literal block to preserve newlines in the brief."""
    lines = ["---"]
    for key, value in fields.items():
        if value is None:
            continue
        if isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, (int, float)):
            lines.append(f"{key}: {value}")
        elif isinstance(value, list):
            if not value:
                continue
            lines.append(f"{key}: {', '.join(value)}")
        elif key == "initialPrompt":
            lines.append(f"{key}: |")
            for ln in str(value).splitlines() or [""]:
                lines.append(f"  {ln}")
        else:
            lines.append(f"{key}: {_yaml_escape(str(value))}")
    lines.append("---")
    return "\n".join(lines)


def bind(
    orgdef_path: str | Path,
    position_id: str,
    *,
    agents_root: str | Path = ".claude/agents",
    context_tag: str | None = None,
    initial_prompt: str | None = None,
    tools: list[str] | None = None,
    model: str = "inherit",
    permission_mode: str = "acceptEdits",
    max_turns: int | None = None,
    color: str | None = None,
    extra_context: str = "",
    roledef_fail_closed: bool = False,
    allow_embedded_fallback: bool = True,
) -> BindResult:
    """Bind an OAGP position to a Claude Code subagent file.

    Parameters
    ----------
    orgdef_path : str | Path
        Path to the org's ``.opencatalog`` JSON (catdef-family substrate).
    position_id : str
        Id of the ``orgdef:Position`` item within the orgdef to bind.
    agents_root : str | Path, optional
        Where the subagent file lands. Relative paths resolve against the
        orgdef's project root (parent of ``org/``); absolute paths used
        as-is. Default: ``.claude/agents`` under the project root. The
        VSCode agent view does not recurse, so the file lands directly in
        ``agents_root`` (no subdirectory).
    context_tag : str | None, optional
        Suffix appended to the agent name with a single hyphen, e.g.
        ``"tt-2026-05-16"`` for a time-travel variant. ``None`` means the
        agent name is just ``<position-id>``.
    initial_prompt : str | None, optional
        If given, baked into ``initialPrompt:`` frontmatter so the
        dispatcher can invoke with just ``@<name>``. Multi-line preserved.
    tools : list[str] | None, optional
        Allowed-tools list, e.g. ``["Read", "Write", "Glob", "Grep", "Bash"]``.
    model : str, optional
        Subagent model. Default ``"inherit"`` (uses the session's main model).
    permission_mode : str, optional
        Default ``"acceptEdits"``. See lesson 4 in the module docstring.
    max_turns : int | None, optional
        Subagent turn budget. ``None`` for unbounded (subject to model limits).
    color : str | None, optional
        Visual identification in the agent view panel. ``None`` consults
        the roledef-id color map; falls back to ``"cyan"``.
    extra_context : str, optional
        Extra prose appended to the synthesized body (e.g. time-travel
        instructions, scope override). Distinct from ``initial_prompt``:
        ``extra_context`` is part of the system prompt; ``initial_prompt``
        is the dispatcher's first user message.

    Returns
    -------
    BindResult
        Describes where the subagent file landed plus everything the
        caller needs to dispatch it.

    Raises
    ------
    ValueError
        If ``position_id`` is not present in the orgdef, or if the
        position has neither a fetchable URL nor an embedded
        ``job_definition`` for the roledef.
    """
    assert_dispatch_allowed("bind")
    orgdef_path = Path(orgdef_path).resolve()
    orgdef = _load_orgdef(orgdef_path)
    position = _find_position(orgdef, position_id)
    roledef, source, url = _resolve_roledef(
        position,
        fail_closed=roledef_fail_closed,
        allow_embedded_fallback=allow_embedded_fallback,
    )

    org_meta = next(
        (i for i in orgdef.get("items", []) if i.get("type") == "orgdef:Organization"),
        None,
    ) or {}
    org_name = org_meta.get("name") or orgdef.get("name") or "(unnamed org)"
    org_id = org_meta.get("id") or orgdef.get("id")

    project_root = orgdef_path.parent.parent
    memos_dir = project_root / "memos"

    agents_root_path = Path(agents_root)
    if not agents_root_path.is_absolute():
        agents_root_path = project_root / agents_root_path
    agents_root_path.mkdir(parents=True, exist_ok=True)

    base_name = _slugify(position_id)
    if context_tag:
        base_name = f"{base_name}-{_slugify(context_tag)}"
    agent_file = agents_root_path / f"{base_name}.md"

    description = (
        f"{position.get('name', position_id)} for {org_name}. "
        f"Roledef: {roledef.get('name', roledef.get('id', 'unknown'))} "
        f"v{roledef.get('version', '?')}. "
        f"Source: {source}. Bind-tag: {context_tag or 'none'}."
    )

    body = _synthesize_body(
        roledef=roledef,
        org_name=org_name,
        position_name=position.get("name", position_id),
        position_status=position.get("status", "unknown"),
        orgdef_path=orgdef_path,
        memos_dir=memos_dir,
        extra_context=extra_context,
    )

    frontmatter = _render_frontmatter({
        "name": base_name,
        "description": description,
        "tools": tools or None,
        "model": model,
        "permissionMode": permission_mode,
        "maxTurns": max_turns,
        "color": color or _ROLE_COLOR.get(roledef.get("id", ""), "cyan"),
        "initialPrompt": initial_prompt,
    })

    agent_file.write_text(frontmatter + "\n\n" + body + "\n", encoding="utf-8")

    if initial_prompt:
        dispatch_hint = f"@{base_name}"
    else:
        dispatch_hint = f"@{base_name} <your engagement brief here>"

    return BindResult(
        agent_file=agent_file,
        agent_name=base_name,
        description=description,
        org_name=org_name,
        org_id=org_id,
        orgdef_path=str(orgdef_path),
        position_id=position_id,
        position_name=position.get("name", position_id),
        position_status=position.get("status", "unknown"),
        roledef_id=roledef.get("id", "unknown"),
        roledef_version=roledef.get("version", "unknown"),
        roledef_source=source,
        roledef_url=url,
        dispatch_hint=dispatch_hint,
    )
