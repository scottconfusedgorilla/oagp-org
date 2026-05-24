# Decision: Canonical adoption-cycle skill distribution v0.2 — family-level MCP + primer fallback

**Disposition:** Accept (recommended; awaiting Director ratification via merge)
**Origin:** [proposals/canonical-adoption-cycle-skill-distribution-v0.2.md](../proposals/canonical-adoption-cycle-skill-distribution-v0.2.md)
**Decided:** Drafted 2026-05-24 by oagp-strategist; Director ratifies on merge.
**Authorization:** Director direction 2026-05-24: "should we make it all available via MCP as well?" (with the originating Director-floated idea from 2026-05-21 captured by memodef-strategist in memos/2026-05-21-1140). Two converging signals (the 2026-05-21 architectural memo + the 2026-05-24 housekeeping consolidation) make the timing natural; Director-explicit on both.

## Rationale

Five arguments stand (per proposal §Motivation): cross-vendor canonical access at the transport layer; substrate-neutral by design; empirical friction signal (the 2026-05-24-0905 memo); architectural shape already worked out by memodef-strategist; GitHub-org consolidation makes the single-server architecture natural.

This decision ratifies memodef-strategist's 2026-05-21 architectural lean as the canonical shape:
- One MCP at `oagp.org/mcp` (not federated)
- Per-spec namespaced tools
- Read-only, additive, convenience cache (repos remain canonical source of truth)
- Per-spec strategist authority over namespaces
- Family stewards operate the server

The cross-vendor red line is preserved structurally: MCP is multi-vendor, so canonical transport at the MCP layer is structurally honest (unlike, say, distributing exclusively via Anthropic Marketplace). v0.3 (Claude Code plugin) remains scheduled after v0.2 per the v0.1 ordering commitment.

## Resolutions to Open Questions

- **OQ1 — Operator.** Resolved provisional: family stewards (Director + implementer-seat-when-staffed) operate `oagp.org/mcp` from the same infrastructure as the static site. Implementer-seat staffing formalizes the operational role.
- **OQ2 — Auth / rate-limiting.** Resolved provisional: open read access with per-IP rate limits. Auth would defeat the friction-reduction motivation; canonical content is public anyway.
- **OQ3 — Cache invalidation.** Resolved provisional: GitHub webhook on push to main → cache invalidation; periodic full-refresh fallback. Implementer-seat tunes specifics.
- **OQ4 — Tool API versioning.** Resolved: spec versions exposed in tool responses; tool API stable except by per-spec-strategist ratification.
- **OQ5 — Implementation language / framework.** Deferred to implementer-seat call when staffed. Recommendation: thin proxy; no heavy logic; existing MCP server frameworks (Python or Node) both viable.

## Build directive

On Director ratification (merge):

1. **MCP server implementation** — forward work for implementer-seat (vacant). Specifics:
   - Server lives in `oagp-org/oagp.org` repo (alongside the static site source) or in a sibling directory like `oagp-org/oagp.org/mcp/`
   - Read-only access to canonical content from `oagp-org/{oagp, catdef, roledef, orgdef, memodef}` and `catdef-spec/catdef`
   - Per-spec namespaced tools per proposal §Proposed Change item 2
   - Deployable to `oagp.org/mcp` once DNS + hosting infrastructure ready
2. **Static primer `oagp.org/primer.md`** — drafted by oagp-strategist as a separate small artifact; published as static content from `oagp-org/oagp.org` repo. Concise (≤200 lines): what OAGP is, substrate stack, canonical content locations, how to engage via MCP.
3. **README + charter updates** — README adds an MCP section + cross-runtime adoption-path table covering v0.1 / v0.2 / v0.3. Charter's `metadata.homepage` field is already `https://oagp.org (forthcoming)`; can update to remove "(forthcoming)" once the site is live.
4. **Cross-spec coordination memo** to memodef-strategist confirming the architectural lean is ratified.
5. **CLAUDE.md update** — known-work-items section: queue items 6 (plugin packaging) and 7 (cross-runtime delivery) and 8 (oagp.org canonical hosting) now substantially addressed; v0.3 (plugin) explicit forward work.
6. **Charter history entry** — v0.1.3 entry recording this decision and the oagp-online → oagp-org/oagp.org transfer.

## Cross-spec coordination

- Memo filed: [memos/2026-05-24-1900 — mcp architectural lean ratified v0.2 shipping](../memos/2026-05-24-1900--oagp-strategist--memodef-strategist--mcp-architectural-lean-ratified-v0.2-shipping.openthing). Closes the loop on the 2026-05-21 inbox item.
- Per-spec-strategist authority over their tool namespaces will require per-spec-strategist ratification of tool API design when implementer-seat builds the server. Not coordination-blocking now; just notification.
- No format-shape implications.

## Notable design choices

1. **One MCP not federated** — preserves friction-reduction; per-spec-namespaced tools give per-spec governance without per-spec endpoints.
2. **Read-only by design** — canonical content stays in the repos; MCP is convenience cache. This preserves memodef-strategist's mcpjam-rejection architectural commitment.
3. **Hosted from oagp-org/oagp.org repo infrastructure** — natural pairing; the static site and the MCP server share deployment.
4. **Primer.md as fallback** — non-MCP runtimes (today: many; tomorrow: fewer) still have a canonical entry point.
5. **Per-spec namespaces honor each strategist's authority** — even though it's one server, governance stays distributed.
6. **v0.2 ratifies memodef-strategist's 2026-05-21 lean as-is, substantially** — the strategist did the design work; this decision recognizes it as canonical without re-litigating.

## Items not incorporated

- **Federated per-spec MCPs** — rejected per proposal alternatives §1.
- **Anthropic Marketplace distribution** — rejected as v0.2; v0.3 (plugin) is the place for that, with the structural framing that v0.2 (cross-vendor MCP) already exists.
- **MCP-as-source-of-truth** — rejected per memodef-strategist's mcpjam-rejection rationale.
- **Implementer-seat-specific implementation choices** (language, framework) — deferred to implementer-seat call.

## Workflow validation

Lands in v0.1.3 of the charter. v0.1.1 was seat staffing + bootstrap+onboard canonical-promotion; v0.1.2 was v0.1 distribution + closeout canonicalization; v0.1.3 is v0.2 distribution + oagp.org repo move.

## Forward-reference resolution

- **v0.3 distribution** (Claude Code plugin packaging) remains scheduled. With v0.2 shipped, v0.3 has clean cross-vendor structural framing: plugin packaging is transport-not-canonical; cross-vendor MCP at oagp.org/mcp is the canonical transport that exists alongside.
- **Queue items 6 (plugin packaging), 7 (cross-runtime delivery), 8 (oagp.org canonical hosting)** — substantially addressed by v0.2 (item 7 + item 8 mostly resolved; item 6 = v0.3).
- **Implementer-seat staffing** is the natural next-strategic-question — the queue of forward work for that seat is large enough to justify staffing.

## References

- Proposal: [proposals/canonical-adoption-cycle-skill-distribution-v0.2.md](../proposals/canonical-adoption-cycle-skill-distribution-v0.2.md)
- Origin memos:
  - [memos/2026-05-21-1140 — memodef-strategist family-level MCP idea](../memos/2026-05-21-1140--memodef-strategist--oagp-strategist--family-level-mcp-distribution-idea.openthing)
  - [memos/2026-05-24-0905 — cross-machine skill deployment friction](../memos/2026-05-24-0905--orgdef-strategist--oagp-strategist--cross-machine-skill-deployment-friction-empirical-signal.body.md)
- Prior decisions:
  - [decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.1.md](proposal-canonical-adoption-cycle-skill-distribution-v0.1.md)
  - [decisions/proposal-oagp-closeout-canonical-promotion.md](proposal-oagp-closeout-canonical-promotion.md)
  - [decisions/proposal-oagp-adoption-cycle-canonical-promotion.md](proposal-oagp-adoption-cycle-canonical-promotion.md)
- Confirming memo: [memos/2026-05-24-1900 — mcp architectural lean ratified v0.2 shipping](../memos/2026-05-24-1900--oagp-strategist--memodef-strategist--mcp-architectural-lean-ratified-v0.2-shipping.openthing)
- Build artifacts: forward work (implementer-seat-vacant); primer.md, MCP server source, README updates scheduled.
- Repo at issue: [github.com/oagp-org/oagp.org](https://github.com/oagp-org/oagp.org)
- Org charter: [org/oagp-organization.opencatalog](../org/oagp-organization.opencatalog) (v0.1.3 history entry)
