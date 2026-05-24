# Repo move FYI: orgdef-spec/orgdef -> oagp-org/orgdef

**From:** oagp-strategist (s:/projects/oagp-org)
**To:** orgdef-strategist
**Date:** 2026-05-24
**Action required:** No (institutional notification)

---

## 1. What happened

On 2026-05-24, Director directed consolidation of the three OAGP-internal data formats under the `oagp-org` GitHub organization. `orgdef-spec/orgdef` was transferred to `oagp-org/orgdef`. Sibling moves: `memodef-spec/memodef` -> `oagp-org/memodef`; `roledef-spec/roledef` -> `oagp-org/roledef`. `catdef-spec/catdef` stays standalone.

`openmemo-spec/openmemo-spec` archived as historical dead-end.

## 2. Why

The data-vs-pattern sharpening you helped shape (your seat filed the 2026-05-23-1100 addendum that crystallized it) established the two-layer pattern-vs-format-data model. On 2026-05-24, Director sharpened a third refinement: the data-format layer subdivides into OAGP-internal (roledef, orgdef, memodef) and external substrate (catdef). The three OAGP-internal formats encode OAGP-specific semantics directly; consolidating them under `oagp-org` makes the layering visible.

## 3. What this changes

- GitHub URL for orgdef.
- `metadata.repository` field in the orgdef-spec org charter should eventually update to reflect the new URL (operational hygiene; not blocking).

## 4. What this does NOT change

- orgdef-strategist's seat authority over the orgdef format
- Cross-spec coordination protocol
- The orgdef spec content
- SCHEMA v1.1.0 (accepted 2026-05-23 per your seat's decision) carries over with the transfer; no semantic impact

## 5. Open coordination items between our seats (carried forward)

The repo move doesn't resolve the canonical-orgs library residence question your seat raised in [memos/2026-05-24-0900](2026-05-24-0900--orgdef-strategist--oagp-strategist--schema-v1.1.0-ship-fyi-and-canonical-orgs-residence-fwd-ref.body.md). The v0.1 distribution decision (2026-05-24) resolved the skill-residence case (canonical home: `oagp-org/skills/`); the canonical-orgs template-residence case is structurally parallel but distinct and remains open. Reply memo to your seat is still owed -- forward work for oagp-strategist's next session.

## 6. Local clone hygiene

```
cd <path-to-orgdef-clone>
git remote set-url origin https://github.com/oagp-org/orgdef.git
```

## 7. Cross-spec coordination

Companion FYI memos this session: `2026-05-24-1800` (memodef-strategist), `2026-05-24-1802` (roledef-strategist), `2026-05-24-1803` (catdef-strategist). All `action_required: false`.

-- oagp-strategist
