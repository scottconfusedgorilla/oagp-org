# Proposal: agent-sdk v0.2 amendment — compose-with-Workflows + OAGP layer-positioning

**Status:** Open (awaiting Director ratification via merge)
**Author:** oagp-strategist <oagp-strategist@oagp.org>
**Created:** 2026-05-29
**Target version:** oagp-org v0.1.8 (history entry; sequenced after the pending v0.1.6 [implementer agent-sdk graduation] and v0.1.7 [v0.2 autonomous-dispatch direction] entries — charter reconciliation is a known cross-session debt, see Workflow note in the decision)
**Origin:**
- PO question 2026-05-29: *"your new workflows can clearly run async tasks without any extra code. Is the bind() work we are doing redundant?"* + the broader *"how will workflows affect the OAGP concept, and vice versa? Is our work still relevant?"*
- Adversarial-analysis workflow `wf_6a87be32-ee4` (9 agents; 4 lenses → adversarial verify → synthesis), 2026-05-29. The synthesis is a verified draft; this proposal carries its surviving recommendations into ratifiable form.
- Amends: [decisions/proposal-agent-sdk-v0.2-autonomous-dispatch.md](../decisions/proposal-agent-sdk-v0.2-autonomous-dispatch.md).

## Summary

The Claude Code Workflows feature (native deterministic multi-agent orchestration) does **not** obsolete bind()/the agent-sdk, because the two operate on opposite axes: Workflows-dispatch **maximizes** task fan-out (recursion is a feature); OAGP-dispatch **caps** it (the Tier-3 non-delegable floor). They compose — Workflows is a within-session execution primitive; OAGP is the cross-session organizational-governance layer over it. This proposal (1) re-scopes agent-sdk v0.2 to **compose with Workflows as the Claude-Code dispatch backend** rather than build dispatch plumbing from scratch, (2) tightens the Tier-3 environmental-enforcement requirement to cover the Workflows-inside-bound-agent hazard, (3) canonicalizes OAGP layer-positioning language, and (4) folds a narrowly-scoped pattern-promotion candidate into the existing queue. It also surfaces (to the Director) that the residual risk is adoption traction, not capability redundancy.

## Motivation

The bind()-redundancy worry conflates *orchestration plumbing* (which Workflows wins) with what bind()/agent-sdk uniquely is:
- the **roledef→AgentDefinition translation** (governance identity → runnable agent) — Workflows has no equivalent;
- **cross-vendor** binding (charter scope: Anthropic/OpenAI/Google/others) — Workflows is single-vendor by construction; leaning on it as *the* dispatch mechanism would be a no-vendor-capture red-line violation;
- **persistent named seats** (agent-view supervised sessions) vs ephemeral task-subagents;
- **time-travel binding** (git-worktree-at-SHA) — orthogonal to Workflows;
- the **governance half** (bind-event memos, three-tier authority as auditable/ratifiable primitive).

The verified workflow synthesis put it crisply: *"the differentiator was never the plumbing — it is the governance wrapper."* And the layer crux: *"a capability built to maximize fan-out cannot subsume a pattern whose hard floor is capping fan-out."*

Independent corroboration worth banking (narrowly): the Workflow tool enforces *"nesting is one level only"* — a structural re-derivation of OAGP's Tier-3 non-delegable-dispatch floor, by a vendor with no knowledge of OAGP. This validates the *dispatch shape*; it leaves OAGP's governance/persistence/ratification layers un-re-derived and still OAGP's to own.

## Proposed Change

### 1. Re-scope agent-sdk v0.2 dispatch (amends the v0.2 build directive)

- **Remove** "build a CLI dispatch wrapper / `run_seat()` subprocess-scheduler from scratch" as a Claude-Code-runtime deliverable.
- **Recast** `run_seat()` as the **runtime-neutral dispatch abstraction**. On the Claude Code transport, its preferred backend is the native Workflows-class dispatcher (Tier-1 propose-only workers map onto it). On non-Anthropic runtimes, other backends; `run_seat()` sits above all of them.
- **Preserve unchanged** the unique core: roledef→AgentDefinition translation, time-travel binding, bind-event memo discipline, the three-tier bounded-authority model as governance (not merely execution scoping).
- **Net effect:** lowers agent-sdk plumbing burden; the governance wrapper is the differentiator and is untouched.

### 2. Tighten the Tier-3 environmental-enforcement requirement

Add to the three-tier spec: Workflows-class fan-out is permitted **under an interactive seat (human backstop)** or **as the top-level orchestrator**; it MUST be **absent/inert inside any autonomously-dispatched bound-agent execution context.** The hazard: an elevated bound agent with shell + an importable dispatcher could spawn subagents, breaching the non-delegable floor. The existing environmental guard (dispatch tooling inert when a bound-agent session marker is present) must explicitly cover Workflows-class entry points, not just `bind()`/`run_seat()`.

### 3. Canonicalize OAGP layer-positioning language

Adopt and land (README + the substrate-neutral primer.md) the one-liner:

> *"OAGP is the cross-session organizational-governance layer. Runtime orchestration primitives (Claude Code Workflows, multi-agent frameworks) are within-session execution mechanisms that OAGP composes over — AGT-class policy enforcement beneath, OAGP above."*

Workflows is **one acceptable transport, not a privileged substrate.** Any framing implying Claude Code is the canonical substrate is a no-vendor-capture red-line violation. Extends the primer's existing "OAGP IS NOT" block with a fourth negation: *not a within-session orchestration framework.*

### 4. Fold a narrow pattern-promotion candidate into the queue

Add to the consolidated pattern-promotion queue (the candidate list tracked from memos/2026-05-28-1000 §8): **"dispatch is commodity; governance is the value."** Defensible claim only: external convergence (Workflows' one-level-nesting; AGT; orchestration frameworks) validates the dispatch *shape*; OAGP's distinct contribution is upstream — the Tier-3 floor + human ratification + cross-session persistence. **Do not overclaim** "a vendor re-derived OAGP" — the convergence is on generic task-decomposition mechanics, not on OAGP's governance instrument.

### 5. Surface the adoption headwind to the Director (not a strategist call)

The capability case is settled; the traction case is not. v1 criterion (d) — one non-spec real-org adopter in the wild — remains unmet; every named use is still first-party (Thingalog, Caliper). The bootstrap-ceremony-vs-write-a-script friction asymmetry is the genuine adoption gate. **This is a Director priority/resourcing decision, flagged here, not decided by the strategist seat.**

## Backward Compatibility

- bind() v0.1 (interactive) unchanged.
- The v0.2 *direction* (three tiers; bind-event memos; fail-closed roledef resolution) is preserved; only the dispatch-backend implementation strategy changes (compose vs build-from-scratch).
- No change to ratified decisions other than this explicit amendment to the v0.2 build directive.

## Conformance Tests

1. `run_seat()` exposes a runtime-neutral interface; the Claude-Code backend delegates to a Workflows-class dispatcher rather than bespoke subprocess plumbing.
2. roledef→AgentDefinition translation remains the agent-sdk's core and is runtime-target-agnostic.
3. A Workflows-class entry point is inert when invoked inside a bound-agent execution context (Tier-3 guard covers it).
4. README + primer.md carry the layer-positioning language and the fourth "OAGP IS NOT" negation.
5. The pattern-promotion queue entry states the narrow claim (validates shape; not "vendor re-derived OAGP").

## Alternatives Considered

1. **Abandon bind()/agent-sdk; use Workflows directly.** Rejected — vendor capture (red line); loses roledef-translation, cross-vendor reach, persistent seats, governance semantics.
2. **Ignore Workflows; build run_seat() plumbing as originally specced.** Rejected — wasteful reinvention of a now-native runtime capability; the workflow analysis confirmed the plumbing was never the differentiator.
3. **Promote a strong "vendor re-derived OAGP" pattern claim.** Rejected — overclaim; the convergence is on dispatch mechanics, not governance. Narrow claim only.
4. **Treat Workflows as OAGP's canonical dispatch substrate.** Rejected — single-vendor; substrate/vendor capture.

## Open Questions

- **OQ1 — Backend abstraction shape.** How `run_seat()` selects/declares its dispatch backend per runtime (config? capability detection?). Implementer design call.
- **OQ2 — Tier-3 guard mechanism for Workflows entry points.** Shared with the v0.2 OQ1 (session-marker vs package-absence); now must cover Workflows-class imports too.
- **OQ3 — Positioning venue.** Whether the layer-positioning language also belongs in the charter `vision`/`scope` or only in README + primer. Lean README + primer first; charter on the next reconciliation pass.

## Cross-spec coordination

- None newly required. roledef-strategist URL-resolution contract (memos/2026-05-25-0001) still gates fail-closed roledef resolution, unchanged by this amendment.
