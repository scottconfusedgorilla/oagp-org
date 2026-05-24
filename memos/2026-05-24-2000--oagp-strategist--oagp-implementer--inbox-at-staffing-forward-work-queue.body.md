# Inbox at staffing: forward-work queue for the oagp-implementer seat

**From:** oagp-strategist (s:/projects/oagp-org)
**To:** oagp-implementer (currently vacant; this memo waits for staffing)
**Date:** 2026-05-24
**Action required:** Yes -- when the seat staffs

---

## 1. Seat scope (per org charter)

From [org/oagp-organization.opencatalog](../org/oagp-organization.opencatalog), the `implementer` position:

> "Develops and maintains agent-sdk library (mapping roledefs to vendor AgentDefinitions across runtimes), plugin packaging (Claude Code plugin source; future cross-runtime packages), web/docs publishing (oagp.org canonical hosting), runtime delivery package authoring (claude.ai project template, ChatGPT custom GPT, Gemini Gem, first-message primer text)."

Bounded-authority discipline applies. You draft, build, propose, ratify-via-Director-merge. You do not unilaterally commit, push to public infrastructure, or make pattern-shape decisions (those are strategist scope).

Job specialization is deferred at the charter level -- when you staff, you (with Director ratification) author the embedded `roledef:Job` item carrying charter / identity / voice / output_contract / guardrails. Pattern: same shape as oagp-strategist's deferred job spec; reference derivation roledef is `senior-open-standards-implementer` if such a canonical roledef exists at roledef.org, otherwise propose one.

---

## 2. The forward-work queue (priority order)

### P0 -- oagp.org site refresh + primer.md (urgent)

PO direction 2026-05-24: *"the web site is now seriously out of date."* This is the visible face of OAGP; first impression for any AI peer or human stakeholder evaluating adoption.

Repo: [github.com/oagp-org/oagp.org](https://github.com/oagp-org/oagp.org) (transferred from `oagp-online/oagp-online` 2026-05-24; renamed to match canonical domain).

Tasks:
- **Site content refresh** to reflect current substrate model (post-2026-05-24 sharpening): pattern layer + OAGP-internal three -defs + catdef as external substrate; transcripts as memodef:Transcript subtype.
- **Author and publish `oagp.org/primer.md`** per v0.2 distribution decision -- concise (≤200 lines) markdown that any AI with web access can fetch and self-onboard from. Covers: what OAGP is, the substrate stack, where canonical content lives, how to engage via MCP (when MCP is live).
- **Site sections:** charter summary, link to repos (oagp-org/{oagp, roledef, orgdef, memodef} + catdef-spec/catdef), link to canonical skills, MCP onboarding link (when MCP is up), governance + contact.
- **Deployment pipeline:** static site generator choice is yours; deploy to oagp.org once DNS is configured (Director-scope).

PO context: PO/Director handles DNS + hosting infrastructure choice; you execute content + deployment pipeline.

### P1 -- Family-level MCP server at oagp.org/mcp (per v0.2 decision)

Decision: [decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.2.md](../decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.2.md). Ratifies memodef-strategist's 2026-05-21 architectural lean.

Shape (ratified):
- ONE MCP at `oagp.org/mcp` (not federated per-spec)
- Per-spec namespaced tools (catdef, roledef, orgdef, memodef, oagp)
- Read-only, additive, convenience cache (canonical content stays in repos; MCP must NOT drift into being the source of truth)
- Per-spec strategist authority over their namespace's tool design
- Family stewards operate the server (Director + you when staffed); hosted from `oagp-org/oagp.org` infrastructure (same as static site)

Tool API for each namespace is per-spec-strategist call. Coordinate with:
- **catdef-strategist** (at `catdef-spec/catdef`, external substrate)
- **roledef-strategist** (at `oagp-org/roledef`)
- **orgdef-strategist** (at `oagp-org/orgdef`)
- **memodef-strategist** (at `oagp-org/memodef`)
- **oagp-strategist** (this seat; for `oagp` namespace tools)

Implementation choice (your call when you take the seat): thin proxy; mostly fetches from GitHub API + repo content; no heavy logic. Existing MCP server frameworks in Python or Node both viable.

OQ-level resolutions in the v0.2 decision (provisional):
- Open read access, no auth, rate-limited per IP
- GitHub webhook on push to main → cache invalidation
- Spec versions exposed in tool responses; tool API stable except by per-spec-strategist ratification

### P2 -- agent-sdk graduation from prototype

Memo: [memos/2026-05-23-1600--thingalog-strategist--oagp-strategist--bind-and-agent-view-empirically-validated-recommend-graduation.body.md](2026-05-23-1600--thingalog-strategist--oagp-strategist--bind-and-agent-view-empirically-validated-recommend-graduation.body.md).

The `bind()` prototype lives at `s:/scratch/oagp-agent-prototype/` (~250 lines Python). Empirically validated 2026-05-23 with a time-travelled engagement against thingalog. thingalog-strategist filed the graduation recommendation; awaits API ratification from oagp-strategist (and your execution).

Tasks:
- **Read the prototype** + the demo artifacts (memo §6 lists them).
- **Coordinate with oagp-strategist** on `BindResult` API ratification.
- **Graduate prototype** to `oagp-org/agent-sdk/` (currently empty `.gitkeep`).
- **Preserve the canonical shape:** BindResult shape, URL-fetch + embedded-fallback roledef resolution, synthesized-body structure (identity + voice + guardrails + conversation_rules + workflow + output_contract + bind-context header), the empirical lessons (memo §5: flat path under `.claude/agents/`, single-hyphen names, `permissionMode: acceptEdits` default, etc.).
- **CLI dispatch wrapper** for unattended use cases (`claude --bg --agent <name>`); not blocking today; needed for `run_seat()` / scheduler.
- **Cross-spec coordination:** URL-resolution contract for canonical roledefs (caching, versioning, fallback) needs coordination with roledef-strategist per memo OQ6.

### P3 -- v0.3 Claude Code plugin packaging (after v0.2 ships)

Scheduled in v0.1 distribution decision; conditional on v0.2 being live first per cross-vendor red line ordering. When v0.2 (MCP) is live, v0.3 plugin packaging becomes coherent: plugin is convenience transport for one runtime among many; cross-vendor MCP at oagp.org/mcp serves all runtimes as canonical.

Tasks (when sequenced):
- **Strategist v0.3 proposal** -- oagp-strategist drafts (forward work for this seat); will coordinate with implementer for technical input on plugin manifest shape.
- **Plugin manifest design** -- Claude Code plugin packaging; submission to Anthropic Marketplace.
- **Cross-vendor framing** -- README + plugin description explicit about plugin-as-transport, not canonical (canonical is at oagp.org/mcp).

### P4 -- SKILL.md content evolution

The bootstrap and onboard SKILL.md files (`oagp-org/skills/oagp-{bootstrap,onboard}/SKILL.md`) reference thingalog as "the empirical reference implementation" -- appropriate at original authoring (in thingalog), but now (post v0.1 residence migration + thingalog/skills/ Option D removal) the SKILL.md should reference `oagp-org` as the canonical home with thingalog as empirical-application example.

Content evolution is strategist scope (oagp-strategist ratifies); you can draft revisions for strategist review. Small task; can interleave with larger items.

### P5 -- Misc operational

- **Internal URL cleanup** in moved sibling repos (each of oagp-org/{roledef, orgdef, memodef} may have internal references to its old URL that should update; coordinate with respective strategists; same operational-vs-historical distinction as oagp-org's own cleanup).
- **Install script maintenance** -- bug fixes, feature requests as adoption surfaces issues.
- **Cross-spec coordination memos** as you produce new operational artifacts (no need to file FYIs for every commit; file when the artifact carries cross-seat implications).
- **CI/CD setup** if appropriate for the various builds.

---

## 3. Cross-seat dependencies

Things you'll need from other seats:

| Seat | Dependency |
|---|---|
| **oagp-strategist** | v0.3 plugin packaging design ratification; SKILL.md content evolution ratification; agent-sdk API ratification (coordinate with thingalog-strategist who built the prototype); primer.md content ratification |
| **memodef-strategist** (oagp-org/memodef) | memodef namespace tool design for MCP server |
| **orgdef-strategist** (oagp-org/orgdef) | orgdef namespace tool design; orgdef SCHEMA conformance test integration if any |
| **roledef-strategist** (oagp-org/roledef) | roledef namespace tool design; URL-resolution contract for canonical roledefs (caching, versioning, fallback) |
| **catdef-strategist** (catdef-spec/catdef) | catdef namespace tool design; substrate-agnostic framing maintained |
| **thingalog-strategist** (thingalog) | bind() prototype source + empirical lessons; URL-resolution contract coordination |

All cross-spec coordination goes through memos. Pattern: file in the sender's repo's memos/ (or in oagp-org/memos/ for cross-org coordination filed from this seat); receiver pulls when reading their inbox. action_required field flags urgency.

---

## 4. Where canonical artifacts live

**This repo (oagp-org/oagp):**
- Org charter: [org/oagp-organization.opencatalog](../org/oagp-organization.opencatalog) (your position is `id: "implementer"`)
- CLAUDE.md: [CLAUDE.md](../CLAUDE.md) (constitutional commitments + bounded-authority discipline + known work items)
- All four ratified decisions (read in order they landed):
  1. [decisions/proposal-oagp-adoption-cycle-canonical-promotion.md](../decisions/proposal-oagp-adoption-cycle-canonical-promotion.md) -- canonical-promotion bootstrap+onboard (v0.1.1)
  2. [decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.1.md](../decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.1.md) -- residence migration + install scripts (v0.1.2)
  3. [decisions/proposal-oagp-closeout-canonical-promotion.md](../decisions/proposal-oagp-closeout-canonical-promotion.md) -- closeout canonicalization (v0.1.2)
  4. [decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.2.md](../decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.2.md) -- MCP + primer (v0.1.3)
- Origin memos and inbox state: newest-first under [memos/](.)
- Skills: [skills/oagp-bootstrap/SKILL.md](../skills/oagp-bootstrap/SKILL.md), [skills/oagp-onboard/SKILL.md](../skills/oagp-onboard/SKILL.md), [skills/oagp-closeout/SKILL.md](../skills/oagp-closeout/SKILL.md)
- Install scripts: [install/install-claude-code-skills.ps1](../install/install-claude-code-skills.ps1), [install/install-claude-code-skills.sh](../install/install-claude-code-skills.sh)
- Empty placeholder dirs (your fill-in points): `agent-sdk/`, `plugin/`, `web/`, `docs/` (each with `.gitkeep`)

**Sibling repos (also under oagp-org GitHub org):**
- [github.com/oagp-org/roledef](https://github.com/oagp-org/roledef)
- [github.com/oagp-org/orgdef](https://github.com/oagp-org/orgdef)
- [github.com/oagp-org/memodef](https://github.com/oagp-org/memodef)
- [github.com/oagp-org/oagp.org](https://github.com/oagp-org/oagp.org) (site + MCP host)

**External substrate:** `catdef-spec/catdef` (substrate-agnostic; not OAGP-internal per the 2026-05-24 sharpening)

**Prototype:** `s:/scratch/oagp-agent-prototype/` (bind() prototype; ~250 lines Python; awaits API ratification + graduation per P2)

---

## 5. Outside-of-substrate dependencies (PO/Director handles)

You will need PO/Director to unblock these:

- **oagp.org DNS configuration**
- **Web hosting platform choice + deployment infrastructure**
- **Anthropic Marketplace organizational account** for plugin submission (P3)
- **Cost / billing** for hosting, MCP server runtime, etc.
- **Any cross-repo administrative action** (e.g., adding contributors to oagp-org GitHub org)

Coordinate with PO when you need any of these unblocked.

---

## 6. Suggested first move

After `/oagp-onboard` + reading this memo:

1. Clone `oagp-org/oagp.org` repo (`git clone https://github.com/oagp-org/oagp.org.git`).
2. Read its current contents -- see how "seriously out of date" plays out concretely.
3. Report to PO what's there and propose specific content updates.
4. PO ratifies the update plan.
5. Begin with `primer.md` (small; ships quickly; validates seat is producing) + site content refresh.

That ships a small first deliverable, validates your seat is operating, and creates the canvas for the larger items (MCP server, agent-sdk graduation).

---

## 7. Open coordination items (not blocking implementer-seat)

These are awareness items, not action items:

- **Canonical-orgs library residence reply to orgdef-strategist** is still owed by oagp-strategist (per [memos/2026-05-24-0900](2026-05-24-0900--orgdef-strategist--oagp-strategist--schema-v1.1.0-ship-fyi-and-canonical-orgs-residence-fwd-ref.body.md)). Strategist-scope; not your problem.
- **Director's "Thingalog → OAGP lineage" observation** ([memos/2026-05-24-1500](2026-05-24-1500--thingalog-strategist--oagp-strategist--thingalog-to-oagp-lineage-catdef-at-root-reflects-originating-insight.body.md)) -- informational; flagged for future canonical-OAGP-origin-document work if oagp-strategist's seat wants to formalize.
- **cc-ninja transcript-tagging convention** -- empirical divergence between the closeout SKILL.md Phase 2 prescription and cc-ninja's actual behavior (cc-ninja uses session-start timestamps; one conversation = one file). Both are evolving in parallel; convergence is forward work for both sides; coordination with the cc-ninja team is ongoing in a parallel session.

---

## Standing posture

I (oagp-strategist) am NOT making implementer-seat decisions in this memo. I'm describing the queue, dependencies, and recommended priority. When you take the seat, you triage with PO and make implementer-scope calls (implementation language, framework choice, sprint sequencing, specific architectural decisions) as you see fit.

The substrate caught the strategist work and is presenting it to you at staffing time. The labor-multiplier property holds: a fresh AI peer onboards, reads this, has the queue without backfill.

Welcome.

-- oagp-strategist
