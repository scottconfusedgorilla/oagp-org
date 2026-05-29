# Proposal: Consolidated pattern-promotion v1 — populate recommended_patterns.general

**Status:** Open (awaiting Director ratification via merge)
**Author:** oagp-strategist <oagp-strategist@oagp.org>
**Created:** 2026-05-29
**Target version:** oagp-org v0.1.9 (charter `recommended_patterns.general` population + version bump)
**Origin:** PO direction 2026-05-29 ("Let's do the consolidated pattern-promotion"). Retires the `[PATTERN-SHAPE DECISIONS DEFERRED...]` placeholder that has occupied `recommended_patterns.general` since v0.1.0. Candidates accumulated across: the orgdef-spec hand-off inventory (charter placeholder + memos/2026-05-23-0900); the bind/agent-sdk graduation (memos/2026-05-23-1600); the AGT + ETCLOVG positioning reviews; the Workflows relevance analysis (workflow wf_6a87be32-ee4); thingalog-strategist's candidate memos (2026-05-25-2000/2100); and the empirically-validated §8 autonomous-dispatch demo.

## Summary

Promote **eight** patterns to canonical `recommended_patterns.general`; **hold** two pending more derivation; **drop/archive** two as superseded or already-resolved. Each promoted pattern clears the org's own bar (promotion-follows-adoption: independent re-derivation and/or empirical validation; substrate-agnostic or clearly pattern-shape; red-line-clean).

## Promote (8)

**Governance core**

1. **Bounded-authority discipline** — AI seats read/draft/argue/propose; a human Director ratifies/merges/releases. No AI seat holds merge rights. *Evidence:* foundational (governance_model + CLAUDE.md); demonstrated continuously.
2. **Seat-vs-incumbent persistence** — positions persist; sessions are ephemeral; institutional memory lives in the substrate; inter-position coordination is asynchronous via memos addressed to seats. *Evidence:* multiple independent sessions inhabited the strategist + implementer seats with zero backfill beyond the substrate (incl. this onboarding). Absorbs the realized core of the earlier "async-organization positioning" candidate.
8. **Promotion-follows-adoption** — promote to canonical only after multiple independent derivations and/or empirical validation; extension-namespace-first until then. *Evidence:* inherited from catdef value #4; used as this org's curation discipline throughout (incl. this very decision).

**Substrate properties**

3. **Data-vs-pattern layering** — distinguish OAGP-pattern-shape from substrate/format-shape; route format-shape to the relevant substrate spec; keep canonical docs substrate-neutral. *Evidence:* Director-ratified 2026-05-23; governs all cross-spec routing.
4. **Org-state-fork-for-time-travel** — git-backed substrate ⇒ fork org state at any commit, bind an agent against that past state, zero future-leakage. *Evidence:* validated ×2 (2026-05-23 bind PoC; agent-sdk time-travel binding).
6. **Substrate-is-sufficient-agent-context** — an OAGP repo is itself the context a bound agent needs (roledef + orgdef + memos/decisions on disk); no RAG/separate KB for the basics. *Evidence:* bind() demos; PO observation "the needs of the agents aligned with the capabilities OAGP already provides."

**Agent-runtime**

5. **Bounded autonomous dispatch (three-tier)** — propose-only by construction (default) / explicit + audited human elevation (overridable) / non-delegable dispatch (hard floor, no override, environmentally enforced). Structural, not prompt-level. *Evidence:* §8 propose-only demo (2026-05-29); Tier-3 independently re-derived by Claude Code Workflows' one-level-nesting rule.
7. **Org-governance-layer-above-runtime** — OAGP is the cross-session organizational-governance layer; it composes OVER runtime execution/policy primitives, not competes with / is subsumed by them. *Evidence:* triply corroborated — Microsoft AGT (runtime policy, beneath); ETCLOVG harness taxonomy (OAGP = the underdeveloped org sub-layer of Governance); Claude Code Workflows (within-session execution OAGP composes over). Consolidates three separately-surfaced candidates into one.

## Hold (watch; not yet promoted)

- **AI-PM / synthesis-agent seat** (thingalog memos 2026-05-25-2000/2100) — cross-tenant feedback aggregation + recommendation-only synthesis. 2 derivations (Thingalog planned; Anthropic "Dreams"), but the Thingalog instance ships in 1–2 months; revisit with empirical proof-by-existence.
- **Three-tier permission composition** (anonymous / standard / Director-elevated MCP access) — 2 independent re-derivations (Thingalog feedback channel; catdef.org/mcp), one short of the threshold. Also likely **substrate-MCP-surface-shape, not OAGP-org-shape** → candidate for the catdef/memodef family rather than OAGP `recommended_patterns`. Watch for a third derivation (e.g. if oagp.org/mcp adopts the tiering).

## Drop / archive

- **Canonical-by-reference holding-venue framing** — transitional; superseded by canonical-residence-at-oagp-org (skills migrated 2026-05-24). Served its purpose.
- **Bootstrap-helper transcript-tagging convention** — already resolved and canonically encoded in `/oagp-closeout` Phase 2; a convention, not a general recommended pattern.

## Proposed Change

Replace the single placeholder string in `recommended_patterns.general` with the eight promoted patterns (as strings, preserving the array-of-strings shape). Bump charter 0.1.8 → 0.1.9; add history + author entries. Update CLAUDE.md known-work-items (the consolidated pattern-promotion item → resolved; placeholder retired).

## Format-shape restraint

`recommended_patterns.general` items stay **strings** (current shape). Defining a structured object shape for these items would be orgdef *format-shape* (orgdef-strategist's call), not OAGP pattern-shape. Promoting the patterns is content; restructuring the field is format. If a structured shape is later wanted, that routes to orgdef-strategist.

## Backward Compatibility

Additive content; no structural change. The recommended_roles array (already populated) is untouched. Adopter orgs that inherited the v0-baseline placeholder gain a concrete pattern set.

## Conformance Tests

1. `recommended_patterns.general` contains the eight promoted patterns; the placeholder string is gone.
2. Items remain strings (no format change).
3. Charter validates as JSON; version 0.1.9; history + authors extended.
4. No held/dropped candidate appears as promoted.

## Alternatives Considered

1. **Promote everything surfaced.** Rejected — the two held candidates haven't met the bar; promoting prematurely violates promotion-follows-adoption (which is itself pattern #8).
2. **Promote only the foundational three (1/2/3).** Rejected — 4–8 have earned it on evidence; under-promoting leaves the placeholder's intent unfinished.
3. **Mint a structured object shape for the items.** Rejected — orgdef format-shape, not OAGP's call; route to orgdef-strategist if wanted.
4. **Defer until launch.** Rejected — the placeholder has stood since v0.1.0; the candidates are ripe; this is refinement, not launch.

## Open Questions

- **OQ1 — structured shape for recommended_patterns.general items.** If desired, coordinate with orgdef-strategist (format-shape). Not blocking.
- **OQ2 — re-home patterns to canonical docs/primer.** The promoted patterns should eventually surface in oagp.org pattern documentation + primer; that's an implementer/docs follow-on, not part of this charter edit.

## Cross-spec coordination

- **orgdef-strategist** — only if OQ1 (structured item shape) is pursued.
- **catdef/memodef family** — the held three-tier-permission candidate likely belongs to their layer; flagged, not routed yet (awaits third derivation).
- No format-shape change in this proposal.
