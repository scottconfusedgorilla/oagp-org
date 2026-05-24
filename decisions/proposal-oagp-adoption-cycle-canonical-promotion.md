# Decision: Canonical promotion of `/oagp-bootstrap` + `/oagp-onboard`

**Disposition:** Accept (recommended; awaiting Director ratification via merge)
**Origin:** [proposals/oagp-adoption-cycle-canonical-promotion.md](../proposals/oagp-adoption-cycle-canonical-promotion.md)
**Decided:** Drafted 2026-05-23 by oagp-strategist; Director ratifies on merge.
**Authorization:** Director direction 2026-05-23 during oagp-strategist onboarding session: "Let's do both of those" — covering (a) staffing reflection and (b) taking up the canonical-promotion item as the first queue task. This authorizes the strategist drafting the decision; merge IS the Director's ratification of the decision itself.

## Rationale

Three independent arguments stand (per proposal §Motivation): adoption-barrier collapse; reference-implementation drift risk; compositional readiness (both sides empirically validated 2026-05-22).

The data-vs-pattern sharpening (orgdef-spec memo `2026-05-23-1100`) is the venue-correction prerequisite: the work is properly OAGP-pattern-shape, not orgdef-format-shape. Filing at oagp-org rather than orgdef-spec resolves the holding-venue problem the precursor (withdrawn) artifact diagnosed correctly but answered wrong.

The proposal preserves the cross-vendor red line structurally: skill content substrate-neutral and runtime-neutral; runtime adaptation tables enumerate non-Anthropic runtimes alongside Anthropic; delivery-package decisions (OQ1, OQ2) flagged for the implementer seat with substrate-neutral primer-text recommended ahead of plugin packaging.

## Resolutions to Open Questions

- **OQ1 — Cross-runtime delivery packaging timeline.** Resolved provisional: defer to implementer-seat staffing; cross-vendor neutrality requires no Anthropic-exclusive first package. Hard call awaits implementer seat.
- **OQ2 — OAGP plugin packaging strategic call.** Resolved provisional: substrate-neutral primer-text ships first; plugin packaging frames as transport-not-canonical. Hard call awaits implementer-seat staffing.
- **OQ3 — oagp.org canonical web hosting timeline.** Noted; not blocking; forward work for implementer seat.
- **OQ4 — Cross-spec FYI memos.** Resolved: not required at this stage. Canonical promotion has no format-shape implications; no substrate field requested.

## Build directive

On Director ratification (merge):

1. **README update** (`oagp-org/README.md`). The existing "Canonical adoption-cycle skills" section reads:
   > "Both skills are currently hosted at github.com/scottconfusedgorilla/thingalog/skills/ as canonical-by-reference pending re-homing into skills/ in this repo. See the inbox memos for canonical-promotion status."

   Adjust to:
   > "Both skills are designated canonical OAGP adoption-cycle primitives (decision: [decisions/proposal-oagp-adoption-cycle-canonical-promotion.md](decisions/proposal-oagp-adoption-cycle-canonical-promotion.md), 2026-05-23). Reference implementations are currently hosted at github.com/scottconfusedgorilla/thingalog/skills/ as canonical-by-reference; migration into oagp-org/skills/ is forward work for the implementer seat. Once oagp.org is live, canonical web hosting moves there."

2. **CLAUDE.md "Known work items" update**. Mark item 1 (canonical promotion) as resolved by this decision; items 2–8 remain active.

3. **Charter history entry** (`org/oagp-organization.opencatalog`). The v0.1.1 history entry already records both the seat staffing and this decision's drafting. Merge-ratification IS the canonical-promotion ratification.

4. **No cross-spec coordination memos required** (per OQ4 resolution).

## Cross-spec coordination

None at this stage.

## Notable design choices

1. **Holding venue is oagp-org** (not orgdef-spec, not a separate OAGP-spec sibling) — resolves the venue conflation the precursor diagnosed.
2. **Canonical-by-reference, not canonical-by-residence** — designation is independent of filesystem location; migration into `oagp-org/skills/` is forward work.
3. **Substrate-neutral primer-text recommended ahead of plugin packaging** — preserves the cross-vendor red line structurally; the first cross-runtime delivery should not be Anthropic-exclusive.
4. **Director-ratifies-by-merge convention** — strategist drafts; the merge IS the ratification; no separate ratification ceremony.
5. **OQs flagged for implementer seat** rather than left open-and-blocking — keeps the designation unblocked while honoring the bounded-authority distinction.

## Items not incorporated

- **Precursor "Authorization" trail citing Director's "do those two first" directive.** That directive ratified the precursor strategist's drafting effort; it does not carry into this fresh decision. Authorization for THIS decision is the Director's "Let's do both of those" direction 2026-05-23.
- **Precursor cross-spec FYI memo build directive.** Not carried; per OQ4 resolution, no FYI memos required.
- **Precursor "holding venue" framing.** Superseded; this decision uses "canonical-by-reference" explicitly without holding-venue language.

## Workflow validation

This decision is filed during the same session that staffed the strategist seat. Staffing and this decision both land in v0.1.1 of the charter (single Director-merge ratification expected). If the Director prefers two-commit cadence (staffing first, then decision), the decision artifact can be reserved for a follow-up v0.1.2 merge — strategist defers to Director on ratification cadence.

## Forward-reference resolution

- `decisions/proposal-bootstrap-session-transcript-position-tag.md` (transcript-tagging convention) — next queue item; separate decision forthcoming.
- Queue items 3–8 — open; pattern-promotion calls scheduled as separate decisions per item.

## Notes

Precursor (withdrawn) orgdef-spec artifacts preserved at:
- https://github.com/orgdef-spec/orgdef/blob/main/proposals/oagp-adoption-cycle-canonical-promotion.md (WITHDRAWN)
- https://github.com/orgdef-spec/orgdef/blob/main/decisions/proposal-oagp-adoption-cycle-canonical-promotion.md (WITHDRAWN)

Substantive analysis preserved as input material per [memos/2026-05-23-1200 — inbox-pointers-withdrawn-orgdef-strategist-artifacts](../memos/2026-05-23-1200--orgdef-strategist--oagp-strategist--inbox-pointers-withdrawn-orgdef-strategist-artifacts.body.md).

## References

- Proposal: [proposals/oagp-adoption-cycle-canonical-promotion.md](../proposals/oagp-adoption-cycle-canonical-promotion.md)
- Inbox pointer (originating memos): [memos/2026-05-23-1200 — inbox-pointers-thingalog-strategist-memos](../memos/2026-05-23-1200--orgdef-strategist--oagp-strategist--inbox-pointers-thingalog-strategist-memos.openthing)
- Inbox pointer (input material): [memos/2026-05-23-1200 — inbox-pointers-withdrawn-orgdef-strategist-artifacts](../memos/2026-05-23-1200--orgdef-strategist--oagp-strategist--inbox-pointers-withdrawn-orgdef-strategist-artifacts.openthing)
- Originating memos (in orgdef-spec): four memos enumerated in the inbox pointer above
- Data-vs-pattern sharpening: orgdef-spec memo `2026-05-23-1100--thingalog-strategist--orgdef-strategist--handoff-addendum-data-vs-pattern`
- Org charter: [org/oagp-organization.opencatalog](../org/oagp-organization.opencatalog)
- CLAUDE.md: [CLAUDE.md](../CLAUDE.md)
