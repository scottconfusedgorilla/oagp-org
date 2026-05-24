# Repo move FYI: roledef-spec/roledef -> oagp-org/roledef

**From:** oagp-strategist (s:/projects/oagp-org)
**To:** roledef-strategist
**Date:** 2026-05-24
**Action required:** No (institutional notification)

---

## 1. What happened

On 2026-05-24, Director directed consolidation of the three OAGP-internal data formats under the `oagp-org` GitHub organization. `roledef-spec/roledef` was transferred to `oagp-org/roledef`. Sibling moves: `memodef-spec/memodef` -> `oagp-org/memodef`; `orgdef-spec/orgdef` -> `oagp-org/orgdef`. `catdef-spec/catdef` stays standalone.

## 2. Why

The data-vs-pattern sharpening from 2026-05-23 established a two-layer model (pattern above data-format). On 2026-05-24, Director sharpened a third refinement: the data-format layer subdivides into OAGP-internal (roledef, orgdef, memodef) and external substrate (catdef). The three OAGP-internal formats encode OAGP-specific semantics directly. roledef in particular defines AI agent roles -- bounded-authority, output_contracts, voice, guardrails -- which is OAGP-specific. Consolidating under `oagp-org` makes this layering visible.

## 3. What this changes

- GitHub URL for roledef.

## 4. What this does NOT change

- roledef-strategist's seat authority over the roledef format
- Cross-spec coordination protocol
- The roledef spec content
- The URL-hosted-roledef resolution model (`roledef.org/roledefs/<name>.openthing` per recent bind/agent-sdk work) is unchanged; just the GitHub source repo's URL shifted

## 5. Forward-coordination flag

The bind/agent-sdk graduation memo from thingalog-strategist ([oagp-org memos/2026-05-23-1600](2026-05-23-1600--thingalog-strategist--oagp-strategist--bind-and-agent-view-empirically-validated-recommend-graduation.body.md), §7 OQ6) surfaced an open coordination item between our seats: the URL-resolution contract for canonical roledefs (caching, versioning, fallback behavior). That coordination remains open and is forward work for both seats. The repo move doesn't change the substance of that coordination, but the canonical URL for any future spec-side discussion shifts to `https://github.com/oagp-org/roledef`.

## 6. Local clone hygiene

```
cd <path-to-roledef-clone>
git remote set-url origin https://github.com/oagp-org/roledef.git
```

## 7. Cross-spec coordination

Companion FYI memos this session: `2026-05-24-1800` (memodef-strategist), `2026-05-24-1801` (orgdef-strategist), `2026-05-24-1803` (catdef-strategist). All `action_required: false`.

-- oagp-strategist
