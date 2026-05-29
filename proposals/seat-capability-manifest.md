# Proposal: Seat capability manifest — seats carry their relevant skills, plugins, and MCP surfaces

**Status:** Open (awaiting Director ratification via merge)
**Author:** oagp-strategist <oagp-strategist@oagp.org>
**Created:** 2026-05-29
**Target version:** charter unaffected for now (pattern-shape convention; not yet a `recommended_patterns.general` promotion — see §Promotion discipline)
**Origin:** PO observation 2026-05-29: *"our seat/position memory does not include relevant skills and plugins. They should."* PO hit this as a concrete limitation in-session.

## Summary

Establish the pattern-shape convention that an OAGP **seat's definition SHOULD carry a capability manifest** — the canonical skills, plugins, and MCP surfaces relevant to (or required by) that seat — and that **onboarding and binding equip from it.** The *encoding* (where the field lives, its schema) is substrate format-shape, routed to roledef-strategist (primary) and orgdef-strategist. This closes the gap the PO hit and makes pattern #6 (substrate-is-sufficient-agent-context) actually hold.

## Motivation

Today a seat is specified by identity/voice/output_contract/guardrails (roledef) + a position description (orgdef). Skills are installed at the **machine** level (`install/install-claude-code-skills.*`); roledefs describe **behavior**. Nothing at the **seat** level enumerates the tooling that is part of doing the seat's job. Consequences:

1. **Onboarding gap.** A fresh peer taking a seat learns who it is from the substrate but not what tooling it is equipped with. (E.g., the oagp-strategist seat uses `/oagp-closeout` and `/oagp-init`; the implementer seat uses the agent-sdk and the install scripts — none of this is in the seat definition.) The PO hit exactly this.
2. **Binding gap.** `bind()` sets runtime tools (Read/Write/Bash) in the subagent frontmatter, but not OAGP-layer capability (which skills/plugins/MCP surfaces the bound agent should have/know). The capability manifest is the missing input.
3. **It undercuts pattern #6.** "Substrate-is-sufficient-agent-context" claims the repo IS the context a bound agent needs. If the seat needs tooling the substrate doesn't enumerate, the substrate is not quite sufficient. The manifest is what makes #6 true.

## Proposed Change (pattern-shape)

1. **Convention (SHOULD):** an OAGP seat's definition carries a **capability manifest** — relevant skills (e.g. `/oagp-closeout`), plugins, and MCP surfaces (e.g. catdef.org/mcp), each ideally annotated required-vs-recommended and with a one-line "why this seat uses it."
2. **Natural home:** the deferred `roledef:Job` item (which already carries charter/identity/voice/output_contract/guardrails — the manifest is one more field). Role-general tooling lives at the roledef/job level; org-specific seat additions may live at the `orgdef:Position` level. Exact placement is format-shape (routed).
3. **Onboarding equips from it:** `/oagp-onboard` surfaces the seat's manifest when a peer takes the seat ("this seat uses X, Y, Z").
4. **Binding provisions from it:** `bind()` reads the manifest and provisions/references the seat's skills+plugins in the bound agent's context (beyond the runtime `tools:` list).
5. **Content is authored per-seat** (by the strategist or the seat incumbent, Director-ratified) — like every other seat-specific field.

## Promotion discipline (why this is NOT yet a recommended_patterns promotion)

Per pattern #8 (promotion-follows-adoption, ratified v0.1.9 today), a fresh insight with zero derivations and no validation does not go straight into `recommended_patterns.general`. This proposal **designs and decides the convention**; promotion to canonical recommended-pattern is **earned later**, once the first seats actually carry manifests and bind/onboard exercise them (the validation). Surfaced as a watch-item alongside the other held candidates.

## Format-shape dependency (routed, not decided here)

How roledef/orgdef encodes the manifest — field name, schema, required-vs-recommended representation, roledef:Job vs orgdef:Position placement — is substrate format-shape:
- **roledef-strategist (primary):** the role/job-level manifest field.
- **orgdef-strategist (secondary):** any `orgdef:Position`-level extension for org-specific seat tooling.

Cross-spec coordination memo filed to roledef-strategist (flagging the orgdef dimension).

## Backward Compatibility

Additive. Seats without a manifest behave as today. The deferred job-specialization for all current seats remains deferred; the manifest joins the list of fields authored when a seat's job specializes.

## Conformance Tests (once the format lands)

1. A seat definition can carry a capability manifest (skills + plugins + MCP surfaces).
2. `/oagp-onboard` surfaces the occupied seat's manifest.
3. `bind()` provisions/references the manifest's skills+plugins in the bound agent context.
4. A seat with no manifest still onboards/binds (graceful absence).

## Alternatives Considered

1. **Leave tooling at the machine/install level only.** Rejected — that's the gap; machine-level install doesn't tell a seat what it's equipped with, and doesn't travel with the seat across machines/runtimes.
2. **Put it only in CLAUDE.md prose.** Rejected — not seat-scoped, not machine-readable for bind(), doesn't compose with roledef-driven binding.
3. **Promote straight to recommended_patterns.general now.** Rejected — violates promotion-follows-adoption (#8); zero derivations/validation yet.
4. **Decide the field shape here.** Rejected — format-shape; routes to substrate strategists.

## Open Questions

- **OQ1 — roledef:Job vs orgdef:Position placement** (format-shape; roledef-strategist + orgdef-strategist).
- **OQ2 — required-vs-recommended representation** and whether MCP surfaces, skills, and plugins share one manifest or separate lists (format-shape).
- **OQ3 — bind() provisioning semantics** — does bind() merely *reference* the manifest in the bind-context, or actively *install/activate*? Implementer design once the format lands; lean reference-first (provisioning skills into a runtime is environment-specific).

## Cross-spec coordination

- **roledef-strategist** (primary) + **orgdef-strategist** (secondary) — format-shape encoding.
- Refines pattern #6 (substrate-is-sufficient-agent-context); does not amend the charter now (the refinement is the mechanism that makes #6 fully true; #6's text stands).
