# Decision: agent-sdk v0.2 governance addendum — autonomous-dispatch operational constraints (launcher-per-dispatch; Tier-2 gating)

**Disposition:** Accept (recommended; awaiting Director ratification via merge)
**Origin:** Empirical findings from the §8 demo, [memos/2026-05-29-1700](../memos/2026-05-29-1700--oagp-implementer--oagp-strategist--agent-sdk-v0.2-live-workflows-wired-demo-findings.body.md) §3–§4. Amends the autonomous-dispatch model in [decisions/proposal-agent-sdk-v0.2-autonomous-dispatch.md](proposal-agent-sdk-v0.2-autonomous-dispatch.md) (Tier-3 §) and the consolidated build-direction [memos/2026-05-29-1300](../memos/2026-05-29-1300--oagp-strategist--oagp-implementer--agent-sdk-v0.2-consolidated-build-direction.body.md) §4/§8.
**Decided:** Drafted 2026-05-29 by oagp-strategist; Director ratifies on merge.
**Authorization:** Implementer routed two governance/operational calls (memos/2026-05-29-1700 §3, §4) explicitly to oagp-strategist; these are pattern-shape MUST-conventions (delegated strategist authority; Director ratifies-by-merge).

## Rationale

The live WorkflowsBackend (commit 3644bb6) empirically validated propose-only autonomous dispatch and, in doing so, surfaced two facts about *how* bounded authority must be enforced in the Workflows path. Both turn out to reinforce the bounded-authority property rather than weaken it, but they require explicit canonical constraints so future implementers and auditors don't re-open the holes.

The unifying insight: **the structural Tier-1 bound (the agent file's `tools:` frontmatter) is only loaded when dispatch goes through `agentType` in a session that started after the agent file existed.** Therefore the *only* bounded-authority-preserving autonomous-dispatch path is fresh-session + agentType. Inline/same-session dispatch silently substitutes the workflow's broad default toolset and is not a sanctioned autonomous path. The session-start registry rule (Finding 1) does not obstruct this — it enforces it.

## The two rulings

### Ruling A — launcher-per-dispatch is the canonical autonomous-dispatch shape (Finding 1, §3)

1. Autonomous `run_seat()` dispatch **MUST** use the fresh-session / `agentType` path: a launcher starts a clean session per dispatch, against which the bound agent file pre-exists and resolves.
2. Inline / same-session dispatch **MUST NOT** be used for autonomous runs — it cannot carry the agent file's `tools:` frontmatter and so silently breaks the Tier-1 structural bound. It is acceptable only for clearly-labeled interactive/demo mechanics, never as a sanctioned autonomous path.
3. This composes naturally with the autonomous/cron use case (each scheduled dispatch is a fresh session anyway) and reinforces seat-vs-incumbent (no cross-dispatch state leakage).
4. The launcher is canonical infrastructure; the implementer designs the hook.

### Ruling B — Tier-1 is the only sanctioned autonomous path until Tier-2 is launcher-gated (Finding 2, §4)

1. **Tier-1 (propose-only) autonomous dispatch is PERMITTED now.** It is safe by toolset construction: no `Bash` → no capability to reach a dispatcher → the Tier-3 non-delegable floor holds regardless of the env-marker's unavailability in the Workflows path. Package-absence is defense-in-depth, not the load-bearing barrier, for Tier-1.
2. **Tier-2 (elevated) autonomous dispatch via Workflows is PROHIBITED** until a **verified package-absent dispatch environment** exists. In the Workflows path the `OAGP_BOUND_AGENT` env marker cannot be injected, so for a Bash-capable elevated agent the *only* barrier to self-dispatch is that `oagp_agent_sdk` is not importable. Tier-3 is the one floor with no override; a deployment guarantee the SDK merely documents is not, by itself, a sufficient hard floor.
3. **Required mechanism:** the launcher (Ruling A) **MUST** verify package-absence (the dispatch environment cannot import `oagp_agent_sdk`) as a preflight before any Tier-2 autonomous dispatch; absent that verification the launcher **MUST** refuse the Tier-2 dispatch. This converts the deployment guarantee into an in-band, launcher-enforced, verifiable gate rather than a documented hope.
4. Convergence: the launcher is the single locus of both Ruling A (fresh-session handling) and Ruling B (Tier-2 package-absence preflight).

## Resolutions to the implementer's questions

- **§3 "is launcher-per-dispatch the canonical shape?"** — Yes (Ruling A). Document it as canonical; design the launcher hook.
- **§4 "is package-absence an acceptable Tier-3 floor, or do you want a stronger mechanism before Tier-2 autonomous dispatch?"** — Acceptable for Tier-1 (which is already safe by toolset). NOT sufficient on its own for Tier-2; Tier-2 autonomous dispatch is gated behind launcher-verified package-absence (Ruling B). Your recommendation (keep Tier-1 as the only autonomous path until the gate is in place) is ratified.

## Build directive

On Director ratification (implementer-execution):

1. Document launcher-per-dispatch as the canonical autonomous-dispatch operational pattern (agent-sdk docs + README/examples).
2. Design the launcher hook: starts a clean session per dispatch; runs the generated dispatch workflow against the pre-existing agent file via `agentType`.
3. Implement the Tier-2 preflight: launcher verifies `oagp_agent_sdk` is not importable in the dispatch environment before any Tier-2 dispatch; refuse otherwise.
4. Until the gate ships, restrict autonomous dispatch to Tier-1; mark Tier-2 autonomous as unsupported-pending-gate in docs and (if feasible) refuse it at the API with a clear error.
5. Add conformance tests: (a) inline/same-session dispatch is rejected or clearly-labeled-non-structural for autonomous use; (b) Tier-2 autonomous dispatch refuses absent verified package-absence.

## Cross-spec coordination

None new. Independent of the still-pending memodef bind-event-subtype (memos/2026-05-29-1601) and roledef URL-resolution (memos/2026-05-25-0001) items.

## Notable design choices

1. **The constraint is the enforcement.** The session-start rule forces the only toolset-bound dispatch path; we adopt it as canonical rather than working around it.
2. **Inline dispatch is barred for autonomous runs** — it cannot carry the structural bound. Naming this prevents a future "convenience" regression.
3. **Tier-2 gated, not merely warned.** The launcher verifies package-absence; a documented deployment guarantee alone is insufficient for a no-override floor.
4. **Tier-1-only until the gate exists** — ships the safe capability now without waiting on the Tier-2 mechanism.
5. **Single locus (launcher)** for both operational constraints — cohesive, auditable.

## Items not incorporated

- Permitting Tier-2 autonomous dispatch on documented-package-absence alone — rejected (insufficient for a no-override floor).
- An in-band env-marker mechanism for the Workflows path — not available (the Workflow tool exposes no per-agent env); superseded by the launcher preflight.

## Workflow validation

Charter untouched in this decision's commit (the v0.1.x history is current at v0.1.8; this addendum is a governance refinement that will fold into the next charter pass if a version bump is warranted, or stand as a decision artifact). Build is implementer-execution.

## Forward-reference resolution

- A **fresh-session end-to-end structural run** (agentType, launcher-driven) closes the full §8 demo (the inline variant validated the read→work→file flow; the structural path validates the toolset bound under real dispatch).
- Launch remains Director-gated/deferred.

## References

- Findings: [memos/2026-05-29-1700](../memos/2026-05-29-1700--oagp-implementer--oagp-strategist--agent-sdk-v0.2-live-workflows-wired-demo-findings.body.md)
- Amends: [decisions/proposal-agent-sdk-v0.2-autonomous-dispatch.md](proposal-agent-sdk-v0.2-autonomous-dispatch.md) + [decisions/proposal-agent-sdk-v0.2-amendment-workflows-composition-and-positioning.md](proposal-agent-sdk-v0.2-amendment-workflows-composition-and-positioning.md)
- Build-direction: [memos/2026-05-29-1300](../memos/2026-05-29-1300--oagp-strategist--oagp-implementer--agent-sdk-v0.2-consolidated-build-direction.body.md)
- Reply to implementer: [memos/2026-05-29-1800](../memos/2026-05-29-1800--oagp-strategist--oagp-implementer--demo-validated-launcher-and-tier2-gating-ratified.body.md)
- Demo evidence: agent-sdk/examples/demo-output/ (review-proposal.md; bind-event-doc-reviewer.*)
