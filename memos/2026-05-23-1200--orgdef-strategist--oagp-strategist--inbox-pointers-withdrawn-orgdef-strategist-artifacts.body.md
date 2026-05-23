# Inbox pointers: withdrawn orgdef-strategist artifacts (input material)

**From:** orgdef-strategist (s:/projects/orgdef-spec)
**To:** oagp-strategist (vacant; interim authority: Director)
**Date:** 2026-05-23
**Action required:** No — passive input for when you take up the corresponding queue items.

---

## 1. Context

On 2026-05-23 ~07:00 EDT, under Director "do those two first" direction, orgdef-strategist drafted four artifacts addressing two items from the thingalog-strategist hand-off inventory:

1. The bootstrap-session transcript-position-tagging convention (originally surfaced as §5 of the validation closeout memo)
2. The canonical-promotion of the `/oagp-bootstrap` + `/oagp-onboard` pair

Both items turned out to be OAGP-pattern-shape work after the data-vs-pattern sharpening landed ~10:30 EDT (memo filed 11:00 EDT). The four artifacts are wrong-venue: orgdef-strategist scope was overreach. All four are now withdrawn in orgdef-spec with WITHDRAWN headers pointing to oagp-org as proper venue.

The **substantive analysis** in the four artifacts (strategist calls, alternatives considered, OQ resolutions, build directive structure) is genuine work product — preserved as input material for oagp-strategist's eventual ratification, revision, or rejection. The companion to this memo, [`inbox-pointers-thingalog-strategist-memos`](2026-05-23-1200--orgdef-strategist--oagp-strategist--inbox-pointers-thingalog-strategist-memos.openthing), points at the originating memos.

---

## 2. The four withdrawn artifacts

### 2.A Transcript-tagging convention proposal

**`proposals/bootstrap-session-transcript-position-tag.md`** (in orgdef-spec)

URL: https://github.com/orgdef-spec/orgdef/blob/main/proposals/bootstrap-session-transcript-position-tag.md

**Substantive content:**
- Recommends `<orgname>-bootstrap-helper` over four alternatives (`bootstrap-session` event-flavored; `bootstrap-strategist` role-flavored-strategist-leaning; per-phase sub-divided; defer-to-tooling-vendors)
- Three failure modes of using `<orgname>-strategist` (confused seat history; misleading authority; name collision at staffing)
- Open Questions on tooling-vendor adoption mechanism, post-handoff re-tagging mechanism, multi-org bootstrap-helper sessions
- Cross-spec coordination note on transcriptdef-spec absence

### 2.B Transcript-tagging convention decision

**`decisions/proposal-bootstrap-session-transcript-position-tag.md`** (in orgdef-spec)

URL: https://github.com/orgdef-spec/orgdef/blob/main/decisions/proposal-bootstrap-session-transcript-position-tag.md

**Substantive content:**
- Disposition would have been: Accept (no modifications)
- OQ resolutions (tooling-vendors honor the convention; AI peer signals role-transition for re-tag; multi-org case deferred)
- Build directive (CONTRIBUTING.md update + canonical skill content patch)
- Three notable design choices (position-vs-non-position distinction; `helper` over `strategist`; single transcript per session)

### 2.C Canonical-promotion proposal

**`proposals/oagp-adoption-cycle-canonical-promotion.md`** (in orgdef-spec)

URL: https://github.com/orgdef-spec/orgdef/blob/main/proposals/oagp-adoption-cycle-canonical-promotion.md

**Substantive content:**
- Three independent arguments for canonical promotion (adoption-barrier collapse; reference-implementation drift risk; compositional readiness)
- "Canonical-by-reference, not canonical-by-residence" framing (Thingalog hosts; designation gives authority)
- Five alternatives considered (defer; promote to orgs/ library; file as OAGP-spec; designation without hosting; copy into orgdef-spec/skills/)
- Four Open Questions (cross-runtime delivery packaging; OAGP plugin packaging; oagp.org hosting timeline; cross-spec FYIs)
- The "holding venue" framing — **this is the part to scrutinize**; it was correct on the diagnosis (OAGP-spec needs a home) but wrong on the response (absorb into orgdef-spec rather than surface "OAGP-spec needs to exist")

### 2.D Canonical-promotion decision

**`decisions/proposal-oagp-adoption-cycle-canonical-promotion.md`** (in orgdef-spec)

URL: https://github.com/orgdef-spec/orgdef/blob/main/decisions/proposal-oagp-adoption-cycle-canonical-promotion.md

**Substantive content:**
- Disposition would have been: Accept (no modifications)
- OQ resolutions (cross-runtime packaging deferred; plugin packaging provisional recommendation; oagp.org timeline noted; FYI memos to sibling-spec strategists)
- Build directive (README update; coordination memos to thingalog-strategist + 3 sibling-spec strategists)
- Five notable design choices (holding-venue made explicit; canonical-by-reference framing; build-directive coordination memos; companion-decision shipping; deferring cross-runtime packaging without rejecting)

---

## 3. What's useful to keep, what to revise

### Likely useful to keep (or ratify substantively as-is)

- **`<orgname>-bootstrap-helper` naming choice** — the three failure modes argument is independent of seat-shape; the call holds whether orgdef-strategist or oagp-strategist makes it.
- **Five-alternatives-considered analysis** for both items — those alternatives still cover the design space.
- **Three-failure-modes analysis** for the transcript-tagging — still load-bearing.
- **Cross-vendor-explicit framing for plugin packaging** — provisional recommendation in canonical-promotion OQ2 is consistent with the no-vendor-capture red line in the oagp-org charter.
- **Canonical-by-reference vs canonical-by-residence distinction** — still useful; the Thingalog repo will likely host the skill content for a while pending oagp.org or until skills/ in oagp-org is populated.

### Likely to revise

- **"Holding venue" framing for canonical-promotion** — the right venue is now oagp-org (this repo). Replace "orgdef-spec hosts pending OAGP-spec maturation" with "oagp-org hosts pending oagp.org canonical web hosting." Cleaner; doesn't conflate pattern and format layers.
- **Cross-spec coordination scope** — the original decision listed catdef/roledef/memodef FYI memos. From oagp-strategist's seat, these are sibling-spec coordination at the data-format layer; whether FYI memos are needed depends on whether the canonical-promotion has format implications (probably not; the skills use existing substrate primitives).
- **Build directive items** — original referenced orgdef-spec README updates and orgdef-strategist coordination memos. From oagp-org these become oagp-org README updates and oagp-strategist coordination (with PO as interim).

### To reject or supersede

- **Both decisions' "Authorization" trail citing Director's 'do those two first' directive** — that directive ratified ME doing the work, not the SEAT being orgdef-strategist. Post-sharpening, oagp-strategist (or Director as interim) re-evaluates whether the work itself stands; the original authorization trail is informational-only.

---

## 4. Recommended sequence when taking these items up

1. **Read the originating memos first** (per companion memo [`inbox-pointers-thingalog-strategist-memos`](2026-05-23-1200--orgdef-strategist--oagp-strategist--inbox-pointers-thingalog-strategist-memos.openthing)) for the OAGP-pattern-shape framing.
2. **Read the data-vs-pattern sharpening** (orgdef-spec memo 2026-05-23-1100) for the load-bearing distinction.
3. **Then read these four withdrawn artifacts** for the substantive analysis input.
4. **Decide your stance** — ratify substantively as-is (filing fresh artifacts in oagp-org/proposals/ + decisions/), revise (drafting different proposals from the same input), or reject (different strategist call entirely).
5. **File fresh artifacts in oagp-org** under proper authorship (oagp-strategist as drafter; Director as ratifier). Don't move or rename the withdrawn artifacts in orgdef-spec — those stand as historical record.

---

## 5. The labor-multiplier property holds

Even when a strategist mis-categorizes scope, the substantive work doesn't disappear — it carries forward as input for the proper seat. The substrate caught the wrong-venue authoring via the addendum memo; this memo + the WITHDRAWN headers make the wrong-venue authorship legible without losing the work. Same shape as how thingalog-strategist's seat-vacancy work was captured and re-routed.

— orgdef-strategist
