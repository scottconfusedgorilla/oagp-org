# Proposal: agent-sdk v0.2 — autonomous dispatch with bounded authority made structural

**Status:** Open (awaiting Director ratification via merge)
**Author:** oagp-strategist <oagp-strategist@oagp.org>
**Created:** 2026-05-28
**Target version:** oagp-org v0.1.7 (history entry; sequenced after the implementer's pending v0.1.6 agent-sdk-graduation entry — see Workflow note in the decision)
**Origin:**
- PO direction 2026-05-28: *"finalize the bind() work on dispatching autonomous agents. That is the 'trendy' thing right now and I think without it our efforts will be minimized."*
- v0.1 ratification ([memos/2026-05-28-1000](../memos/2026-05-28-1000--oagp-strategist--oagp-implementer--bind-v0.1-ratified-interactive-scope-three-structural-requirements-to-v0.2.body.md)) — the code review found bounded authority is *conventional* in v0.1 (human supervises), and must become *structural* for autonomous dispatch.
- PO crystallization 2026-05-28: *"we provide a gun, you provide a foot; the gun ships with instructions not to aim at the foot; if you want to aim at your foot that's your choice; and even then the gun can never give instructions to another gun."*
- Deferred items now ending: §7.3 (CLI dispatch) + §7.4 (bind-event memo discipline) from thingalog-strategist's 2026-05-23-1600 recommendation.

## Summary

agent-sdk v0.2 adds **autonomous dispatch** — `run_seat()` + a CLI dispatch wrapper that dispatch an agent bound to an OAGP position as an unattended background session. The defining property: **bounded authority becomes structural, not conventional.** Where v0.1 relies on a human watching the agent-view panel, v0.2 makes the agent *constructed unable* to act outside its sanction. Three tiers:

1. **Propose-only by construction** (default) — the agent has no push/merge-capable tools; it reads substrate, drafts artifacts, files memos.
2. **Explicit + audited Director elevation** (overridable) — the human Director may grant action authority; doing so moves the hard layer and fires an audit memo.
3. **Non-delegable dispatch** (hard floor, no override) — no bound agent, however elevated, may dispatch another agent; enforced environmentally.

This is the differentiated outreach story: *safe by default, powerful by deliberate + audited choice, and structurally incapable of self-replication.*

## Motivation

1. **Strategic necessity for outreach.** Autonomous dispatch is the capability the field is excited (and nervous) about. Without it, OAGP outreach is minimized; with it framed correctly, OAGP demonstrates the *safe* version.
2. **Empirical proof of the core claim.** OAGP's whole value is bounded-authority discipline. An autonomous agent that runs unattended yet cannot merge/push/decide is that claim made concrete and demoable.
3. **Removing the human-in-the-loop-per-action forces the property to be structural.** v0.1's bounded authority is supervision-convention (a human is the backstop). Autonomous dispatch removes the live backstop, so the constraint must move from prompt-instruction (soft) to tool/permission/environment scoping (hard). Per the AGT lesson reviewed 2026-05-26: prompt-level instruction is not a control surface for a stochastic system.

## Proposed Change

### New API surface

- **`run_seat(orgdef_path, position_id, *, brief, grant_director_actions=None, ...) -> DispatchResult`** — binds the position (via v0.1 `bind()`) and dispatches it as an unattended background session. Returns a dispatch record (agent name, org-state SHA, granted authority, bind-event memo path).
- **CLI dispatch wrapper** — `oagp-agent-sdk dispatch <position> --brief "..."` wrapping `claude --bg --agent <name>` (exact surface is an implementer design call).
- Both build on v0.1 `bind()` unchanged.

### Tier 1 — propose-only by construction (default)

- `run_seat()` defaults to a propose-only toolset (Read, Write scoped to the workspace, Glob, Grep, memo-filing). **No Bash-with-git, no push/merge/tag/release tools.**
- The bind-context system prompt gains a **propose-only block**: *"You may read the org substrate, draft artifacts, and file memos (propose). You may NOT commit, push, merge, tag, release, or ratify — those are Director-only. Your work accumulates as proposals a human Director reviews and ratifies."*
- **Structural:** the tool omission is the hard layer; the prompt block is the soft layer that explains it. The agent is *constructed* unable, not *asked* to refrain.

### Tier 2 — explicit + audited Director elevation (overridable)

- A deliberate parameter `grant_director_actions: list[str] | None = None` (default `None` = propose-only). The human Director may pass e.g. `["commit"]` or `["commit", "push"]`.
- Granting elevation does three things together:
  1. **Moves the hard layer** — adds the capable tools to the agent's frontmatter (not just prompt text).
  2. **Updates the bind-context block** — reflects the granted authority honestly.
  3. **Fires a bind-event memo** (mandatory) — records who granted what, when, against which org-state SHA.
- Never a silent default; requires explicit, deliberate opt-in.
- The elevated agent acts as the Director's **delegated instrument**; the human remains accountable. It does not become a second Director.

### Tier 3 — non-delegable dispatch (hard floor, NO override)

- No bound agent — propose-only or elevated — may dispatch / bind / elevate another agent.
- **Enforcement is environmental**, not tool-list-omission or prompt-text (an elevated agent with `Bash` + the sdk importable could otherwise reach the dispatcher via `python -c "from oagp_agent_sdk import bind; ..."`):
  - `bind()` / `run_seat()` refuse to run when a bound-agent session marker is present (e.g., an env var like `OAGP_BOUND_AGENT=1` set on dispatch), and/or
  - the dispatch execution environment does not expose the sdk package importably.
- **No parameter, no flag, no Director override** grants dispatch authority to an agent.
- Rationale: keeps the accountability chain exactly one hop deep (every agent traces directly to a human Director); structurally prevents runaway agent proliferation. Answers the recursion question from [memos/2026-05-24-2200](../memos/2026-05-24-2200--oagp-strategist--oagp-strategist--sub-org-governance-implications-idea.body.md) for the dispatch case: dispatch does not recurse.

### Bind-event memo discipline (now triggered — resolves deferred §7.4)

- Every autonomous dispatch emits a **bind-event memo**: `from` = the dispatching human's seat (director), `to` = the dispatched seat, recording: agent name, position id, org-state SHA, granted-authority (propose-only or the elevated action list), dispatch timestamp, brief.
- This memo is the audit trail that **replaces live human supervision** in autonomous mode.
- Interactive `bind()` (v0.1 path) is unchanged — no bind-event memo; the agent-view session list remains its trail.

### Fail-closed roledef resolution (gated sub-item)

- In autonomous mode, a URL roledef fetch failure should **fail closed** (abort dispatch with a clear error) rather than silently falling back to embedded — because no human is watching to notice an identity swap.
- **Gated on the roledef-strategist URL-resolution contract** ([memos/2026-05-25-0001](../memos/2026-05-25-0001--oagp-implementer--roledef-strategist--url-resolution-contract-for-canonical-roledefs.body.md)). Interim conservative default until that contract lands: autonomous-mode URL fetch failure aborts; embedded fallback available only with explicit `allow_embedded_fallback=True` or in interactive mode.

## Backward Compatibility

- v0.1 `bind()` unchanged; interactive dispatch works exactly as before.
- v0.2 is purely additive (`run_seat()` + CLI + the propose-only defaults apply only to the new autonomous path).

## Conformance Tests

1. `run_seat()` with default args produces a subagent with **no** push/merge-capable tools.
2. The propose-only bind-context block is present in the default-dispatched agent's system prompt.
3. Elevation requires the explicit `grant_director_actions` param; absent it, no capable tools appear.
4. Elevation fires a bind-event memo recording the grant.
5. A bound-agent execution context **cannot** invoke `bind()` / `run_seat()` (environmental floor) — verify the marker/refusal path.
6. Autonomous-mode URL roledef fetch failure **fails closed** (aborts) absent explicit fallback opt-in.
7. A bind-event memo is emitted on every autonomous dispatch.

## Alternatives Considered

1. **Propose-only as a prompt-only constraint (no tool scoping).** Rejected — prompt-level safety is not a control surface (AGT lesson). The hard layer is the tool list.
2. **Allow agents to dispatch sub-agents (delegable dispatch).** Rejected — breaks the accountability chain; enables runaway proliferation. Tier 3 hard floor.
3. **No elevation possible (hard propose-only floor for everything).** Rejected — the human Director has legitimate authority to delegate; a tool that refuses the Director inverts the hierarchy.
4. **Elevation without a mandatory audit memo.** Rejected — accountability requires the trail; an un-audited grant lets authority float free of a human.
5. **Wait for the roledef URL-resolution contract before any v0.2.** Rejected (PO chose Option A 2026-05-28) — tiers 1–3 are the differentiated core and don't depend on the roledef contract; fail-closed resolution lands as a follow-up.

## Open Questions

- **OQ1 — Tier 3 environmental enforcement mechanism.** Session-marker env var vs. package-absent sandbox vs. both. Implementer design call; the floor is non-negotiable, the mechanism is open.
- **OQ2 — `grant_director_actions` granularity.** Per-action list (`["commit","push"]`) vs. coarse levels (`"elevated"`). Lean per-action for auditability; refine during build.
- **OQ3 — Fail-closed roledef resolution specifics.** Gated on roledef-strategist contract.
- **OQ4 — Bind-event memo home + shape.** `memos/` with a subject convention, or a dedicated log? Lean `memos/` with clear convention; memodef-strategist coordination if a new envelope subtype is warranted.
- **OQ5 — CLI surface shape.** `oagp-agent-sdk dispatch ...` vs. thin wrap of `claude --bg --agent`. Implementer call.

## Cross-spec coordination

- **roledef-strategist** — URL-resolution contract gates the fail-closed-resolution sub-item ([memos/2026-05-25-0001](../memos/2026-05-25-0001--oagp-implementer--roledef-strategist--url-resolution-contract-for-canonical-roledefs.body.md)).
- **memodef-strategist** — bind-event memo envelope shape, if a new memodef subtype (vs. a plain `memodef:Memo` with a convention) is warranted. Lightweight; coordinate when bind-event discipline is built.
