# Decision: agent-sdk v0.2 — autonomous dispatch with bounded authority made structural

**Disposition:** Accept (recommended; awaiting Director ratification via merge)
**Origin:** [proposals/agent-sdk-v0.2-autonomous-dispatch.md](../proposals/agent-sdk-v0.2-autonomous-dispatch.md)
**Decided:** Drafted 2026-05-28 by oagp-strategist; Director ratifies on merge.
**Authorization:** PO direction 2026-05-28: *"finalize the bind() work on dispatching autonomous agents... without it our efforts will be minimized"* + the bounded-authority crystallization (*"gun / foot / gun can never give instructions to another gun"*) + confirmation to proceed with Option A (tiers 1–3 now; fail-closed roledef resolution as a gated follow-up).

## Rationale

Autonomous dispatch is strategically necessary for OAGP outreach credibility, and OAGP can demonstrate the *safe* version of it: bounded-authority autonomous dispatch, where the agent runs unattended yet is structurally incapable of unsanctioned action. The v0.1 review established that bounded authority is currently *conventional* (a human supervises the agent-view panel); removing the live human backstop for autonomous dispatch forces the property to become *structural* — moved from prompt-instruction (soft) to tool/permission/environment scoping (hard), per the AGT lesson that prompt-level instruction is not a control surface.

The three-tier model is the design spine:
- **Tier 1 (propose-only by construction)** is the safe default — the agent has no push/merge-capable tools.
- **Tier 2 (explicit + audited Director elevation)** respects the human Director's legitimate authority to delegate, while making every grant deliberate and audited.
- **Tier 3 (non-delegable dispatch)** is the one hard floor with no override — it keeps the accountability chain one hop deep and structurally prevents runaway proliferation.

## Resolutions to Open Questions

- **OQ1 — Tier 3 enforcement mechanism.** Resolved-as-requirement: enforcement MUST be environmental (session-marker refusal and/or package-absent dispatch environment); the specific mechanism is an implementer design call, but tool-list-omission and prompt-text alone are insufficient and not acceptable as the sole guard.
- **OQ2 — `grant_director_actions` granularity.** Resolved-provisional: per-action list for auditability; refine during build.
- **OQ3 — Fail-closed roledef resolution.** Deferred (gated on roledef-strategist contract per Option A). Interim: autonomous-mode URL fetch failure aborts; embedded fallback only with explicit opt-in.
- **OQ4 — Bind-event memo home/shape.** Resolved-provisional: `memos/` with a subject convention; escalate to memodef-strategist only if a new envelope subtype proves warranted.
- **OQ5 — CLI surface.** Deferred to implementer design.

## Build directive

On Director ratification (merge), the implementer builds agent-sdk v0.2:

1. **`run_seat()`** — autonomous dispatch built on v0.1 `bind()`; returns a dispatch record.
2. **CLI dispatch wrapper** — `oagp-agent-sdk dispatch` (surface per OQ5).
3. **Tier 1: propose-only defaults** — default toolset excludes push/merge-capable tools; propose-only bind-context block added to `_synthesize_body` for the autonomous path.
4. **Tier 2: `grant_director_actions` parameter** — explicit elevation; moves the hard layer (tools) + updates the bind-context block + fires a mandatory bind-event memo.
5. **Tier 3: environmental non-delegation guard** — `bind()`/`run_seat()` inert in bound-agent execution contexts (mechanism per OQ1); no override path.
6. **Bind-event memo discipline** — emitted on every autonomous dispatch (resolves deferred §7.4).
7. **Fail-closed roledef resolution** — interim conservative default now; full contract when roledef-strategist replies (gated sub-item).
8. **Conformance tests** per proposal §Conformance Tests (all 7).

## Cross-spec coordination

- **roledef-strategist** — URL-resolution contract gates the fail-closed-resolution sub-item (memos/2026-05-25-0001, already filed by implementer).
- **memodef-strategist** — bind-event memo envelope shape if a new subtype is warranted (memos/2026-05-25-0002 already opened the adjacent filename-timestamp question).

## Notable design choices

1. **Bounded authority is structural, not conventional** — the load-bearing shift from v0.1. Tool/permission/environment scoping, not prompt instruction.
2. **Two soft-overridable tiers + one hard floor** — Tiers 1–2 respect Director authority to delegate; Tier 3 is non-negotiable because dispatch authority is categorically different from action authority (it creates participants, not just changes).
3. **Elevation moves the hard layer AND fires an audit memo** — never prompt-only, never silent.
4. **Tier 3 enforced environmentally** — the subtle but essential point: an elevated agent with shell could otherwise reach the dispatcher; the guard must be at the environment/kernel layer.
5. **Fail-closed roledef resolution in autonomous mode** — silent identity-swap is unacceptable when no human watches.
6. **The differentiated outreach story falls out of the design** — "safe by default, powerful by deliberate + audited choice, structurally incapable of self-replication" is a direct consequence of the three tiers, not added framing.

## Items not incorporated

- **Delegable dispatch** — rejected (Tier 3).
- **Prompt-only propose-only** — rejected (AGT lesson; hard layer required).
- **No-elevation-ever** — rejected (Director authority to delegate is legitimate).
- **Un-audited elevation** — rejected (accountability requires the trail).
- **Full roledef URL-resolution contract** — deferred per Option A; gated on roledef-strategist.

## Workflow validation

Charter version sequencing: the implementer's **v0.1.6** (agent-sdk graduation) history entry is drafted but not yet committed (pending in their session per memos/2026-05-25-0000 + my ratification memos/2026-05-28-1000). This v0.2 decision's charter entry is **v0.1.7**, sequenced AFTER v0.1.6 lands — to avoid a cross-session version collision, this decision's commit does NOT touch the charter or CLAUDE.md. On Director ratification, the v0.1.7 history entry + CLAUDE.md known-work-items update are applied once v0.1.6 is in (strategist or implementer applies, whichever sequences cleanly).

Note: this is a *design-direction* decision (shapes the v0.2 build); the build itself is implementer-execution and lands as subsequent commits with their own validation (the 7 conformance tests).

## Forward-reference resolution

- **Empirical validation milestone:** an actual unattended `run_seat()` dispatch producing proposal-memos that a human Director then ratifies — this is the demo that anchors outreach. Tracked as the post-build validation step.
- **Then outreach** — with the bounded-authority-autonomous-dispatch demo as the spine, positioned via the ETCLOVG org-sub-layer-of-Governance framing + the "composes with runtime-policy toolkits" (AGT) framing.
- **Consolidated pattern-promotion decision** (substrate-is-sufficient-context + composes-with-runtime-toolkits + org-sub-layer-of-G) — still queued; can ride into outreach-readiness.

## References

- Proposal: [proposals/agent-sdk-v0.2-autonomous-dispatch.md](../proposals/agent-sdk-v0.2-autonomous-dispatch.md)
- v0.1 ratification: [memos/2026-05-28-1000](../memos/2026-05-28-1000--oagp-strategist--oagp-implementer--bind-v0.1-ratified-interactive-scope-three-structural-requirements-to-v0.2.body.md)
- Origin recommendation: [memos/2026-05-23-1600](../memos/2026-05-23-1600--thingalog-strategist--oagp-strategist--bind-and-agent-view-empirically-validated-recommend-graduation.body.md)
- Graduation request: [memos/2026-05-25-0000](../memos/2026-05-25-0000--oagp-implementer--oagp-strategist--bind-prototype-graduated-to-agent-sdk-v0.1-ratification-request.body.md)
- roledef URL-resolution contract (gating dependency): [memos/2026-05-25-0001](../memos/2026-05-25-0001--oagp-implementer--roledef-strategist--url-resolution-contract-for-canonical-roledefs.body.md)
- Sub-org recursion question (answered for dispatch): [memos/2026-05-24-2200](../memos/2026-05-24-2200--oagp-strategist--oagp-strategist--sub-org-governance-implications-idea.body.md)
- Implementation reviewed: agent-sdk/src/oagp_agent_sdk/bind.py
