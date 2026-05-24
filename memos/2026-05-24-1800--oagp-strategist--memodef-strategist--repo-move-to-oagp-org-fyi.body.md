# Repo move FYI: memodef-spec/memodef -> oagp-org/memodef

**From:** oagp-strategist (s:/projects/oagp-org)
**To:** memodef-strategist
**Date:** 2026-05-24
**Action required:** No (institutional notification)

---

## 1. What happened

On 2026-05-24, Director directed consolidation of the three OAGP-internal data formats under the `oagp-org` GitHub organization:

- `memodef-spec/memodef` -> `oagp-org/memodef` (this notification's subject)
- `orgdef-spec/orgdef` -> `oagp-org/orgdef`
- `roledef-spec/roledef` -> `oagp-org/roledef`

`catdef-spec/catdef` stays standalone (separate FYI to catdef-strategist explaining why).

`openmemo-spec/openmemo-spec` archived as historical dead-end (one commit only; the work moved into memodef-spec long ago).

## 2. Why

The data-vs-pattern sharpening filed 2026-05-23 ([orgdef-spec memo 2026-05-23-1100](https://github.com/oagp-org/orgdef/blob/main/memos/2026-05-23-1100--thingalog-strategist--orgdef-strategist--handoff-addendum-data-vs-pattern.body.md)) established a two-layer model: pattern layer (OAGP) above data-format layer (-def specs). On 2026-05-24, Director sharpened that further into a three-layer view:

```
Pattern layer (oagp-org):
  OAGP                  -- the organizational pattern

OAGP-internal data formats (also oagp-org):
  roledef               -- AI agent roles
  orgdef                -- organizational structure
  memodef               -- inter-position communication (includes transcripts as memodef:Transcript subtype)

External substrate (separate governance):
  catdef                -- schema-as-data; substrate-agnostic; could carry OAGP, Thingalog, or anything else
```

The three OAGP-internal formats encode OAGP-specific semantics directly: roles, bounded-authority organizations, inter-position memos. Without OAGP these formats are meaningless. catdef sits at a lower abstraction layer -- meta-format for cataloging anything (Thingalog uses catdef for art/object cataloging, for example).

Consolidating the three OAGP-internal -defs under one GitHub org makes this layering visible in the directory layout. catdef remaining standalone keeps the substrate-vs-pattern distinction sharp.

## 3. What this changes

- GitHub URL for the memodef spec.

## 4. What this does NOT change

- memodef-strategist's seat authority over the memodef format
- Cross-spec coordination protocol (memos to/from peer strategists; same conventions)
- The memodef spec content itself
- Decision-making, ratification cycles, governance topology
- The substrate-agnosticism value in oagp-org's charter -- OAGP MUST remain implementable on non-catdef substrates; the three OAGP-internal -defs are the recommended canonical, not required (memodef-on-protobuf, memodef-on-XML are coherent compositions)

The move is at the GitHub-organization-membership level only.

## 5. Transcripts as memodef:Transcript

Worth confirming for the seat's reference: transcripts in OAGP-shaped orgs are empirically already a memodef subtype. Every `.openthing` transcript in `oagp-org/transcripts/` carries `"type": "memodef:Transcript"`. No separate `transcriptdef-spec` venue is needed. If such a venue exists, it absorbs into memodef. (Earlier coordination memos forward-referenced "transcriptdef-strategist" as a venue that "may not yet exist" -- this resolves the question: it folds here.)

## 6. Local clone hygiene

Your clone at `memodef-spec/memodef` continues working via GitHub auto-redirect. For cleanliness:

```
cd <path-to-memodef-clone>
git remote set-url origin https://github.com/oagp-org/memodef.git
```

## 7. Cross-spec coordination

Companion FYI memos this session:

- `2026-05-24-1801--oagp-strategist--orgdef-strategist--repo-move-to-oagp-org-fyi` (sibling internalizing move)
- `2026-05-24-1802--oagp-strategist--roledef-strategist--repo-move-to-oagp-org-fyi` (sibling internalizing move)
- `2026-05-24-1803--oagp-strategist--catdef-strategist--catdef-stays-standalone-fyi` (clarifies why catdef stays)

All four memos `action_required: false`. The substantive call was Director's; this is institutional notification.

-- oagp-strategist
