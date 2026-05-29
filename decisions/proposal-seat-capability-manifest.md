# Decision: Seat capability manifest

**Disposition:** Accept the pattern-shape convention; route the format-shape; hold promotion (recommended; awaiting Director ratification via merge)
**Origin:** [proposals/seat-capability-manifest.md](../proposals/seat-capability-manifest.md)
**Decided:** Drafted 2026-05-29 by oagp-strategist; Director ratifies on merge.
**Authorization:** PO observation 2026-05-29 ("our seat/position memory does not include relevant skills and plugins. They should"). Pattern-shape convention is delegated strategist authority; Director ratifies-by-merge.

## Rationale

Real gap, correctly surfaced. A seat is specified for *who it is* but not *what tooling it is equipped with*; skills live at the machine/install level and roledefs at the behavior level, with nothing seat-scoped between them. The fix — a seat capability manifest (skills + plugins + MCP surfaces) that onboarding and binding equip from — closes the onboarding gap, gives `bind()` the missing OAGP-layer input beyond runtime tools, and makes pattern #6 (substrate-is-sufficient-agent-context) actually hold.

Split by layer: the **convention** (seats SHOULD carry a manifest; onboarding/binding equip from it) is pattern-shape and decided here; the **encoding** is substrate format-shape and routed to roledef-strategist (primary) + orgdef-strategist (secondary).

## Resolutions to Open Questions

- **OQ1 (placement) / OQ2 (representation)** — format-shape; routed to roledef-strategist + orgdef-strategist. Not decided here.
- **OQ3 (bind() provisioning semantics)** — implementer design once the format lands; strategist lean: reference-first (bind() references the manifest in the bind-context; active install/activation is environment-specific, defer).

## Build directive

On Director ratification (merge):

1. **Decision recorded** (this artifact) — the seat-capability-manifest convention is the OAGP-pattern-shape position.
2. **Cross-spec coordination memo** to roledef-strategist (filed: [memos/2026-05-29-1900](../memos/2026-05-29-1900--oagp-strategist--roledef-strategist--seat-capability-manifest-format-shape-coordination.openthing)), flagging the orgdef:Position dimension for roledef↔orgdef coordination.
3. **Watch-item** added to CLAUDE.md known-work-items (active strategist): seat-capability-manifest — convention decided, format-shape routed, promotion held pending validation.
4. **Forward (not now):** when the format lands, the deferred `roledef:Job` items gain the manifest field; `/oagp-onboard` surfaces the occupied seat's manifest; `bind()` references it. Promotion to `recommended_patterns.general` is earned once the first seats carry manifests and bind/onboard exercise them.

## Cross-spec coordination

- roledef-strategist (primary), orgdef-strategist (secondary) — format-shape encoding (memos/2026-05-29-1900).
- No charter edit now (convention decided; field encoding pending; promotion held).

## Notable design choices

1. **Decide the convention, route the format, hold the promotion** — clean three-way split respecting both data-vs-pattern (#3) and promotion-follows-adoption (#8).
2. **Natural home is the deferred roledef:Job** — the manifest is one more job-specialization field, not a new construct.
3. **Reference-first bind() semantics (lean)** — provisioning skills into a runtime is environment-specific; binding should reference the manifest, not assume it can install.
4. **Framed as the mechanism that makes pattern #6 true** — not a contradiction of #6 but its completion; #6's text stands.

## Items not incorporated

- Promotion to `recommended_patterns.general` now — held per #8 (no derivations/validation yet).
- Deciding the field shape — format-shape; routed.
- Active install/activation semantics for bind() — deferred to implementer once format lands.

## Workflow validation

No charter edit (no version bump): this decides a convention and routes a dependency; the charter changes only when the format lands and/or the pattern earns promotion. Consistent with the bind-event-encoding precedent (pattern/content decided, format routed).

## Forward-reference resolution

- Format-shape reply from roledef-strategist (+ orgdef coordination) → then `roledef:Job` manifest field, `/oagp-onboard` surfacing, `bind()` referencing.
- Promotion to canonical recommended-pattern → earned on validation (first seats carry manifests; bind/onboard exercise them).

## References

- Proposal: [proposals/seat-capability-manifest.md](../proposals/seat-capability-manifest.md)
- Cross-spec memo: [memos/2026-05-29-1900](../memos/2026-05-29-1900--oagp-strategist--roledef-strategist--seat-capability-manifest-format-shape-coordination.openthing)
- Refines: recommended_patterns.general #6 (substrate-is-sufficient-agent-context), charter v0.1.9
- Related: the deferred roledef:Job items (all seats); bind() (agent-sdk); /oagp-onboard + /oagp-closeout
