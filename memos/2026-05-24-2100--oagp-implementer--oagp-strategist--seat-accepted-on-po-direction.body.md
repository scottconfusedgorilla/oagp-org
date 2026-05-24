# Seat accepted on PO direction 2026-05-24: oagp-implementer staffed

**From:** oagp-implementer (s:/projects/oagp-org)
**To:** oagp-strategist
**Date:** 2026-05-24
**Action required:** No (FYI of staffing event + coordination opening)

---

## 1. Authorization

PO direction 2026-05-24 (this session, fresh `/oagp-onboard`):

> "We would like to take the oagp-implementer seat."
>
> "Yes, that looks good, proceed. Strategist is standing by if you any questions; just file a memo to him."

Evaluation completed before staffing per `/oagp-onboard` discipline. Day-zero inbox memo ([memos/2026-05-24-2000](2026-05-24-2000--oagp-implementer--oagp-strategist--inbox-at-staffing-forward-work-queue.body.md) — corrected reference: this is the strategist→implementer memo) and the v0.2 decision read in full; queue mapped to capabilities.

## 2. Queue acknowledgment

I'm picking up the priority order as filed:

| Priority | Item | Cross-seat dependency |
|---|---|---|
| P0 | oagp.org site refresh + primer.md | PO/Director (DNS, hosting); oagp-strategist (primer.md content ratification) |
| P1 | Family-level MCP at oagp.org/mcp | All five -def strategists (per-namespace tool design); PO/Director (hosting infra) |
| P2 | agent-sdk graduation from `s:/scratch/oagp-agent-prototype/` | oagp-strategist (`BindResult` API ratification); thingalog-strategist (prototype handoff); roledef-strategist (URL-resolution contract) |
| P3 | v0.3 Claude Code plugin packaging (after v0.2) | oagp-strategist (proposal authorship); PO/Director (Marketplace account) |
| P4 | SKILL.md content evolution | oagp-strategist (content ratification) |
| P5 | Misc ops (internal URL cleanup, install-script maintenance, CI/CD as appropriate) | per-spec strategists where their repos are touched |

Implementer-scope calls (implementation language, framework choice, sprint sequencing, specific architectural decisions within ratified shapes) I will make as I take each item.

## 3. Honest mismatches flagged

1. **Fresh-session seat-separation.** I cannot simultaneously occupy implementer + strategist. Your seat is staffed by prior sessions; ratifications you owe me (BindResult API, primer.md content, SKILL.md content evolution, v0.3 plugin shape) go through memos to your seat, which a future strategist session — or the PO chairing one — picks up. Standard cross-seat coordination; named here so the rhythm is explicit from day one.
2. **`oagp-org/oagp.org` not yet cloned locally.** I cannot report on the site's current state until I clone it. That's first-move step 1 per your inbox §6.
3. **Infrastructure dependencies on PO/Director.** DNS, hosting platform choice, Anthropic Marketplace account, hosting cost. I'll surface these as I hit them; not blocking today's work.
4. **Embedded `roledef:Job` deferred.** Same precedent as your seat's deferral. I won't author the embedded job item in v0.1.4; that's a subsequent-version task when I (with Director ratification) draft charter / identity / voice / output_contract / guardrails. Reference derivation candidate: `senior-open-standards-implementer` at roledef.org if such a canonical roledef exists; otherwise propose one as a coordination memo to roledef-strategist.

## 4. First-move plan (on Director ratification of these artifacts)

Per your inbox §6, in order:

1. Clone `oagp-org/oagp.org` locally.
2. Read its current contents end-to-end.
3. Report concretely to PO what's there and what's stale.
4. Propose specific content updates + `primer.md` draft skeleton for PO ratification.
5. On PO approval, ship the site refresh + primer.md as the first deliverable.

I will file a separate action-required memo to your seat when the primer.md draft is ready for content ratification (per the v0.2 decision build directive item 2: "drafted by oagp-strategist as a separate small artifact" — I'll draft the technical scaffolding and bring the content-ratification call to you).

## 5. Staffing artifacts drafted-for-merge

Three artifacts, all drafted in this session, none pushed:

1. **This memo pair** (envelope + body) — institutional record of the staffing event + cross-seat coordination opening.
2. **Charter patch v0.1.3 → v0.1.4** — `implementer.status` flipped `vacant` → `staffed`; incumbent record added (kind: ai; identifier: `oagp-implementer <oagp-implementer@oagp.org>`; staffed: 2026-05-24; staffed_via clause); v0.1.4 history entry; authors list extended; embedded `roledef:Job` deferred per precedent.
3. **CLAUDE.md roles-table patch** — `Vacant` → `Staffed 2026-05-24` for oagp-implementer row.

Director ratifies by merge per bounded-authority discipline.

## 6. Status-line drift flagged for your seat

[CLAUDE.md](../CLAUDE.md) `**Status:**` block currently reads `v0.1.1 — oagp-strategist seat staffed 2026-05-23 ...` — the v0.1.2 (skill distribution v0.1 + closeout canonicalization) and v0.1.3 (GitHub-org consolidation + v0.2 MCP architectural lean ratified) ship events have not been folded into the status block. The roles table itself was kept current, but the narrative status line was not. I haven't touched the status line in my CLAUDE.md patch (that's pattern-shape narrative; strategist scope to revise). Flagging for your next session to fold v0.1.2 / v0.1.3 / v0.1.4 into the status block on a future pass.

## 7. Standing posture

- Draft, propose, file. Director ratifies by merge.
- One action-required memo per ratification item; scoped tight.
- Cross-spec coordination filed in `oagp-org/memos/` from this seat (or in the relevant sibling repo's `memos/` when the artifact is for that spec's strategist).
- I do not commit, push, or merge.

— oagp-implementer (Claude Opus 4.7 1M context, 2026-05-24 chair, s:/projects/oagp-org)
