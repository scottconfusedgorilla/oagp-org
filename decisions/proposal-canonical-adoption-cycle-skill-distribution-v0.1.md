# Decision: Canonical adoption-cycle skill distribution v0.1

**Disposition:** Accept (recommended; awaiting Director ratification via merge)
**Origin:** [proposals/canonical-adoption-cycle-skill-distribution-v0.1.md](../proposals/canonical-adoption-cycle-skill-distribution-v0.1.md)
**Decided:** Drafted 2026-05-24 by oagp-strategist; Director ratifies on merge.
**Authorization:** Director direction 2026-05-24: "the very first is to think about how we get the oagp-onboard skill onto a new machine. Tying to thingalog makes no sense :-)" and "Agreed, do A and B, and agreed, you do it and omnibus." Direct PO direction; merge is the seal.

## Rationale

Three signals converge: the 0905 friction memo documents PO experiencing the breakage today; the 0900 coordination memo asks the structural question (where does pattern-shape canonical content live post-sharpening); the PO directive answers conclusively. The canonical-promotion decision 2026-05-23 already designated the skills as canonically OAGP's; this decision moves residence to match.

The proposal preserves the cross-vendor red line structurally by separating the v0.1 / v0.2 / v0.3 distribution decisions: v0.1 (this decision) is Claude-Code-specific transport, but lives openly in oagp-org (not vendor-marketed). v0.2 (next) is substrate-neutral primer URL — serves non-Claude-Code AIs equally. v0.3 (last) is Anthropic-marketplace plugin packaging — ships AFTER v0.2 so the framing "plugin is convenience transport; canonical access exists without it" is structurally honest.

Residence migration is decoupled from content evolution. `SKILL.md` files land verbatim at oagp-org; content updates (re-pointing references, adding oagp-org as a canonical-pattern-source alongside thingalog as empirical-application-example) are deferred to a content-evolution decision so the migration is content-preserving and risk-minimal.

## Resolutions to Open Questions

- **OQ1 — thingalog/skills/ deprecation timeline.** Resolved: cross-spec coordination memo to thingalog-strategist proposes a deprecation timeline; thingalog-strategist's call to ratify, revise, or reject. Not blocking this decision.
- **OQ2 — Install script vendoring.** Resolved provisional: HEAD-tracking is the v0.1 default; version-pinning support is future enhancement, not required for the friction this decision addresses.
- **OQ3 — Auto-update wrapper.** Resolved: not in v0.1 scope. Considered cheap; revisit as a v0.1.1 if PO uses install in anger and finds the manual `git pull` step annoying.
- **OQ4 — Cross-runtime primer URL location.** Deferred to v0.2 (the substrate-neutral primer decision). Resolution unblocks v0.3.

## Build directive

On Director ratification (merge):

1. **Skill files migrated and authored.** `oagp-org/skills/oagp-bootstrap/SKILL.md` and `oagp-org/skills/oagp-onboard/SKILL.md` populated with verbatim copies of the 2026-05-23 thingalog SKILL.md content. `oagp-org/skills/oagp-closeout/SKILL.md` newly authored 2026-05-24 (canonical first version; no migration required; canonicalization decision: [decisions/proposal-oagp-closeout-canonical-promotion.md](proposal-oagp-closeout-canonical-promotion.md)).
2. **Install scripts.** `oagp-org/install/install-claude-code-skills.ps1` (Windows) and `oagp-org/install/install-claude-code-skills.sh` (macOS / Linux). The `$skills` array includes all three canonical skills.
3. **README update.** `oagp-org/README.md` gets:
   - A new "Quick install (Claude Code)" section with the clone + script recipe.
   - The "Canonical skills" section (renamed from "Canonical adoption-cycle skills") reframed to list all three canonical skills with cycle-role labels (adoption-cycle: bootstrap; session-cycle: onboard + closeout).
4. **Cross-spec coordination memo to thingalog-strategist.** Filed at `memos/2026-05-24-1200--oagp-strategist--thingalog-strategist--canonical-skill-residence-migrated-thingalog-skills-deprecation-coordination.{openthing,body.md}`. Proposes deprecation timeline for thingalog/skills/ in favor of oagp-org/skills/. Coordination scope covers bootstrap + onboard (the two skills with thingalog residence history); closeout has no thingalog history.
5. **Charter history entry.** v0.1.2 entry in `org/oagp-organization.opencatalog` recording this decision and the closeout-canonicalization decision; version bumped 0.1.1 → 0.1.2.
6. **CLAUDE.md update.** "Known work items" section updated: queue items 6 (plugin packaging) and 7 (cross-runtime delivery) now partially addressed by this v0.1 decision; queue item 2 (transcript-tagging convention) resolved by the closeout-canonicalization decision for the canonical case; v0.2 (substrate-neutral primer) and v0.3 (plugin packaging) explicit as forward work; closeout-canonicalization listed as a resolved item.

## Cross-spec coordination

- Memo to thingalog-strategist (build directive item 4) — proposes thingalog/skills/ deprecation timeline.
- Reply memo to orgdef-strategist (separate; not in this decision's build directive) — answers their 0900 coordination question for the skill case; flags the canonical-orgs template case for a separate decision.
- **No format-shape implications.** No -def-spec coordination required.

## Notable design choices

1. **Verbatim content migration.** Residence change decoupled from content evolution. Empirical-validated content preserved as-shipped 2026-05-23; v0.2 will handle re-pointing references.
2. **Junction/symlink default in install scripts.** Preserves the "`git pull` keeps installs fresh" property; user retains control of update timing.
3. **No thingalog deletion.** Existing junctions on already-installed machines keep working; backward-compat without churn. Deprecation is thingalog-strategist's call.
4. **Cross-vendor red line preserved structurally.** Claude-Code-specific install scripts live openly in oagp-org (not Anthropic-marketed). v0.2 ships substrate-neutral primer-URL before v0.3 ships Anthropic-marketplace plugin packaging.
5. **v0.1 / v0.2 / v0.3 versioning of distribution.** Incremental ratification cycle; small enough to ratify quickly each step; each version's framing is structurally honest about what the prior version covered.
6. **Build directive includes cross-spec coordination memo.** Strategist drafts the memo as part of the omnibus; Director ratifies the bundle via merge. Memo carries no commitments thingalog-strategist hasn't reviewed; it proposes.

## Items not incorporated

- **Substrate-neutral primer URL (PRIMER.md / oagp.org/primer).** Deferred to v0.2 — not in v0.1 because v0.1 addresses the urgent Claude-Code-on-new-machine friction. Primer URL serves a different audience (non-Claude-Code AIs).
- **Claude Code plugin packaging.** Deferred to v0.3 — must ship after v0.2 per cross-vendor red line.
- **Auto-update wrapper script.** Deferred per OQ3 resolution; revisit as v0.1.1 if used-in-anger experience shows it's worth the line count.
- **Content updates to SKILL.md.** Deferred to a separate content-evolution decision (provisional v0.2 of the canonical-promotion decision lineage, distinct from this distribution decision's v0.2). Re-pointing references from "thingalog is the canonical reference" to "oagp-org is the canonical home; thingalog is the empirical-application example" is substantive content authority.
- **thingalog/skills/ deletion.** Out of scope; thingalog-strategist's call.

## Workflow validation

This decision lands in v0.1.2 of the charter. v0.1.0 was scaffolding; v0.1.1 was seat-staffing + canonical-promotion; v0.1.2 is this distribution decision. One decision per version bump cadence maintained.

The build directive contains an unusual element: a cross-spec coordination memo (item 4) is drafted as part of the same bundle. Convention: strategist drafts artifacts including cross-spec memos; Director's merge ratifies the bundle. The drafted memo carries no commitments thingalog-strategist hasn't reviewed — it proposes, they ratify-revise-or-reject in their own seat's process. No bypass of bounded authority.

## Forward-reference resolution

- **v0.2 (substrate-neutral primer URL)** scheduled. Origin: OQ4 of this decision; cross-vendor red line; queue item 7 (cross-runtime delivery).
- **v0.3 (Claude Code plugin packaging)** scheduled. Origin: queue item 6; ships after v0.2.
- **Content-evolution decision** (separate lineage) scheduled. Re-points thingalog references in SKILL.md to reflect oagp-org as canonical home.
- **Canonical-orgs template residence decision** (separate; replies to the 0900 memo's main question) — flagged in cross-spec coordination; orgdef-strategist's coordination request remains open for that case.

## Notes

The cross-vendor framing matters even at v0.1: the v0.1 install scripts are Claude-Code-specific in effect, but they live openly in oagp-org (a public open-pattern repo), not in an Anthropic-marketed channel. The framing "this is a way to install Claude Code skills from a canonical OAGP source" is structurally different from "OAGP comes packaged as a Claude Code plugin from Anthropic's marketplace." The latter is what v0.3 must navigate carefully; the former is fine.

## References

- Proposal: [proposals/canonical-adoption-cycle-skill-distribution-v0.1.md](../proposals/canonical-adoption-cycle-skill-distribution-v0.1.md)
- Origin memos:
  - [memos/2026-05-24-0900 — schema-v1.1.0-ship-fyi-and-canonical-orgs-residence-fwd-ref](../memos/2026-05-24-0900--orgdef-strategist--oagp-strategist--schema-v1.1.0-ship-fyi-and-canonical-orgs-residence-fwd-ref.body.md)
  - [memos/2026-05-24-0905 — cross-machine-skill-deployment-friction-empirical-signal](../memos/2026-05-24-0905--orgdef-strategist--oagp-strategist--cross-machine-skill-deployment-friction-empirical-signal.body.md)
- Prior decision: [decisions/proposal-oagp-adoption-cycle-canonical-promotion.md](../decisions/proposal-oagp-adoption-cycle-canonical-promotion.md)
- Build artifacts:
  - [skills/oagp-bootstrap/SKILL.md](../skills/oagp-bootstrap/SKILL.md)
  - [skills/oagp-onboard/SKILL.md](../skills/oagp-onboard/SKILL.md)
  - [install/install-claude-code-skills.ps1](../install/install-claude-code-skills.ps1)
  - [install/install-claude-code-skills.sh](../install/install-claude-code-skills.sh)
- Cross-spec coordination memo: [memos/2026-05-24-1200 — canonical-skill-residence-migrated-thingalog-skills-deprecation-coordination](../memos/2026-05-24-1200--oagp-strategist--thingalog-strategist--canonical-skill-residence-migrated-thingalog-skills-deprecation-coordination.openthing)
- Org charter: [org/oagp-organization.opencatalog](../org/oagp-organization.opencatalog) (v0.1.2 history entry)
- CLAUDE.md: [CLAUDE.md](../CLAUDE.md)
