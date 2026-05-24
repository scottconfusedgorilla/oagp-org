# Proposal: Designate `/oagp-closeout` as the canonical OAGP session-cycle closing skill

**Status:** Open (awaiting Director ratification via merge)
**Author:** oagp-strategist <oagp-strategist@oagp.org>
**Created:** 2026-05-24
**Target version:** oagp-org v0.1.2 (rolling into the existing v0.1.2 bundle)
**Origin:** Director direction 2026-05-24: "I'd actually like to add one more skill first: oagp-closeout. This would be a very simple skill that will prompt the AI to write a closeout memo, and then prompt the human to save the transcript."

## Summary

Designate `/oagp-closeout` as the canonical OAGP **session-cycle** closing skill, companion to `/oagp-onboard` which opens the session-cycle. The skill drafts a closeout memo capturing the session's drafted artifacts and open items, then prompts the PO to save the session transcript using the canonical position-tag convention.

Closeout completes the **session-cycle** (onboard → working session → closeout); distinct from the **adoption-cycle** (bootstrap → operational use → onboard for every joiner) canonicalized 2026-05-23.

## Motivation

Three independent arguments:

1. **Session-cycle completeness.** Without a canonical closeout primitive, every session ends without institutional capture — the memo trail has gaps the next incumbent must reconstruct from artifact diffs and chat scrollback. Closeout makes per-session capture the default.

2. **Canonical transcript-position-tag convention venue.** The closeout skill is the natural canonical reference for the transcript-position-tag bifurcation (staffed-seat → seat name; bootstrap → `<orgname>-bootstrap-helper`). The convention has prior precursor analysis (withdrawn orgdef-strategist artifact recommending `<orgname>-bootstrap-helper` for bootstrap sessions) and empirical confirmation (Director's 2026-05-23 transcript save tagged `oagp-strategist` for a staffed-seat working session). Closeout's Phase 2 table is the canonical encoding. This resolves queue item 2 (transcript-tagging convention) for the canonical case.

3. **Companion to onboard.** Onboard is canonical (per 2026-05-23 decision); closeout symmetrically pairs with it. Without closeout, the session-cycle is open at one end. With closeout, the session-cycle is structurally complete.

## Proposed Change

1. **Designation.** `/oagp-closeout` is the canonical OAGP session-cycle closing skill. Canonical content lives at `oagp-org/skills/oagp-closeout/SKILL.md`.

2. **Two-phase shape.**
   - Phase 1: Draft a closeout memo (from-seat-to-seat institutional capture).
   - Phase 2: Prompt the PO to save the transcript at the canonical `transcripts/<seat>/...` path.

3. **Transcript-position-tag convention** canonically encoded in the SKILL.md Phase 2 table:
   - Staffed-seat working session → seat id (e.g., `oagp-strategist`)
   - Bootstrap session → `<orgname>-bootstrap-helper`
   - Unattached / exploratory → `unattached-ai` (or omit)

4. **Distribution.** Closeout ships through the same v0.1 distribution mechanism as bootstrap + onboard (Claude Code install scripts updated to include closeout; README updated to list all three canonical skills). Drafted as part of the v0.1.2 bundle, ratified by the same Director merge.

5. **Cross-vendor neutrality preserved.** SKILL.md is substrate-neutral and runtime-neutral; the Adapting-to-runtime table enumerates non-Anthropic runtimes alongside Anthropic. Same red-line discipline as bootstrap + onboard.

## Backward Compatibility

Not applicable — no prior canonical closeout designation exists.

## Conformance Tests

A skill is OAGP-conformant session-cycle closing content when:

1. It is `/oagp-closeout` OR derives from it with substantive equivalence.
2. It runs the two-phase shape: memo draft, then transcript-save prompt.
3. It does not save the transcript itself — that's a PO/runtime action.
4. The closeout memo is `from-seat-to-seat` (institutional, not narrative-to-PO).
5. The transcript-position-tag convention is honored (staffed-seat → seat id; bootstrap → `<orgname>-bootstrap-helper`).
6. The skill stops at "stand by" after Phase 2 — does not auto-commit, does not auto-staff, does not bundle multiple sessions.

## Alternatives Considered

1. **Don't canonicalize; let adopter orgs invent their own closeout convention.** Rejected. Drift risk — session-cycle conventions would fragment across adopter orgs; the substrate's labor-multiplier property weakens when each org reinvents closeout shape.
2. **Bundle with the onboard canonicalization retroactively.** Rejected. The 2026-05-23 decision is uncommitted but specifically scoped to bootstrap+onboard; expanding it now would be revisionist. Separate proposal is cleaner.
3. **Wait for empirical validation before canonicalizing.** Rejected. The skill is small, low-risk, and the Director directed canonicalization today. Empirical validation can happen against canonical content; iterating before designation slows adoption.
4. **Encode the transcript-tagging convention in a separate document rather than in the closeout SKILL.md.** Rejected. The skill IS the canonical reference; encoding the convention where it's operationally enforced minimizes drift between document and behavior.
5. **Frame closeout as part of the adoption-cycle.** Rejected. Adoption is one-shot per project (bootstrap); session-cycle is recurring (onboard / closeout per session). Different cycles, different categories.

## Open Questions

- **OQ1 — Transcript-position-tag convention scope.** This proposal canonically encodes the bifurcation for the three common cases (staffed, bootstrap, unattached). Edge cases (multi-org sessions where the AI works across two orgs in one session; role transitions mid-session where the seat changes; multi-AI sessions where two AIs participate in the same transcript) are not addressed here. Provisional: queue item 2 (transcript-tagging) is closed by this decision for the canonical case; edge-case extensions can ship as subsequent convention decisions if they surface.
- **OQ2 — Closeout memo addressing for handoff sessions.** If a session ends with the AI handing off the seat to a new incumbent (rare but possible), should the closeout memo be `to: director` rather than `to: <seat>`? Provisional: still `to: <seat>` — the memo is for the seat's institutional history; the handoff is captured in the body, not in addressing. Edge case worth flagging for future revision.

## Cross-spec coordination

None required at this stage. No format-shape implications; the skill uses existing substrate primitives (memodef:Memo for the closeout artifact; memodef:Transcript at the canonical path for the save).
