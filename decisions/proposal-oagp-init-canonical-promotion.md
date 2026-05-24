# Decision: Canonical promotion of `/oagp-init` (founding-side skill)

**Disposition:** Accept (recommended; awaiting Director ratification via merge)
**Origin:** [proposals/oagp-init-canonical-promotion.md](../proposals/oagp-init-canonical-promotion.md)
**Decided:** Drafted 2026-05-24 by oagp-strategist; Director ratifies on merge.
**Authorization:** Director direction 2026-05-24: *"We need another skill. oagp-create_new_org..."* + design refinements *"Technically this does not need git, but it does need a folder. I think we should just ask for a folder. The tech-savvy users will choose a repo. The rest will just choose a folder, and that's OK."* + *"sub-org case... I don't think that's MVP."*

## Rationale

Three arguments stand (per proposal §Motivation): adoption-barrier collapse for the fresh-project path; self-referential canonicality (oagp-org itself was created via the pattern `/oagp-init` would canonicalize); folder-only is empirically valid OAGP shape (reinforces substrate-agnosticism).

The skill mirrors `/oagp-bootstrap`'s five-phase discipline (propose-don't-impose; stop at each phase boundary; bounded-authority all the way through). The substantive difference is Phase 1 (Elicit, not Survey) — interview-driven rather than artifact-driven, because there's no existing project to read.

Director's "folder, not repo" framing is the key simplification. Git is recommended-canonical-distribution but not required-for-OAGP-conformance. The skill defaults to folder-only; Phase 4h offers an optional git-init recipe. This expands the addressable adopter population (non-technical PO's can found OAGP-shaped orgs without git literacy).

Sub-org case is deferred to a forward-reference idea memo per Director direction; non-MVP. Captured at [memos/2026-05-24-2200 — sub-org governance implications](../memos/2026-05-24-2200--oagp-strategist--oagp-strategist--sub-org-governance-implications-idea.openthing).

## Resolutions to Open Questions

- **OQ1 — `<orgname>-init-helper` transcript-position-tag.** Resolved: ratified by this decision; extends the bootstrap-helper convention canonically. Multi-session init and post-init re-tagging handled the same way as for bootstrap-helper per the closeout skill's Phase 2 table.
- **OQ2 — Sub-org case timing.** Resolved: deferred per Director direction. Sub-org governance implications captured separately as forward-reference idea memo.
- **OQ3 — Auto-distribute via install scripts.** Resolved: yes, include in next install-script revision; implementer-seat executes (coordination memo filed).
- **OQ4 — CLAUDE.md template artifact.** Resolved: not in MVP; potential v0.2 enhancement if PO use-in-anger shows authoring CLAUDE.md from scratch is consistently friction-prone.

## Build directive

On Director ratification (merge):

1. **Skill file** at `oagp-org/skills/oagp-init/SKILL.md` (drafted; awaiting merge).
2. **Coordination memo to oagp-implementer** for install-script update (drafted; awaiting merge as part of this bundle): [memos/2026-05-24-2201 — install-claude-code-skills update for /oagp-init](../memos/2026-05-24-2201--oagp-strategist--oagp-implementer--install-script-update-add-oagp-init.openthing).
3. **Sub-org governance idea memo** filed as forward-reference: [memos/2026-05-24-2200 — sub-org governance implications](../memos/2026-05-24-2200--oagp-strategist--oagp-strategist--sub-org-governance-implications-idea.openthing).
4. **README update** — "Canonical skills" section adds `/oagp-init` under an **org-genesis cycle** category (paired with `/oagp-bootstrap`) alongside the existing adoption-cycle (covered by /oagp-bootstrap alone) and session-cycle (covered by /oagp-onboard + /oagp-closeout) categories. Strategist drafts; implementer publishes via the site repo.
5. **CLAUDE.md known-work-items update** — adds the `/oagp-init` canonicalization as a resolved item; flags the sub-org idea memo as forward-reference.
6. **Charter v0.1.4 → v0.1.5 history entry.**

## Cross-spec coordination

- Coordination memo to oagp-implementer for install-script mechanical update.
- No format-shape implications; no -def-spec coordination required.

## Notable design choices

1. **Folder, not repo.** Per Director direction. Substrate-not-distribution-mechanism distinction at the founding layer; reinforces substrate-agnosticism value.
2. **Elicit Phase 1, not Survey.** The interview-driven shape is the right fit for blank-slate founding; bootstrap's Survey shape is right for existing projects. Two skills, two clear workflows.
3. **No auto-staff.** Position items default to `status: vacant`; staffing is opt-in via subsequent `/oagp-onboard` session. Same discipline as the rest of OAGP.
4. **Sub-org deferred.** Non-MVP; forward-reference idea memo captures the implications. Standalone-org is the canonical-MVP case.
5. **Init-helper transcript convention ratified here.** Extends the bootstrap-helper convention canonically; same governance shape.
6. **Bundled with sub-org idea memo + implementer coordination memo in a single merge.** Single Director ratification covers the canonical-promotion decision + the forward-reference idea filing + the implementer mechanical coordination.

## Items not incorporated

- **`/oagp-create-new-org` (PO's initial framing).** Rejected per proposal alternatives §5 — multi-word verb breaks the single-verb-hyphen-cased naming convention.
- **`/oagp-new` and `/oagp-found`.** Rejected per proposal alternatives §5 — less precise than `/oagp-init`.
- **Auto-init git.** Rejected per Director direction. Folder-only is the default; git is opt-in.
- **Sub-org case in MVP.** Rejected per Director direction; captured as forward-reference.
- **CLAUDE.md template artifact.** Deferred per OQ4 resolution; not in MVP.

## Workflow validation

Lands in v0.1.5 of the charter. v0.1.4 was implementer-seat staffing; v0.1.5 is `/oagp-init` canonical promotion + sub-org governance forward-reference. Single Director merge ratifies all artifacts in the bundle (SKILL.md, proposal, decision, two memos, charter+CLAUDE.md updates).

## Forward-reference resolution

- **Sub-org governance** flagged as forward work via [memos/2026-05-24-2200](../memos/2026-05-24-2200--oagp-strategist--oagp-strategist--sub-org-governance-implications-idea.openthing). Not blocking.
- **CLAUDE.md template artifact** flagged as potential v0.2 enhancement; not blocking.
- **Install-script update** delegated to oagp-implementer via coordination memo; not blocking the SKILL.md being canonical.

## References

- Proposal: [proposals/oagp-init-canonical-promotion.md](../proposals/oagp-init-canonical-promotion.md)
- Companion skills (for context): [decisions/proposal-oagp-adoption-cycle-canonical-promotion.md](proposal-oagp-adoption-cycle-canonical-promotion.md), [decisions/proposal-oagp-closeout-canonical-promotion.md](proposal-oagp-closeout-canonical-promotion.md)
- Build artifacts:
  - [skills/oagp-init/SKILL.md](../skills/oagp-init/SKILL.md)
  - [memos/2026-05-24-2200 — sub-org governance implications](../memos/2026-05-24-2200--oagp-strategist--oagp-strategist--sub-org-governance-implications-idea.openthing)
  - [memos/2026-05-24-2201 — install-script update coordination](../memos/2026-05-24-2201--oagp-strategist--oagp-implementer--install-script-update-add-oagp-init.openthing)
- Org charter: [org/oagp-organization.opencatalog](../org/oagp-organization.opencatalog) (v0.1.5 history entry)
