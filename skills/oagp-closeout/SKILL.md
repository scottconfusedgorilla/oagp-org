---
name: oagp-closeout
description: |
  Use this skill at the end of a working session in an OAGP-shaped
  organization. The skill drafts a closeout memo capturing what was
  drafted, decided, in flight, or left open in this session, then
  prompts the Product Owner to save the session transcript using the
  canonical position-tag convention.

  Activate when the user says any of: "close out", "wrap up",
  "end of session", "session closeout", "let's close this session",
  or when a session reaches a natural stopping point.

  The companion skill is /oagp-onboard, used at the start of a
  session. Onboard begins the session-cycle; closeout ends it.
  Together they bracket every working session in an OAGP-shaped org.
---

# /oagp-closeout

You are closing out a working session in an OAGP-shaped organization. Two things:

1. **Draft a closeout memo** capturing what happened this session.
2. **Prompt the Product Owner** to save the session transcript.

You do not save the transcript yourself.

---

## Phase 1 — Draft the closeout memo

File at:

```
memos/<YYYY-MM-DD>-<HHMM>--<seat>--<seat>--<short-summary>.openthing
memos/<YYYY-MM-DD>-<HHMM>--<seat>--<seat>--<short-summary>.body.md
```

`from` and `to` both name the seat you occupied this session (e.g., `oagp-strategist`). The memo is institutional capture for that seat's history — your future replacements read it on their next onboard.

**If you were unattached** (no specific seat occupied; exploratory PO conversation), use `unattached-ai` for `from` and note the framing in `metadata.scope_check`.

**Required content:**

- **Subject:** one-line session summary.
- **Body:** brief institutional capture covering:
  - What was drafted (artifacts created or modified, with paths)
  - What was decided (strategist calls; flag any "awaiting Director merge-ratification")
  - What's in flight (work that started but didn't land)
  - What's open (items surfaced but not addressed)
  - References to related artifacts
- `action_required`: usually `false` (closeout is institutional capture, not action). Set `true` only if a specific follow-up genuinely needs attention from the next session.
- `metadata.drafted_by_session`: model + working directory.
- `metadata.scope_check`: confirms the memo is within the drafting seat's scope (or acknowledges unattached framing).
- `metadata.applies_principles`: 2-3 principles this closeout enacts (e.g., `feedback_substrate_is_workplace_not_documentation`, `seat-vs-incumbent`).

Match the org's existing memo tone: terse, evidence-led, no editorial polish, no celebration of work-completed. The memo's value is durable context for the next incumbent, not narrative for the current PO.

---

## Phase 2 — Prompt the transcript save

After drafting the memo, surface the canonical transcript-save path to the PO:

```
transcripts/<seat>/<YYYY-MM-DD>-<HHMM>--<seat>--<short-description>.openthing
transcripts/<seat>/<YYYY-MM-DD>-<HHMM>--<seat>--<short-description>.body.md
```

The canonical `<seat>` value per session type:

| Session type | `<seat>` value |
|---|---|
| Staffed-seat working session (e.g., the strategist has been working) | The seat's id (e.g., `oagp-strategist`, `oagp-implementer`) |
| Bootstrap session (org doesn't exist yet; AI is the bootstrap helper) | `<orgname>-bootstrap-helper` |
| Unattached / exploratory | `unattached-ai` (or omit save if not institutionally relevant) |

**Print the canonical path in plaintext** so the PO can copy it. Then stand by — transcript-save is a runtime-dependent PO action:

- **Claude Code:** PO uses `ccc-ninja`, the `/transcripts` skill, or manual export.
- **Claude-for-Chrome:** PO uses C4C's transcript capture.
- **claude.ai (web):** PO downloads the chat and commits.
- **ChatGPT / Gemini / other:** Whatever export mechanism the runtime offers.

Your job is to surface the canonical path so the PO knows where the file goes. The runtime owns the conversation state; you cannot export it yourself.

---

## Discipline (load-bearing)

**1. AI drafts; PO ratifies.** Closeout memo is a draft like any other artifact. PO reviews before merge. No auto-commit.

**2. Institutional, not narrative.** Durable context for the seat's next incumbent (or an auditor reading the seat's history in six months), not a retrospective for the PO's reading enjoyment.

**3. Position-tag identifies the seat, not the session.** `oagp-strategist`, not `oagp-strategist-2026-05-24` or `claude-opus-strategist-session`. The seat persists; the session is ephemeral.

**4. Bootstrap sessions are special-cased.** During `/oagp-bootstrap`, the org's permanent positions don't yet exist — the AI is a transient `<orgname>-bootstrap-helper`. If the AI continues operating in the new org after Phase 5 hand-off, subsequent sessions re-tag against the actual staffed position.

**5. You cannot save the transcript.** Even with filesystem access. The runtime owns the conversation state (including tool calls and system reminders); only PO-side tooling can export the full transcript.

**6. Don't close out mid-task.** If invoked while substantive work is in flight, ask: "Are we genuinely closing the session, or do you want a mid-session checkpoint?" Closeout is for session-end, not arbitrary checkpoints. If the PO confirms mid-session checkpoint, file a checkpoint memo (different subject framing) rather than a closeout memo.

**7. Closeout is content, not approval.** Filing a closeout memo does not ratify in-flight work — drafts remain drafts; the Director still merges. The closeout just captures state.

---

## What this skill does NOT do

- Save the transcript (PO/runtime action)
- Auto-commit the closeout memo (PO ratifies, Director merges)
- Write performance reviews, session retrospectives, or marketing copy
- Staff or vacate seats (separate decisions)
- Summarize work from prior sessions (only this session's work)
- Bundle multiple sessions into one closeout (one memo per session)

---

## Adapting to runtime

| Runtime | Memo drafting | Transcript save (PO action) |
|---|---|---|
| **Claude Code** | Direct filesystem write to `memos/` | `ccc-ninja` or equivalent transcript-export tool |
| **Claude-for-Chrome** | Generate memo content; PO commits via web UI | C4C transcript capture |
| **claude.ai (web)** | Generate memo as artifact; PO copies to repo | PO downloads chat |
| **ChatGPT / Gemini / other** | Generate memo as text; PO commits manually | Runtime-specific export |

The canonical transcript-save path is invariant across runtimes; only the save mechanism differs.

---

## References

- **Companion skill:** [/oagp-onboard](../oagp-onboard/SKILL.md) — opens the session-cycle
- **Adoption-cycle skill:** [/oagp-bootstrap](../oagp-bootstrap/SKILL.md) — one-shot per project; runs once when adopting OAGP
- **Substrate stack:** catdef (schema-as-data) → roledef → orgdef → memodef → transcriptdef (this skill produces a `memodef:Memo` and prompts a `memodef:Transcript` save)
- **Empirical reference org:** [github.com/scottconfusedgorilla/oagp-org](https://github.com/scottconfusedgorilla/oagp-org) (this repo)
- **OAGP spec home:** [oagp.org](https://oagp.org) (when canonical)
