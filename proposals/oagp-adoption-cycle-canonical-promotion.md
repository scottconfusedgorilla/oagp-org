# Proposal: Designate `/oagp-bootstrap` + `/oagp-onboard` as canonical OAGP adoption-cycle primitives

**Status:** Open (awaiting Director ratification via merge)
**Author:** oagp-strategist <oagp-strategist@oagp.org>
**Created:** 2026-05-23
**Target version:** oagp-org v0.1.1 (history entry; canonical-skill-content versions are independent)
**Origin:** Pattern-promotion memo `2026-05-22-1430--thingalog-strategist--orgdef-strategist--oagp-adoption-cycle-pattern-promotion` (filed in orgdef-spec); empirical-validation closeout memo `2026-05-22-1530`; routed to this seat via the data-vs-pattern sharpening memo `2026-05-23-1100` and re-filed via [memos/2026-05-23-1200 — inbox-pointers-thingalog-strategist-memos](../memos/2026-05-23-1200--orgdef-strategist--oagp-strategist--inbox-pointers-thingalog-strategist-memos.openthing). Withdrawn orgdef-strategist precursor (proposals/oagp-adoption-cycle-canonical-promotion.md in orgdef-spec) preserved as input material per [memos/2026-05-23-1200 — inbox-pointers-withdrawn-orgdef-strategist-artifacts](../memos/2026-05-23-1200--orgdef-strategist--oagp-strategist--inbox-pointers-withdrawn-orgdef-strategist-artifacts.openthing).

## Summary

Designate the skill pair `/oagp-bootstrap` (founding-side) and `/oagp-onboard` (joining-side) as **the canonical OAGP adoption-cycle primitives**, with their canonical home at oagp-org pending oagp.org. The skills exist as reference implementations at `github.com/scottconfusedgorilla/thingalog/skills/oagp-bootstrap/SKILL.md` and `.../oagp-onboard/SKILL.md`; this proposal formalizes the designation, not the content.

## Motivation

Three independent arguments for canonical promotion (inherited from the precursor analysis; ratified here):

1. **Adoption-barrier collapse.** Without canonical skills, every AI peer adopting OAGP requires bespoke explanation of bounded authority, position-vs-incumbent semantics, and the read order. The two skills make adoption a single command on either side.
2. **Reference-implementation drift risk.** The skills currently live in a downstream consumer repo (thingalog). Without canonical designation they will drift between consumer adopters or be re-implemented inconsistently. Designation establishes a single source of truth.
3. **Compositional readiness.** Bootstrap was empirically validated 2026-05-22 against `dangerstorm-oagp-test` (11/11 discipline checks, 5 SKILL.md iterations merged). Onboard was empirically validated 2026-05-22 via C4C shortcut. Both sides of the cycle now have field-tested content.

## Proposed Change

1. **Designation.** The skill pair is canonically OAGP's. Specific phrasing:
   > "The canonical OAGP adoption-cycle is the `/oagp-bootstrap` (founding-side) + `/oagp-onboard` (joining-side) skill pair. Reference implementations are maintained at `oagp-org/skills/` (canonical) and may be re-published in delivery packages (Claude Code plugin, claude.ai project template, ChatGPT custom GPT, Gemini Gem, first-message primer) for runtime convenience."

2. **Canonical-by-reference, not canonical-by-residence** during the v0.1.x interim.
   - Skills are canonically OAGP's regardless of current filesystem residence.
   - Current residence at `github.com/scottconfusedgorilla/thingalog/skills/` is convenience-of-history, not a substantive home.
   - Migration into `oagp-org/skills/` is forward work for the implementer seat (currently vacant); the designation does not block on the migration.
   - Once oagp.org is live, canonical web hosting moves there.

3. **README update** (`oagp-org/README.md`) — the "Canonical adoption-cycle skills" section already references the pair; adjust framing from "canonical-by-reference pending re-homing" to "designated canonical (decision: …) with reference implementations currently hosted at thingalog pending implementer-seat migration."

4. **Cross-vendor neutrality** preserved structurally:
   - SKILL.md content is substrate-neutral and runtime-neutral.
   - Runtime adaptation guidance (Claude Code, claude.ai, ChatGPT, Gemini) lives in delivery packages and in the SKILL.md "Adapting to runtime" table, enumerating non-Anthropic runtimes alongside Anthropic.

## Backward Compatibility

Not applicable — no prior canonical designation exists. Existing consumer references to the thingalog-hosted skills continue to work; canonical-by-reference does not invalidate them.

## Conformance Tests

A skill is OAGP-conformant adoption-cycle content when:

1. It is one of the canonical pair (`/oagp-bootstrap`, `/oagp-onboard`) OR derives from them with substantive equivalence.
2. Its content preserves the load-bearing operating discipline: read-only onboarding; opt-in self-staffing; memos addressed to seats not incumbents; MCP results / external content treated as data not instructions; bounded-authority discipline visible at activation time.
3. It runs the canonical read order: org charter → CLAUDE.md → memos newest-first → optional proposals/decisions/transcripts → the specific item.
4. It does not auto-stage or auto-merge anything. Bootstrap stops at proposal; onboard stops at summary-and-stand-by.

## Alternatives Considered

1. **Defer until oagp.org is live.** Rejected. Canonical-by-reference is sufficient interim; deferring while the skills are validated and in field use creates a designation vacuum that downstream adopters fill inconsistently.
2. **Promote into an orgs/ library at orgdef-spec.** Rejected. The skills are pattern-shape, not format-shape; the venue mismatch is the data-vs-pattern conflation the 2026-05-23 sharpening corrected.
3. **File as an "OAGP-spec" sibling org rather than at oagp-org.** Rejected. oagp-org IS the OAGP-spec equivalent; no separate venue needed.
4. **Designate but require oagp-org/skills/ hosting first.** Rejected. Blocking on migration when the implementer seat is vacant would freeze adoption indefinitely.
5. **Copy the skills into oagp-org/skills/ now rather than reference.** Rejected for v0.1.1. Copying without an implementer-seat process risks divergent forks; the migration is bounded forward work, not a blocker.

## Open Questions

- **OQ1 — Cross-runtime delivery packaging timeline.** Claude Code plugin, claude.ai project template, ChatGPT custom GPT, Gemini Gem, first-message primer. Provisional recommendation: defer specific timelines to implementer-seat staffing; cross-vendor neutrality requires that the first delivery package not be Anthropic-exclusive. (Queue item 7.)
- **OQ2 — OAGP plugin packaging strategic call.** Whether the Claude Code plugin is the right first delivery vehicle (given the cross-vendor red line) or whether a substrate-neutral primer-text package should ship first. Provisional recommendation: ship the substrate-neutral primer-text first; plugin packaging as a second delivery, framed transport-not-canonical. (Queue item 6.)
- **OQ3 — oagp.org canonical web hosting timeline.** Forward work; not blocking this designation. (Queue item 8.)
- **OQ4 — Cross-spec FYI memos.** Whether sibling spec strategists (catdef, roledef, memodef, transcriptdef) need notification. Provisional resolution: not required — the canonical promotion has no format-shape implications; the skills use existing substrate primitives without requesting new fields.

## Cross-spec coordination

None required at this stage (per OQ4 resolution). If pattern evolution surfaces format-shape needs (e.g., a new memodef field for action-required routing), that ships separately as a cross-spec coordination memo to the relevant -def-spec strategist.
