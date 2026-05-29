"""Bind-event memo emission (resolves the v0.1-deferred §7.4).

Every AUTONOMOUS dispatch emits a bind-event memo: the audit trail that
replaces live human supervision in unattended mode. (Interactive bind() from
v0.1 emits nothing; its trail is the agent-view session list.)

Envelope: memodef:Memo. `from` = the dispatching human's seat (director),
`to` = the dispatched seat. Records agent name, position id, org-state SHA,
granted authority (propose-only or the elevated action list), tier, timestamp,
and the brief.

Note: the filename-timestamp convention is an open coordination item with
memodef-strategist (memos/2026-05-25-0002). This emitter uses dispatch time
(sent-aligned) for both the filename prefix and the `sent` field; swap if the
ratified convention differs.
"""

import json
from datetime import datetime
from pathlib import Path


def _slug(s: str) -> str:
    out = []
    for ch in s.lower():
        if ch.isalnum():
            out.append(ch)
        elif out and out[-1] != "-":
            out.append("-")
    return "".join(out).strip("-") or "memo"


def emit_bind_event_memo(
    memos_dir: str | Path,
    *,
    from_seat: str,
    to_seat: str,
    agent_name: str,
    position_id: str,
    org_state_sha: str | None,
    granted_authority: list[str],
    tier: int,
    brief: str | None,
    now: datetime,
    roledef_id: str | None = None,
    roledef_version: str | None = None,
    roledef_source: str | None = None,
) -> Path:
    """Write a bind-event memo (.openthing envelope + .body.md) to memos_dir.

    Returns the path to the .openthing envelope. `now` is injected (not read
    from the clock) so callers control the timestamp and tests are
    deterministic.
    """
    memos_dir = Path(memos_dir)
    memos_dir.mkdir(parents=True, exist_ok=True)

    ts = now.strftime("%Y-%m-%d-%H%M")
    iso = now.strftime("%Y-%m-%dT%H:%M:%S")
    authority_label = "propose-only" if not granted_authority else ", ".join(granted_authority)

    stem = f"{ts}--{_slug(from_seat)}--{_slug(to_seat)}--bind-event-{_slug(agent_name)}"
    envelope_path = memos_dir / f"{stem}.openthing"
    body_path = memos_dir / f"{stem}.body.md"

    subject = (
        f"Bind-event: dispatched '{agent_name}' bound to position '{position_id}' "
        f"as Tier-{tier} ({authority_label}) against org-state "
        f"{org_state_sha or 'unknown'}"
    )

    envelope = {
        "catdef": "1.4",
        "memodef": "0.4.0",
        "type": "memodef:Memo",
        "from": from_seat,
        "to": to_seat,
        "subject": subject,
        "sent": f"{iso}-04:00",
        "action_required": False,
        "body": (
            f"Autonomous bind-event audit record. Agent '{agent_name}' was "
            f"dispatched bound to position '{position_id}' at Tier {tier} "
            f"(authority: {authority_label}) against org-state SHA "
            f"{org_state_sha or 'unknown'}. This memo is the audit trail that "
            f"replaces live human supervision for this unattended dispatch. "
            f"Brief and full grant detail in body_ref."
        ),
        "body_ref": body_path.name,
        "metadata": {
            "memo_subtype": "bind-event",
            "agent_name": agent_name,
            "position_id": position_id,
            "org_state_sha": org_state_sha,
            "tier": tier,
            "granted_authority": granted_authority,
            "roledef_id": roledef_id,
            "roledef_version": roledef_version,
            "roledef_source": roledef_source,
            "emitted_by": "oagp_agent_sdk.run_seat (autonomous dispatch)",
        },
    }

    envelope_path.write_text(
        json.dumps(envelope, indent=2) + "\n", encoding="utf-8"
    )

    body_lines = [
        f"# Bind-event: {agent_name}",
        "",
        f"**From:** {from_seat} (dispatching human's seat)",
        f"**To:** {to_seat} (dispatched seat)",
        f"**Dispatched:** {iso}",
        f"**Tier:** {tier} ({authority_label})",
        f"**Org-state SHA:** {org_state_sha or 'unknown'}",
        "",
        "---",
        "",
        "## Grant",
        "",
    ]
    if tier == 1 or not granted_authority:
        body_lines.append(
            "Propose-only. No commit/push/merge/tag/release capability granted; "
            "the agent is constructed without Director-capable tools. Output is "
            "draft files a human reviews and commits."
        )
    else:
        body_lines.append(
            f"Director-elevated. Granted actions: **{', '.join(granted_authority)}**. "
            f"The agent acts as the Director's delegated instrument; the human "
            f"Director remains accountable for everything the agent commits/pushes "
            f"under this grant."
        )
    body_lines += [
        "",
        "## Roledef",
        "",
        f"- id: {roledef_id or 'unknown'}",
        f"- version: {roledef_version or 'unknown'}",
        f"- source: {roledef_source or 'unknown'}",
        "",
        "## Brief",
        "",
        (brief or "_(no brief supplied)_"),
        "",
        "---",
        "",
        "_Tier-3 floor: this agent cannot dispatch, bind, or elevate another "
        "agent. Enforced environmentally; no override exists._",
        "",
        "_Emitted by oagp_agent_sdk.run_seat() on autonomous dispatch._",
        "",
    ]
    body_path.write_text("\n".join(body_lines), encoding="utf-8")

    return envelope_path
