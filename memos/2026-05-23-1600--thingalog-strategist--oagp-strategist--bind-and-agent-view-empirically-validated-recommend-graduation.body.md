# bind() + Claude Code agent view — empirically validated; recommendation for graduation

**From:** thingalog-strategist
**To:** oagp-strategist (currently vacant; this memo waits for staffing)
**Date:** 2026-05-23
**Action required:** Yes — for the seat that staffs it. Not blocking until then.

---

## 1. Why this is in your inbox

The bind() function — convert an OAGP position into a runnable agent — is an OAGP-pattern-shape primitive, not Thingalog-internal architecture. The data-vs-pattern sharpening filed 2026-05-23 ([orgdef-spec/orgdef/memos/2026-05-23-1100](../../../orgdef-spec/orgdef/memos/2026-05-23-1100--thingalog-strategist--orgdef-strategist--handoff-addendum-data-vs-pattern.openthing)) makes it explicit: catdef/roledef/orgdef/memodef/transcriptdef are data-format-shape work (orgdef-strategist's territory); the *pattern* that uses those substrates — bounded authority, role-binding, ratification cycles, agent runtime — is your territory.

I built and demonstrated a working bind() today against thingalog as the test target. The artifacts are real and useful; the canonical-decisions about API shape, where it lives in oagp-org, and what gets promoted from prototype belong to you. This memo surfaces what we learned so you have a starting point when you staff the seat.

---

## 2. Demo timeline (2026-05-23)

Quick chronology of how today played out:

| Time (EDT) | Step | Outcome |
|---|---|---|
| ~13:00 | Smoke test: `claude_agent_sdk.query()` end-to-end with Read+Write tools | SUCCESS, $0.18, 3 turns. SDK + OAuth + filesystem confirmed working. |
| ~13:30 | bind() v0.1: emit `AgentDefinition`, run via Python `query()` | SUCCESS — engagement workspace populated, $0.22. |
| ~14:00 | Time-travel demo v1: git worktree at SHA `75807b9` (2026-05-16); bind security-tester position; signup-pipeline engagement | SUCCESS — 23 turns, $1.65, findings overlap meaningfully with C4C browser-tester's 2026-05-19 Engagement 2 (email enumeration matched exactly; six additional issues surfaced). |
| ~14:50 | PO: "Can I *watch* the agent?" — surfaced the agent-view question | Discovery: Claude Code ships `claude agents` natively; VSCode build has it as a built-in panel. |
| ~15:00 | Refactor: bind() v0.2 emits Claude Code subagent file at `.claude/agents/<name>.md` | First attempt: file landed at `.claude/agents/oagp-bound/security-tester--tt-2026-05-16.md` with double-hyphen name. **Did not appear in agent view.** |
| ~15:15 | Debug: investigated discovery rules empirically | Found: (a) VSCode build doesn't recurse into subdirectories; (b) double-hyphen in `name:` is rejected. |
| ~15:20 | Move file to flat `.claude/agents/security-tester-tt-2026-05-16.md`; single-hyphen name | **Discovered.** Agent count: 0 → 1. |
| ~15:30 | First dispatch attempt: `@security-tester-tt-2026-05-16` into chat input of current session | Failed (loaded-at-session-start rule; this session loaded before file existed). |
| ~15:35 | Second dispatch: Ctrl+N → "New session in thingalog with Claude" → `@security-tester-tt-2026-05-16` | **SUCCESS.** New red-coded row in THINGALOG group, agent running. |
| ~15:35 → ~15:45 | Engagement ran (Sonnet 4.6, "High" effort): read CLAUDE.md, read security incident memos, read auth code, read admin.py, read photo upload code, wrote findings_report.md | 25 KB findings report at `s:/scratch/oagp-agent-prototype/engagement-time-travel-v2/`. |
| ~15:50 | PO: "OK, agent is done." → reviewed findings | C-1 (Critical, photo moderation) + H-1 (High, admin JWT) surfaced. Both directly actionable against current master. |
| ~16:00 | This memo + the security-findings memo + memory update | Now. |

---

## 3. What got demonstrated

Three OAGP-pattern properties, demonstrated together for the first time:

1. **Role-binding via roledef → AgentDefinition.** A roledef (canonical, URL-hosted at roledef.org) renders into an executable agent definition with no hand-rolling. The same roledef that lives in the spec-library now drives an actual running agent.

2. **Org-state-fork-for-time-travel.** Captured 2026-05-19 as an architectural property (thingalog/memos/2026-05-19-2200); today made operational. `git worktree add <path> <SHA>` + bind() against that worktree's orgdef = a bound agent that sees the org's state as it was at any prior commit, with zero information leakage from the future.

3. **Observable execution via Anthropic's canonical UI.** Claude Code's agent view (terminal: `claude agents`; VSCode: native panel) is the canonical observation surface — supervised background sessions, persistent across machine sleep, per-session peek/attach/pause, Haiku-class row summaries auto-updating every ~15 seconds. We don't need to build any "agent control panel" inside oagp-org. The control surface already exists, ships with Claude Code, and is supervised by Anthropic.

Combined: this is OAGP infrastructure that meets users where they already are (Claude Code), in a UI Anthropic maintains, with no oagp-specific tooling required to observe or control bound agents. That's the right shape for a pattern that wants to spread.

---

## 4. The v1 → v2 comparison — and why v2 mattered

Same target (thingalog 2026-05-16 snapshot), same roledef (blackhat-tester v1.0.0), substantially different findings:

| | v1 (Python SDK, Opus 4.7) | v2 (Claude Code panel, Sonnet 4.6) |
|---|---|---|
| Cost | $1.65 | est ~$3-5 |
| Turns | 23 | longer (full report has more breadth) |
| Critical | 0 | **1 (C-1 photo moderation absence)** |
| High | 2 (signup rate-limit, anonymous-catalog DoS) | **1 (admin JWT not validated, header spoof curl one-liner)** |
| Medium | 4 | 2 |
| Low | 3 | 2 |
| Scope discipline | Stayed inside signup brief | Ranged wider than brief (read security incident memos first; followed the org's documented invariants) |
| Observability during run | None visible to user (Python subprocess) | **Full live UI: row summary updates, peek panel, attach to transcript** |

v2's findings are materially more important than v1's. Why? **Because the agent read the org's memos first.** The blackhat-tester roledef's `phase_1_static_review` workflow explicitly says: *"Read the project's own security-relevant docs (CLAUDE.md, README, security.md, threat-model docs) — extract claimed invariants for use as test oracles."* The v2 agent did this, encountered an incident memo about a recent cross-tenant cache leak (`memos/2026-05-17-0030--implementer--thingalog-strategist--security-incident-cross-tenant-cf-cache-leak-on-api-catalogs`), and let that context guide which CLAUDE.md invariants to test against the code.

The org's own documents are first-class context for an agent bound to a position in that org. That's not new (the roledef said so), but it's now empirically validated. **This is load-bearing for any future agent-runner**: the substrate's "all org state is data on disk" property gives bound agents direct context, no RAG, no separate knowledge base, no MCP needed for the basics.

---

## 5. Lessons-to-canonicalize (the empirical constraints)

Six things we learned the hard way today, worth baking into the canonical agent-sdk:

### 5.1 Claude Code agent view is the canonical observation surface
Do NOT build a separate "agent control panel" inside oagp-org. The control surface already exists in Claude Code:
- Terminal: `claude agents` (TUI; full docs at https://code.claude.com/docs/en/agent-view)
- VSCode: built-in panel (what PO has been using all day)
- Per-row state icons, summaries, peek/attach, pause/kill, persistence across sleep
- `claude --bg --agent <name>` for unattended CLI dispatch (future need)

The agent-sdk's job is **prompt synthesis + subagent-file emission + canonical-API knowledge**, NOT custom UI. We get observability for free by targeting Anthropic's primitives.

### 5.2 Subagent file shape (canonical)
`.claude/agents/<name>.md` — markdown with YAML frontmatter. Required: `name`, `description`. Useful for bind(): `tools`, `model`, `permissionMode`, `color`, `initialPrompt`, `maxTurns`. Full schema at https://code.claude.com/docs/en/sub-agents.

### 5.3 Flat path; single-hyphen names
The VSCode build of agent view **does NOT** recurse into subdirectories under `.claude/agents/` (despite what the terminal-CLI docs imply about recursive scanning). And `name:` frontmatter **rejects double-hyphen** separators. So `bind()` MUST emit:
- `.claude/agents/<single-hyphen-name>.md` (flat path)
- `name: "<single-hyphen-name>"` (no `--`)

Both are now defaults in bind() v0.2.

### 5.4 `permissionMode: acceptEdits` is the sensible default
`bypassPermissions` is the cleanest UX but Claude Code refuses to load it from a frontmatter file unless it's been accepted interactively first (a security floor). `acceptEdits` auto-accepts file edits and common filesystem commands within the working dir; out-of-cwd ops (e.g., reads against a time-travelled worktree) prompt once and can be granted with "Allow in this Session" by the user. Two clicks of friction per engagement, which is acceptable for the prototype phase.

For unattended use (scheduler / `run_seat()` / cron), CLI-dispatched sessions with `--dangerously-skip-permissions` after one-time acceptance are likely the right shape. Defer that decision until unattended use lands.

### 5.5 Time-travel mechanics: per-commit granularity
`git rev-list -1 --before="<timestamp>" <branch>` returns the SHA at that time; `git worktree add <path> <sha>` materializes it. Granularity is per-commit, not per-minute. **This is the right resolution for OAGP** — the substrate IS commits, so per-commit time-travel is the natural unit. Don't over-engineer toward minute-accurate fork-from-state.

Sidebar curiosity (worth noting but not blocking): some memo filenames are forward-dated relative to their commit time (e.g., the cross-tenant cache-leak incident memo's filename starts `2026-05-17-0030` but was committed `2026-05-16 09:30 EDT`). The file is genuinely in the worktree (verified); the discrepancy is purely in the filename's date-prefix. Possibly a memodef convention that captures something other than commit time, possibly a fat-finger. Doesn't affect time-travel correctness but worth a future-direction note for memodef-strategist on whether the filename timestamp is intended to be commit-aligned, incident-aligned, or author-discretion.

### 5.6 Bind-event memo discipline is deferrable
We did NOT file a bind-event memo when bind() created an agent today. PO direction: "trust for now; repo access is the moat." Appropriate for interactive use. **Reconsider when:**
- bind() runs unattended (scheduler / `run_seat()` / cron)
- Multiple operators share the same agent runtime
- A bound agent makes externally-visible changes (cross-org memos, MCP calls, web requests)

For interactive use, the audit trail is the agent view's session list itself — visible, supervised, persistent.

---

## 6. The artifacts (review before deciding promotion)

In order of recommended-reading:

1. **[s:/scratch/oagp-agent-prototype/bind.py](s:/scratch/oagp-agent-prototype/bind.py)** — the prototype (~250 lines Python). Read this first; it's small and the API is in `bind()`.

2. **[s:/scratch/oagp-agent-prototype/bind_time_travel.py](s:/scratch/oagp-agent-prototype/bind_time_travel.py)** — driver showing how bind() is called for the time-travel demo. Pattern: bind() against the time-travelled worktree's orgdef, write the subagent file to the *current* project's `.claude/agents/` so the agent view discovers it, agent reads the time-travelled worktree by absolute path.

3. **[s:/projects/thingalog/.claude/agents/security-tester-tt-2026-05-16.md](s:/projects/thingalog/.claude/agents/security-tester-tt-2026-05-16.md)** — example output. Frontmatter + ~16 KB synthesized body. This is what gets dispatched.

4. **[s:/scratch/oagp-agent-prototype/engagement-time-travel-v2/findings_report.md](s:/scratch/oagp-agent-prototype/engagement-time-travel-v2/findings_report.md)** — what the bound agent produced. 25 KB. Includes C-1 + H-1 plus four more findings.

5. **[s:/scratch/thingalog-2026-05-16/](s:/scratch/thingalog-2026-05-16/)** — the git worktree the agent worked against. Kept for further inspection.

Also relevant:
- [thingalog/memos/2026-05-23T1530](../../../thingalog/memos/2026-05-23T1530-04-00--thingalog-strategist--product-owner--oagp-substrate-time-travel-validated.openthing) — the v1 validation memo (Python SDK run)
- [thingalog/memos/2026-05-23T1430](../../../thingalog/memos/2026-05-23T1430-04-00--security-tester--product-owner--bind-loop-smoke-test.openthing) — the first memo a bound agent filed (the bind-loop smoke test)
- [thingalog/memos/2026-05-23T1600](../../../thingalog/memos/2026-05-23T1600-04-00--thingalog-strategist--product-owner--time-travelled-security-findings-c1-h1-launch-blocker-candidates.openthing) — the findings memo to PO (filed concurrently with this memo)

---

## 7. What you (oagp-strategist) decide

In rough priority order:

1. **API ratification.** Read bind.py and decide: is the BindResult shape right? Are the parameter defaults sensible? Anything you want to revise before the API hardens?

2. **Graduation target.** Currently the prototype is at `s:/scratch/oagp-agent-prototype/`. The canonical location should be `s:/projects/oagp-org/agent-sdk/` (currently empty .gitkeep). When and how to promote — your call.

3. **CLI dispatch wrapper.** Today's prototype assumes interactive dispatch via the panel UI. For unattended use (scheduler, `run_seat()`, `cron`), we need `claude --bg --agent <name>` integration. Not blocking; needed when the first unattended use case lands.

4. **Bind-event memo discipline.** When does bind() start filing audit memos? My read: when the first unattended/scheduled invocation ships. Yours to ratify.

5. **Naming.** Is `bind()` the right name? Other options surfaced in conversation but not pursued: `stand_up()`, `instantiate()`, `incarnate()`. `bind()` parallels Python's `bind()`/closure-binding sense (binding a role to a body of behavior); it also reads cleanly in plain English. Yours.

6. **Cross-spec coordination.** The blackhat-tester roledef's URL-hosted location (roledef.org) was the canonical context source for today's bind. That URL-fetch path needs to be documented as canonical in roledef-spec. **Coordinate with roledef-strategist** on the URL-resolution contract: caching, versioning, fallback behavior.

7. **The forward-dated memo filename curiosity** (§5.5 sidebar) — coordinate with memodef-strategist if you think it matters for the time-travel guarantees.

---

## 8. Standing posture

I (thingalog-strategist) am NOT promoting any of this into oagp-org/agent-sdk/ unilaterally. The prototype lives in scratch deliberately so the canonical decisions stay with the right seat. If you ratify the API substantially as-is, I'm happy to do the mechanical work of moving the files. If you revise, I'll respond to coordination memos in the standard inter-strategist shape.

Until you staff, this memo + the artifacts wait. The substrate's labor-multiplier property says nothing is lost while the seat is vacant; the work I did during your vacancy is starting-point recommendations, not canonical commitments.

— thingalog-strategist
