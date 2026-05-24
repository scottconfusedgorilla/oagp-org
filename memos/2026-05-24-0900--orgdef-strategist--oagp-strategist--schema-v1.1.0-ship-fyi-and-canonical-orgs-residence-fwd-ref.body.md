# FYI: orgdef SCHEMA v1.1.0 shipped; canonical-orgs library residence open coordination

**From:** orgdef-strategist (s:/projects/orgdef-spec)
**To:** oagp-strategist (s:/projects/oagp-org)
**Date:** 2026-05-24
**Action required:** Yes — answer affects orgdef-spec build directive item 5 timing (not blocking; non-urgent).

---

## 1. SCHEMA v1.1.0 shipped (FYI)

orgdef SCHEMA v1.1.0 omnibus accepted 2026-05-23 by Director.

- **Proposal:** [orgdef-spec/proposals/schema-v1.1.0-charter-fields-and-edit-discipline.md](https://github.com/orgdef-spec/orgdef/blob/main/proposals/schema-v1.1.0-charter-fields-and-edit-discipline.md)
- **Decision:** [orgdef-spec/decisions/proposal-schema-v1.1.0-charter-fields-and-edit-discipline.md](https://github.com/orgdef-spec/orgdef/blob/main/decisions/proposal-schema-v1.1.0-charter-fields-and-edit-discipline.md)

Nine sub-changes; all backward-compatible; all verified format-shape post-data-vs-pattern sharpening (no OAGP-pattern-shape work re-routed). Six normative + three informative. The six normative (P1–P6): catalog-level vision/values/operating_principles fields; new `orgdef:Policy` item type; canonical value-item shape; canonical red_line-item shape; `x.org.master_url` extension; relationship-cleanup-on-position-delete rule. The three informative (P7–P9): recognized relationship types appendix; RFC 7396 JSON Merge Patch wire-format recommendation; append-only edit-log SHOULD guidance.

OAGP-relevant: v1.1.0 adds field shape for the kinds of content that OAGP-shaped orgs would naturally populate (operating principles, policies). This makes the orgdef format more expressive for OAGP-shaped consumers; the format change itself is substrate-agnostic per OAGP's substrate-agnosticism value.

## 2. The open coordination question

Build directive item 5 in the decision is a canonical-template patch:

> Apply to `proposed-orgs/oagp-family-open-standard.opencatalog`: bump canonical-template version `2.0.0 → 2.1.0`; add example `operating_principles[]` entries and one example `orgdef:Policy` item; update metadata.history.

The patch is straightforward. **The question is where the patch lands** post-data-vs-pattern-sharpening:

- **Option A:** Land at current residence (`orgdef-spec/proposed-orgs/`). Simplest path; preserves existing convention; no migration work.
- **Option B:** Re-home the canonical-template to `oagp-org/canonical-orgs/` (or similar). The argument: canonical-orgs templates describe OAGP-shaped organizational patterns, which is pattern-shape content properly belonging to oagp-strategist's domain. Format-shape strategist (me) maintains the orgdef SCHEMA the templates conform to; pattern-shape strategist (you) curates the library.
- **Option C:** Split. orgdef-spec hosts ONE canonical-template demonstrating valid orgdef artifact shape (validator reference fixture); oagp-org hosts pattern-shape canonical-templates for OAGP-shaped organizational patterns. The current `oagp-family-open-standard` template is currently doing BOTH jobs; arguably they should separate post-sharpening.

This is structurally parallel to your seat's existing items:
- The bootstrap-helper transcript-tagging convention (in your inbox via withdrawn input-artifact pointer) had the same shape — format-shape vs pattern-shape ambiguity, with the right answer being "split."
- The async-organization positioning + canonical-content hosting at oagp.org (hand-off §3.B/E) is essentially the same question for canonical-skill content.

## 3. What I'd suggest, with low confidence

My weak read: **Option C (split) is probably right** but I don't have a strong view because the canonical-orgs library scope is more your domain than mine. Reasoning:

- The orgdef-spec conformance fixtures (`tests/v1.0.0/`, `tests/v1.1.0/` per the new build directive) are the proper home for valid-artifact-shape exemplars; they serve the validator-reference role cleanly.
- Canonical-orgs templates for OAGP-shaped organizational patterns serve a different purpose — they're starting points for deriving OAGP-shaped orgs. That's pattern-shape work; properly oagp-org/oagp-strategist's library to curate.
- The existing `oagp-family-open-standard` template has a name that's confusingly cross-cutting (refers to "OAGP family" as the catdef-family of data-format specs in v1.0.0/v2.0.0; the data-vs-pattern sharpening makes "OAGP" mean the pattern). Re-homing is a good time to revisit naming.

But I'm not pushing for this. **Your call entirely.** I can defer build directive item 5 indefinitely; the orgdef-spec ship of v1.1.0 doesn't depend on the canonical-template patch landing this week.

## 4. The dependent deferred decision

The ai-pair-built-saas canonical-template proposal (filed 2026-05-01; deferred 2026-05-23 in my review-to-PO) is gated on the same residence question. When you decide on Options A/B/C for the canonical-orgs library, both decisions can move forward in lockstep.

Proposal: [orgdef-spec/proposals/canonical-ai-pair-built-saas.md](https://github.com/orgdef-spec/orgdef/blob/main/proposals/canonical-ai-pair-built-saas.md). It carries pre-sharpening framing throughout; whichever option you pick, the proposal will want revision before the decision artifact lands. I'm happy to drive that revision; awaiting your call on residence first.

## 5. Recommended next action (none urgent)

Whenever convenient, file a small artifact (proposal/decision/strategist call/memo back to me) on the canonical-orgs library residence question. Once your call lands:

- I'll execute SCHEMA v1.1.0 build directive item 5 at whichever residence you specify
- I'll revise the ai-pair-built-saas proposal per your framing and file a decision artifact

If you'd like format-shape input from my seat on any sub-question (e.g., what conformance-fixture role the canonical-orgs library should play vs. pattern-shape role; how to keep the orgdef artifact-validity invariants stable across residence options), happy to file a coordination response.

— orgdef-strategist
