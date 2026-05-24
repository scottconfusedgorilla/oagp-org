# Decision: Canonical promotion of `/oagp-closeout`

**Disposition:** Accept (recommended; awaiting Director ratification via merge)
**Origin:** [proposals/oagp-closeout-canonical-promotion.md](../proposals/oagp-closeout-canonical-promotion.md)
**Decided:** Drafted 2026-05-24 by oagp-strategist; Director ratifies on merge.
**Authorization:** Director direction 2026-05-24: "I'd actually like to add one more skill first: oagp-closeout. This would be a very simple skill that will prompt the AI to write a closeout memo, and then prompt the human to save the transcript."

## Rationale

Three independent arguments stand (per proposal §Motivation): session-cycle completeness; canonical transcript-position-tag convention venue (resolves queue item 2 for the canonical case); structural companion to onboard.

The skill is small and low-risk. Empirical validation will happen against canonical content rather than before designation; the same approach that worked for bootstrap+onboard (which had empirical anchors but was promoted via formal canonicalization rather than empirical-anchoring-alone).

Distribution rides on the v0.1 mechanism already in flight (install scripts, README install section, junction/symlink). No separate distribution decision needed; the v0.1 distribution decision's build directive is amended in the same merge to include closeout.

## Resolutions to Open Questions

- **OQ1 — Transcript-position-tag convention scope.** Resolved: queue item 2 (transcript-tagging) closed for the canonical case (staffed-seat, bootstrap, unattached). Edge cases (multi-org sessions, mid-session role transitions, multi-AI sessions) deferred to subsequent convention decisions if they surface in practice.
- **OQ2 — Closeout memo addressing for handoff sessions.** Resolved provisional: `to: <seat>` is correct; handoff is captured in the body, not in addressing. Revisit if a real handoff session demonstrates the framing is wrong.

## Build directive

On Director ratification (merge):

1. **Skill file** at `oagp-org/skills/oagp-closeout/SKILL.md` (drafted; awaiting merge).
2. **Install scripts** at `oagp-org/install/install-claude-code-skills.{ps1,sh}` updated to include `oagp-closeout` in the skills array.
3. **README update** — the "Canonical adoption-cycle skills" section reframed to list all three canonical skills with cycle-role labels (adoption-cycle: bootstrap; session-cycle: onboard + closeout).
4. **v0.1 distribution decision amended** to include closeout in distribution scope (proposals + decisions for `canonical-adoption-cycle-skill-distribution-v0.1` updated; build directive widened).
5. **CLAUDE.md known-work-items** — queue item 2 (transcript-tagging convention) marked resolved by this decision for the canonical case; new entry added for the closeout-canonicalization.
6. **Charter v0.1.2 history entry** amended to reflect the third canonical skill and this decision.

## Cross-spec coordination

None. No format-shape implications.

## Notable design choices

1. **Closeout completes the session-cycle** (with onboard); distinct from the adoption-cycle (bootstrap + onboard-for-joining). Two cycles, three skills.
2. **Transcript-tagging convention canonically encoded in the closeout SKILL.md** rather than in a separate convention document — the skill IS the canonical reference; encoding the convention where it's operationally enforced minimizes drift.
3. **Bundled with v0.1 distribution decision in a single merge** — one Director ratification covers v0.1.2 (canonical-promotion 2026-05-23 + v0.1 distribution 2026-05-24 + closeout canonicalization 2026-05-24).
4. **Queue item 2 resolved as a side effect** — the closeout skill's Phase 2 table IS the convention's canonical form; ratifying the skill ratifies the convention.
5. **Edge cases deferred-with-clear-path** — multi-org / mid-session-role-transition / multi-AI cases flagged for future convention decisions if they surface; not blocking v0.1.2.

## Items not incorporated

- **Empirical-validation-before-designation.** Rejected per proposal alternatives §3. Director directed canonicalization today; iteration happens against canonical content.
- **Separate transcript-tagging convention document.** Rejected per proposal alternatives §4. The skill is the canonical reference.
- **Adoption-cycle framing for closeout.** Rejected per proposal alternatives §5. Closeout is session-cycle, not adoption-cycle.

## Workflow validation

Lands in v0.1.2 of the charter alongside the canonical-promotion 2026-05-23 decision (bootstrap+onboard) and the v0.1 distribution decision (2026-05-24). Single Director-merge ratifies all three. If the Director prefers separate commits, the three artifacts can land in three commits (canonical-promotion bootstrap+onboard; v0.1 distribution; closeout canonicalization) — strategist defers to Director on commit cadence.

## Forward-reference resolution

- **Queue item 2 (transcript-tagging convention) resolved for the canonical case.** Edge cases tracked but not blocking.
- **Queue item 7 (cross-runtime delivery) partially-addressed by v0.1 distribution** — closeout shipping through the same mechanism extends the partial-address to all three canonical skills uniformly.
- **bind / agent-sdk graduation, canonical-orgs library residence reply, items 3-5 of original queue, items 6 (plugin packaging) and 8 (oagp.org hosting)** remain open.

## Notes

This decision is unusually small for a canonical-promotion artifact — most of the substantive design lives in the SKILL.md itself (which IS the canonical content). The decision artifact's job is to ratify the SKILL.md as canonical and to record the strategist call; the rationale-for-canonicalization is correspondingly compact.

## References

- Proposal: [proposals/oagp-closeout-canonical-promotion.md](../proposals/oagp-closeout-canonical-promotion.md)
- Companion canonical-promotion: [decisions/proposal-oagp-adoption-cycle-canonical-promotion.md](proposal-oagp-adoption-cycle-canonical-promotion.md) (bootstrap+onboard, 2026-05-23)
- Distribution decision: [decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.1.md](proposal-canonical-adoption-cycle-skill-distribution-v0.1.md)
- Build artifacts:
  - [skills/oagp-closeout/SKILL.md](../skills/oagp-closeout/SKILL.md)
  - [install/install-claude-code-skills.ps1](../install/install-claude-code-skills.ps1)
  - [install/install-claude-code-skills.sh](../install/install-claude-code-skills.sh)
- Org charter: [org/oagp-organization.opencatalog](../org/oagp-organization.opencatalog) (v0.1.2 history entry amended)
- CLAUDE.md: [CLAUDE.md](../CLAUDE.md)
