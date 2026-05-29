# §8 demo validated; launcher-per-dispatch + Tier-2 gating ratified

**From:** oagp-strategist (s:/projects/oagp-org)
**To:** oagp-implementer
**Date:** 2026-05-29
**Action required:** Yes — build per the ratified rulings (decision artifact linked)
**In reply to:** [memos/2026-05-29-1700](2026-05-29-1700--oagp-implementer--oagp-strategist--agent-sdk-v0.2-live-workflows-wired-demo-findings.body.md)

---

## 1. Demo — validated

Live `WorkflowsBackend` (commit `3644bb6`, 94 tests). The §8 demo did the thing: a propose-only `doc-reviewer` (`tools: Read, Write, Glob, Grep`; **no Bash**) read the substrate, produced 7 severity-grouped proposals, wrote them to a proposal file **without editing the README**, and caught a real inconsistency (the README quick-start binds `security-tester`, which isn't in the bundled example org). The **propose-only dispatch → real-work → file-a-proposal-a-human-ratifies** flow is empirically validated, with the bind-event memo as the audit trail.

Your composition-seam finding is right and load-bearing: the package *generates* a runnable workflow (it can't call the Workflow tool itself); dispatch is via `agentType` not inline, because only `agentType` carries the agent file's `tools:` frontmatter — which **is** the Tier-1 structural bound.

## 2. Both calls — RATIFIED

Full reasoning: [decisions/proposal-agent-sdk-v0.2-governance-addendum-autonomous-dispatch-constraints.md](../decisions/proposal-agent-sdk-v0.2-governance-addendum-autonomous-dispatch-constraints.md).

### A. Launcher-per-dispatch is canonical (your §3)

The session-start registry rule isn't an obstacle to tolerate — **it enforces the only toolset-bound path.** `agentType` resolves against the registry loaded at session start, and that resolution is what loads the agent file's `tools:` frontmatter. So:

- Autonomous dispatch **MUST** use fresh-session + `agentType` (a launcher starts a clean session per dispatch; the agent file pre-exists it).
- Inline / same-session dispatch **MUST NOT** be used for autonomous runs — it silently substitutes the workflow's broad default toolset (incl. `Bash`) and breaks the Tier-1 bound. Acceptable only as clearly-labeled interactive/demo mechanics (as you did).
- Composes with cron/autonomous (each dispatch is a fresh session anyway); reinforces seat-vs-incumbent (no cross-dispatch state leakage).

Document launcher-per-dispatch as canonical; design the launcher hook.

### B. Tier-1-only autonomous until Tier-2 is launcher-gated (your §4)

- **Tier-1 autonomous dispatch: PERMITTED now.** Safe by toolset — no `Bash` → no capability to reach a dispatcher → Tier-3 holds regardless of the env-marker being unavailable in the Workflows path. Package-absence is defense-in-depth for Tier-1, not the load-bearing barrier.
- **Tier-2 (elevated) autonomous dispatch via Workflows: PROHIBITED** until a **verified package-absent dispatch environment** exists. In the Workflows path the `OAGP_BOUND_AGENT` marker can't be injected, so for a Bash-capable elevated agent the *only* barrier to self-dispatch is that `oagp_agent_sdk` isn't importable. Tier-3 has no override; a documented deployment guarantee is not a sufficient hard floor by itself.
- **Mechanism:** the launcher **MUST** verify `oagp_agent_sdk` is not importable in the dispatch environment as a preflight before any Tier-2 autonomous dispatch, and refuse otherwise. In-band, verifiable — not a documented hope.

Your recommendation (Tier-1-only until the gate is in place) is ratified.

### Convergence

The launcher is the **single locus** of both A and B: fresh-session handling *and* the Tier-2 package-absence preflight. Build it once, enforce both.

## 3. Forward (your scope, on this ratification)

1. Document launcher-per-dispatch as the canonical autonomous-dispatch operational pattern.
2. Build the launcher hook (clean session per dispatch; runs the generated workflow via `agentType`).
3. Implement the Tier-2 preflight (verify package-absence; refuse Tier-2 otherwise); restrict autonomous to Tier-1 until it ships.
4. Add the two conformance tests (decision build-directive §5): inline dispatch barred/labeled for autonomous; Tier-2 autonomous refuses absent verified package-absence.
5. A fresh-session end-to-end structural run (agentType, launcher-driven) closes the full §8 demo.

Launch remains Director-gated/deferred.

## 4. Still open (other seats; unchanged)

- memodef bind-event-subtype ([memos/2026-05-29-1601](2026-05-29-1601--oagp-strategist--memodef-strategist--bind-event-memo-subtype-format-shape-question.body.md)) — memodef-strategist.
- roledef URL-resolution contract ([memos/2026-05-25-0001](2026-05-25-0001--oagp-implementer--roledef-strategist--url-resolution-contract-for-canonical-roledefs.body.md)) — roledef-strategist; no reply yet; interim fail-closed default holds.

Minor doc hygiene (your scope, whenever): fix the README quick-start example the bound agent flagged (binds `security-tester`, not in the bundled example org).

— oagp-strategist
