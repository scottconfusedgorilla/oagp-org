# agent-sdk v0.2 — consolidated build-direction (turnkey for a fresh implementer session)

**From:** oagp-strategist (s:/projects/oagp-org)
**To:** oagp-implementer
**Date:** 2026-05-29
**Action required:** Yes — when the implementer seat staffs, build against this single spec
**Consolidates:** [decisions/proposal-agent-sdk-v0.2-autonomous-dispatch.md](../decisions/proposal-agent-sdk-v0.2-autonomous-dispatch.md) (base) + [decisions/proposal-agent-sdk-v0.2-amendment-workflows-composition-and-positioning.md](../decisions/proposal-agent-sdk-v0.2-amendment-workflows-composition-and-positioning.md) (re-scope; **wins on conflict**)

---

## 1. Why this memo exists

The Director prioritized this build 2026-05-29. The spec lives in two ratified decisions (the amendment re-scoped the base), and you shouldn't have to reconcile them by hand. This is the **single current spec.** It is *direction*, not code — building the package is your seat's call; this states what must hold and the bar it must clear.

Scope note: oagp-strategist wrote this; oagp-strategist does **not** write the package (bounded authority). Execution is a staffed implementer session.

## 2. What v0.2 is (one sentence)

Autonomous dispatch: dispatch an agent bound to an OAGP position as an **unattended** session, where bounded authority is **structural** (the agent is constructed unable to act outside its sanction), and — per the amendment — the Claude-Code dispatch backend is the **native Workflows-class dispatcher**, not bespoke plumbing.

## 3. Deliverables

1. **`run_seat()`** — the runtime-neutral autonomous-dispatch entry point, built on v0.1 `bind()`. Returns a dispatch record (agent name, org-state SHA, granted authority, bind-event memo path).
2. **Dispatch-backend abstraction** — `run_seat()` selects a backend per runtime. **On Claude Code: compose over the native Workflows-class dispatcher** (do NOT build a subprocess/CLI scheduler from scratch — that was the base decision; the amendment removed it). `run_seat()` stays the cross-vendor seam; other runtimes get other backends later.
3. **Tier-1 / Tier-2 / Tier-3 enforcement** (§4) — the load-bearing governance work.
4. **Bind-event memo emission** (§5).
5. **Conformance tests** (§6).

**Preserve unchanged from v0.1** (do not regress): roledef→AgentDefinition translation; time-travel binding (`git worktree add <sha>`); the synthesized-body structure; the empirical defaults (acceptEdits, flat path, single-hyphen names, color map).

## 4. The three tiers (the differentiator — make these STRUCTURAL, not prompt-level)

Per PO crystallization: *"we provide a gun, you provide a foot; the gun ships with instructions not to aim at the foot; if you want to aim at your foot that's your choice; and even then the gun can never give instructions to another gun."*

- **Tier 1 — propose-only by construction (default).** `run_seat()` default toolset has **no** push/merge/commit/tag/release-capable tools. The propose-only bind-context block is added to the system prompt. The tool omission is the hard layer; the prompt block explains it. The agent is *constructed* unable, not *asked* to refrain.
- **Tier 2 — explicit + audited Director elevation (overridable).** A deliberate parameter (e.g. `grant_director_actions=["commit", ...]`, default `None`). Granting it must, together: (a) add the capable tools to the agent (hard layer), (b) update the bind-context block to state the granted authority honestly, (c) **fire a bind-event memo** recording who granted what, when, against which org-state SHA. Never silent; never prompt-only. The elevated agent is the Director's delegated instrument; the human stays accountable.
- **Tier 3 — non-delegable dispatch (hard floor, NO override).** No bound agent — however elevated — may dispatch/bind/elevate another agent. **Enforced environmentally**, not by tool-omission or prompt text: `bind()`/`run_seat()` **and any Workflows-class entry point** must be inert when invoked inside a bound-agent execution context (e.g. refuse when a bound-agent session marker is present, and/or the dispatch environment doesn't expose the package). The amendment's hazard: an elevated agent with shell + an importable dispatcher (or reachable Workflows) could otherwise spawn subagents — close that. No parameter grants dispatch authority to an agent.

## 5. Bind-event memo discipline (resolves the deferred §7.4)

Every autonomous dispatch emits a bind-event memo: `from` = the dispatching human's seat (director), `to` = the dispatched seat; records agent name, position id, org-state SHA, granted authority (propose-only or the elevated list), timestamp, brief. This memo is the audit trail that **replaces live human supervision** in autonomous mode. (Interactive `bind()` from v0.1 is unchanged — no bind-event memo; agent-view session list is its trail.)

## 6. Conformance tests (the bar; from the base decision + amendment)

1. `run_seat()` default produces a subagent with **no** push/merge-capable tools.
2. The propose-only bind-context block is present by default.
3. Elevation requires the explicit param; absent it, no capable tools appear.
4. Elevation fires a bind-event memo recording the grant.
5. A bound-agent execution context **cannot** invoke `bind()` / `run_seat()` / a Workflows-class entry point (Tier-3 environmental floor) — verify the refusal path.
6. Autonomous-mode URL roledef fetch failure **fails closed** (aborts) absent explicit fallback opt-in (interim default; see §7).
7. A bind-event memo is emitted on every autonomous dispatch.
8. On Claude Code, the dispatch path delegates to the native Workflows-class dispatcher rather than bespoke subprocess plumbing.
9. `run_seat()` exposes a runtime-neutral interface; roledef→AgentDefinition translation remains runtime-target-agnostic.

## 7. The one gating dependency

**Fail-closed roledef resolution** (Tier-relevant: an autonomous agent must not silently boot with the wrong identity) is gated on the **roledef-strategist URL-resolution contract** ([memos/2026-05-25-0001](2026-05-25-0001--oagp-implementer--roledef-strategist--url-resolution-contract-for-canonical-roledefs.body.md)), which awaits that seat. **Interim default (build to this now):** autonomous-mode URL fetch failure aborts; embedded fallback only with explicit `allow_embedded_fallback=True`. Swap to the ratified contract when it lands. This does NOT block tiers 1–3 or the demo.

## 8. The empirical demo (the milestone that anchors any future reveal)

The build is "done enough to matter" when you can show: an **unattended `run_seat()` dispatch** (Workflows-backed on Claude Code), default propose-only, that reads the org substrate, does real work, and **files proposal-memos a human then ratifies** — with the bind-event memo as the audit trail and zero capability to merge/push/self-dispatch. That demo is the concrete proof of bounded autonomous dispatch. (Public use of it is Director-gated — launch is deferred pending refinement per 2026-05-29; the demo is the refinement, not the launch.)

## 9. Open design calls that are YOURS (implementer scope)

- Backend-selection mechanism (capability detection vs config).
- Tier-3 marker mechanism (env var vs package-absence vs both) — the floor is non-negotiable; the mechanism is yours.
- `grant_director_actions` granularity (per-action list recommended for auditability).
- File layout, test structure, packaging.

## 10. Coordination back to this seat

File an action-required memo to oagp-strategist if the build surfaces a **pattern-shape** question (e.g. the bind-event memo envelope wants a new memodef subtype → that's a memodef-strategist coordination; the Tier semantics need a governance clarification → mine). Pure implementation questions are yours. When the demo lands, a status memo to this seat closes the loop and feeds the (still-deferred) outreach readiness.

— oagp-strategist
