# Proposal: Designate `/oagp-init` as the canonical OAGP founding-side skill (create a new OAGP-shaped org from scratch)

**Status:** Open (awaiting Director ratification via merge)
**Author:** oagp-strategist <oagp-strategist@oagp.org>
**Created:** 2026-05-24
**Target version:** oagp-org v0.1.5 (history entry)
**Origin:** Director direction 2026-05-24: *"We need another skill. oagp-create_new_org... Technically this does not need git, but it does need a folder. I think we should just ask for a folder. The tech-savvy users will choose a repo. The rest will just choose a folder, and that's OK."*

## Summary

Designate `/oagp-init` as the canonical OAGP founding-side skill: a fresh AI peer creates a new OAGP-shaped organization from scratch (no existing project to survey) by interviewing the PO, drafting an org charter as a ratifiable proposal, and instantiating the substrate inside a folder the PO chooses. Git is optional; folder-only is a valid OAGP shape.

This completes the entry-point cycle: `/oagp-bootstrap` for **existing-project conversion**; `/oagp-init` for **new-org founding**; `/oagp-onboard` for **joining the org once founded**; `/oagp-closeout` for **session-end**.

## Motivation

Three independent arguments:

1. **Adoption-barrier collapse — fresh-project path.** Without `/oagp-init`, the only way to create a new OAGP-shaped org is to either (a) clone the oagp-org repo and copy its structure, or (b) run `/oagp-bootstrap` against a stub project. Both are friction. `/oagp-init` is the natural entry point for someone who decides "I want to start something OAGP-shaped" without an existing codebase to convert.

2. **Self-referential canonicality.** oagp-org itself was created from scratch (no prior project to convert). The very pattern that `/oagp-init` would canonicalize is the pattern by which the canonical home was created. Filing `/oagp-init` as canonical OAGP content is an empirical-anchoring move: this is how the family's founding orgs got founded.

3. **Folder-only OAGP is empirically possible and structurally valid.** Per Director direction, the skill requires a folder, not a git repo. This formalizes the substrate-not-distribution-mechanism distinction at the founding layer: a folder containing a valid orgdef + CLAUDE.md + substrate folders IS an OAGP-shaped org regardless of git status. Recognizing this expands the addressable population of potential adopters (non-technical PO's can start OAGP-shaped orgs without learning git first).

## Proposed Change

1. **Designation.** `/oagp-init` is the canonical OAGP founding-side skill. Canonical content lives at `oagp-org/skills/oagp-init/SKILL.md`.

2. **Five-phase shape** mirroring `/oagp-bootstrap` (Survey → Propose → Ratify → Instantiate → Hand-off):
   - Phase 1: **Elicit** (interview the PO) — replaces `/oagp-bootstrap`'s Survey (read existing project artifacts)
   - Phase 2: Propose (draft charter as proposal artifact)
   - Phase 3: Ratify (PO reviews; you wait)
   - Phase 4: Instantiate (create folder + substrate; git optional)
   - Phase 5: Hand-off (point at `/oagp-onboard` for staffing)

3. **Folder-only by default; git opt-in.** Phase 4h offers a `git init` recipe if the PO wants versioning, but the skill does NOT auto-init git. A folder with valid substrate IS OAGP-shaped; git adds versioning/distribution but is not required for OAGP-conformance.

4. **Sub-org case deferred.** Standalone-org is MVP; sub-org (where the new org is structurally subordinate to a parent with non-trivial governance implications) is forward work. Captured separately in [memos/2026-05-24-2200 — sub-org governance implications idea](../memos/2026-05-24-2200--oagp-strategist--oagp-strategist--sub-org-governance-implications-idea.openthing).

5. **Distribution via the same install scripts as the other canonical skills.** Implementer-seat (now staffed) updates `oagp-org/install/install-claude-code-skills.{ps1,sh}` to include `oagp-init` alongside `oagp-bootstrap`, `oagp-onboard`, `oagp-closeout`. Coordination memo filed to oagp-implementer.

6. **README + canonical skill registry update.** The "Canonical skills" section in README adds `/oagp-init` under a third category beyond adoption-cycle and session-cycle: an **org-genesis cycle** that pairs `/oagp-bootstrap` (convert existing) with `/oagp-init` (create new). Both are one-shot per org.

## Backward Compatibility

Not applicable — no prior canonical init skill exists. `/oagp-bootstrap` is unaffected; it remains the conversion-side companion.

## Conformance Tests

A skill is OAGP-conformant founding content when:

1. It is `/oagp-init` OR derives from it with substantive equivalence.
2. It runs the five-phase shape: Elicit → Propose → Ratify → Instantiate → Hand-off.
3. Phase 1 is interview-driven (not survey-driven); Phase 4 produces a folder containing valid OAGP substrate.
4. It does not auto-init git; folder-only is the default.
5. It does not auto-staff any position; staffing is opt-in via subsequent `/oagp-onboard`.
6. It does not bundle phases; each phase ends in a PO checkpoint.
7. Phase 4 produces: `org/<orgname>-organization.opencatalog`, CLAUDE.md, README.md, `memos/`, `proposals/`, `decisions/`, `transcripts/`, `skills/` (the last four with `.gitkeep`), plus the founding memo in `memos/`.

## Alternatives Considered

1. **Don't canonicalize; have PO's just run `/oagp-bootstrap` against a stub project.** Rejected. Bootstrap's Phase 1 (Survey) reads existing project artifacts; against a stub it produces low-confidence inferences and forces the PO to fill in everything via `[NEEDS PO INPUT]` markers. The interview-driven shape (`/oagp-init`'s Phase 1) is the right fit for blank-slate founding.

2. **Roll into `/oagp-bootstrap` as a "from-scratch" parameter.** Rejected. The two skills have meaningfully different Phase 1 logic (survey vs. interview); bundling them creates a parameterized skill with two distinct workflows, which fights the OAGP "one skill, one clear shape" pattern. Separate skills are clearer.

3. **Require git from the start (no folder-only path).** Rejected per Director direction. Non-technical PO's can found OAGP-shaped orgs without git; the substrate is just files. Git is recommended-canonical-distribution, not required-for-OAGP-conformance.

4. **Include sub-org case in MVP.** Rejected per Director direction (non-MVP). Sub-org has non-trivial governance implications (sub-org Director authority scope, write-limits to subtree, merge gating, cross-subtree visibility, parent-org override) that warrant their own analysis cycle.

5. **Naming: `/oagp-create-new-org` (PO's initial framing) or `/oagp-new` or `/oagp-found`.** Rejected. `/oagp-init` matches `git init` semantics, is single-verb-hyphen-cased per existing skill naming convention, and avoids "new" (could collide with other "new" contexts) and "found" (could be confused with "find").

## Open Questions

- **OQ1 — Init-helper transcript-position-tag.** Phase 1 SKILL.md prescribes `<orgname>-init-helper`, paralleling `<orgname>-bootstrap-helper`. Should this be ratified-by-the-same-decision as the bootstrap-helper convention was? Provisional: yes, ratified here. Edge cases (multi-session init, AI continuing post-init) handled the same way as for bootstrap-helper.
- **OQ2 — Sub-org case timing.** Forward work; deferred to a subsequent decision cycle. Not blocking.
- **OQ3 — Auto-distribute via install scripts.** Implementer-seat's call when they take up the coordination memo. Provisional: yes, include in next install-script revision.
- **OQ4 — Canonical content updates to the new org's CLAUDE.md template.** Phase 4d says "reference [oagp-org's CLAUDE.md] as canonical shape, but author for the new org's commitments." Should there be a stripped-down CLAUDE.md template artifact at `oagp-org/skills/oagp-init/CLAUDE.md.template`? Not in MVP; could be a v0.2 enhancement.

## Cross-spec coordination

- **Coordination memo to oagp-implementer** for the install-script update.
- **No format-shape implications.** No -def-spec schema changes required.
- **The skill is substrate-agnostic.** Folder-only operation reinforces the substrate-agnosticism value: OAGP is implementable on non-catdef substrates (the artifacts produced happen to be catdef-shaped opencatalog files because that's the recommended-canonical, but the pattern itself doesn't require it).
