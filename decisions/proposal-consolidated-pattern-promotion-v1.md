# Decision: Consolidated pattern-promotion v1

**Disposition:** Accept (recommended; awaiting Director ratification via merge)
**Origin:** [proposals/consolidated-pattern-promotion-v1.md](../proposals/consolidated-pattern-promotion-v1.md)
**Decided:** Drafted 2026-05-29 by oagp-strategist; Director ratifies on merge.
**Authorization:** PO direction 2026-05-29 ("Let's do the consolidated pattern-promotion"). Pattern-promotion is delegated strategist authority per governance_model; Director ratifies-by-merge.

## Rationale

The charter's `recommended_patterns.general` has carried a `[DEFERRED]` placeholder since v0.1.0, awaiting the staffed strategist's curation. The candidate pool is now ripe: eight patterns have earned canonical status by the org's own bar (promotion-follows-adoption — independent re-derivation and/or empirical validation), two have not yet, and two are superseded/already-resolved. This decision promotes the eight, holds the two, and drops the two, and populates the charter accordingly.

The promotions cluster: governance core (bounded authority; seat-vs-incumbent; promotion-follows-adoption), substrate properties (data-vs-pattern layering; org-state-fork-for-time-travel; substrate-is-sufficient-agent-context), and agent-runtime (bounded autonomous dispatch; org-governance-layer-above-runtime). The agent-runtime pair is the freshest but among the best-evidenced — both were empirically validated or independently re-derived in the past week.

## Resolutions to Open Questions

- **OQ1 — structured item shape.** Deferred; kept strings to avoid orgdef format-shape overreach. Route to orgdef-strategist only if a structured shape is later wanted.
- **OQ2 — re-home to docs/primer.** Implementer/docs follow-on; not part of this charter edit. The promoted patterns should surface in oagp.org pattern documentation + primer when those are built/refined.

## Build directive

On Director ratification (merge):

1. **Charter `recommended_patterns.general`** — replace the placeholder string with the eight promoted pattern strings (done in this commit; Director's merge ratifies).
2. **Charter version** 0.1.8 → 0.1.9; history entry + author entry (done in this commit).
3. **CLAUDE.md known-work-items** — mark the consolidated pattern-promotion item resolved; note `recommended_patterns.general` is populated (no longer placeholder); move the two held candidates to a "watch" note; record the two drops (done in this commit).
4. **Follow-on (not this commit):** the promoted patterns surface in oagp.org pattern documentation + primer (implementer/docs scope, when built).

## Cross-spec coordination

- orgdef-strategist — only if OQ1 (structured item shape) is pursued.
- catdef/memodef family — the held three-tier-permission candidate likely belongs to their layer; flagged for them, routed on a third derivation.

## Notable design choices

1. **Eight promoted, not all candidates** — promotion-follows-adoption applied to the promotion decision itself; the two held candidates haven't met the bar.
2. **Consolidated the AGT / ETCLOVG / Workflows candidates into one pattern (#7)** — they're facets of one layering insight; three entries would have been redundant.
3. **Absorbed "async-organization positioning" into seat-vs-incumbent (#2)** rather than minting a separate pattern — the realized core (async memo coordination across persistent seats) is what's validated; the broader positioning is not separately crisp.
4. **Kept items as strings** — format-shape restraint; restructuring the field is orgdef-strategist's call.
5. **Held the thingalog candidates rather than promoting on the strength of their surfacing** — respects the seat boundary (thingalog-strategist surfaced as observation; promotion is mine) and the evidence bar (one ships in 1–2 months; the other is one derivation short and arguably substrate-layer).

## Items not incorporated

- The two held candidates (AI-PM seat; three-tier permission) — watch-listed, not promoted.
- The two dropped candidates (canonical-by-reference holding-venue; bootstrap-helper transcript-tagging) — superseded / already-resolved.
- A structured object shape for the items — orgdef format-shape; not taken.

## Workflow validation

Charter edited directly in this decision's commit (no cross-session collision risk — single active session, charter freshly reconciled to v0.1.8). Version → v0.1.9. This is content population of an existing field, not a schema change.

## Forward-reference resolution

- `recommended_patterns.general` placeholder — **retired** by this decision.
- Held candidates — revisit: AI-PM seat when Thingalog's ships (~1–2 months); three-tier permission on a third independent derivation.
- Promoted patterns → oagp.org docs/primer — implementer/docs follow-on.
- Pattern-promotion as an ongoing function — future patterns promote via the same discipline (#8) as they earn it; this is "v1" of the curated set, not the final word.

## References

- Proposal: [proposals/consolidated-pattern-promotion-v1.md](../proposals/consolidated-pattern-promotion-v1.md)
- Candidate sources: charter v0.1.0 placeholder; memos/2026-05-23-0900 (hand-off inventory); memos/2026-05-23-1600 (bind/agent-sdk); the AGT + ETCLOVG reviews; workflow wf_6a87be32-ee4 (Workflows relevance); memos/2026-05-25-2000 + 2026-05-25-2100 (thingalog candidates); decisions/proposal-agent-sdk-v0.2-* (bounded autonomous dispatch); memos/2026-05-29-1700 + 1800 (§8 demo validation)
- Charter: [org/oagp-organization.opencatalog](../org/oagp-organization.opencatalog) (v0.1.9)
- CLAUDE.md: [CLAUDE.md](../CLAUDE.md)
