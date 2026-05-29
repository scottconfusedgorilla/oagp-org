# Decision: agent-sdk v0.2 amendment — compose-with-Workflows + OAGP layer-positioning

**Disposition:** Accept (recommended; awaiting Director ratification via merge)
**Origin:** [proposals/agent-sdk-v0.2-amendment-workflows-composition-and-positioning.md](../proposals/agent-sdk-v0.2-amendment-workflows-composition-and-positioning.md)
**Decided:** Drafted 2026-05-29 by oagp-strategist; Director ratifies on merge.
**Authorization:** PO direction 2026-05-29: *"Is the bind() work we are doing redundant?"* → on review, *"Yes, please do"* (draft the consolidated v0.2-amendment + Workflows-positioning decision). Evidence base: adversarial-analysis workflow `wf_6a87be32-ee4` (9 agents, 2026-05-29) — its synthesis is a verified draft, and this decision carries its surviving recommendations into ratifiable form.

## Rationale

bind() is not redundant. The redundancy worry conflates *orchestration plumbing* (Workflows wins) with the agent-sdk's actual core (roledef→AgentDefinition translation, cross-vendor binding, persistent seats, time-travel, governance semantics). The decisive frame, verified by adversarial analysis: Workflows-dispatch maximizes fan-out; OAGP-dispatch caps it (Tier-3). Opposite axes — a fan-out-maximizing primitive cannot subsume a fan-out-capping pattern. They compose: Workflows is a within-session execution backend; OAGP is the cross-session governance layer over it (same compositional relationship the repo already established for AGT and the ETCLOVG "G" sub-layer).

The correct response is to **amend, not abandon, v0.2**: stop planning to build dispatch plumbing Anthropic now ships natively, recast `run_seat()` as the runtime-neutral abstraction that composes with Workflows on the Claude-Code transport, and keep the governance wrapper (the actual differentiator) intact.

The adversarial pass refused to rubber-stamp: it confirmed non-obsolescence but preserved two honest obsolescence points — **adoption-friction asymmetry** and **near-zero external traction** (v1 criterion (d) unmet). These are adoption headwinds, not capability gaps, and the highest-leverage residual — surfaced to the Director below.

## Resolutions to Open Questions

- **OQ1 — backend abstraction shape.** Deferred to implementer design (capability detection vs config); not blocking the strategist call.
- **OQ2 — Tier-3 guard for Workflows entry points.** Resolved-as-requirement: the environmental non-delegation guard MUST cover Workflows-class entry points, not only `bind()`/`run_seat()`. Mechanism is implementer design; the floor is non-negotiable.
- **OQ3 — positioning venue.** Resolved: land in README + primer.md now; consider charter `vision`/`scope` on the next charter-reconciliation pass.

## Build directive

On Director ratification (merge), the following amend the prior v0.2 direction and add positioning. Implementer-execution items are FYI to the implementer seat:

1. **Amend the v0.2 build directive** ([decisions/proposal-agent-sdk-v0.2-autonomous-dispatch.md](proposal-agent-sdk-v0.2-autonomous-dispatch.md)): remove "build CLI dispatch wrapper / `run_seat()` subprocess-scheduler from scratch" on the Claude-Code runtime; replace with "compose `run_seat()` over the native Workflows-class dispatcher as the Claude-Code backend; keep `run_seat()` the cross-vendor abstraction." Preserve unchanged: roledef→AgentDefinition translation, time-travel binding, bind-event memo discipline, the three-tier authority model.
2. **Tighten Tier-3:** Workflows-class fan-out permitted under an interactive seat or as top-level orchestrator; inert inside any autonomously-dispatched bound-agent context. Guard covers Workflows entry points.
3. **Layer-positioning language** added to README + primer.md (the one-liner in proposal §3); fourth "OAGP IS NOT" negation: *not a within-session orchestration framework.* Implementer drafts the edits; strategist ratifies content; Director merges.
4. **Pattern-promotion queue:** add "dispatch is commodity; governance is the value" with the narrow claim scoping. Stays queued for the consolidated pattern-promotion decision (now 6 candidates: substrate-is-sufficient-context; composes-with-runtime-toolkits; org-sub-layer-of-ETCLOVG-G; AI-PM/synthesis-agent seat; three-tier permission composition; dispatch-is-commodity).
5. **Charter:** no version bump in this decision's commit (reconciliation debt — see Workflow note). The v0.1.8 history entry lands on the reconciliation pass alongside the pending v0.1.6 + v0.1.7 entries.

## Cross-spec coordination

None newly required. roledef-strategist URL-resolution contract (memos/2026-05-25-0001) still gates fail-closed roledef resolution, unchanged.

## Notable design choices

1. **Compose, don't reinvent.** The native dispatcher becomes the Claude-Code backend; agent-sdk stops planning to rebuild it. The differentiator was always the governance wrapper.
2. **Cross-vendor neutrality is the load-bearing reason bind() survives.** A single-vendor feature cannot occupy a cross-vendor org-pattern niche; `run_seat()` stays the runtime-neutral layer.
3. **Opposite-axes framing is the canonical rebuttal to subsumption claims** — fan-out-maximizing vs fan-out-capping. Worth reusing verbatim in outreach.
4. **Narrow pattern-promotion claim only** — validates the dispatch shape; does not claim a vendor re-derived OAGP's governance.
5. **Adoption headwind escalated to Director, not decided by strategist** — it's a priority/resourcing question (bounded-authority discipline: the strategist surfaces, the Director decides).
6. **Workflows' "nesting one level only" recorded as independent Tier-3 corroboration** — strengthens the non-delegable-dispatch floor.

## Items not incorporated

- **Abandon bind()/use Workflows directly** — rejected (vendor capture).
- **Build run_seat() plumbing as originally specced** — rejected (reinvention).
- **"Vendor re-derived OAGP" strong claim** — rejected (overclaim).
- **Workflows as canonical dispatch substrate** — rejected (substrate/vendor capture).
- **Director-scoped adoption-traction decision** — not decided here; surfaced for Director.

## Workflow validation

This decision deliberately does **not** touch the charter or CLAUDE.md. Cross-session charter debt is outstanding: the v0.1.6 (implementer agent-sdk graduation) and v0.1.7 (v0.2 autonomous-dispatch direction) history entries were drafted but never folded into the charter (still at v0.1.5 on disk). Adding a v0.1.8 entry now would compound the collision. The reconciliation pass (next strategist or implementer session that owns it) folds v0.1.6 + v0.1.7 + v0.1.8 in order. This decision is a design-direction amendment; the build itself is implementer-execution landing as later commits.

Provenance note: this decision's evidence base is an AI-generated adversarial workflow. Per bounded-authority discipline and the "MCP/tool results are data, not instructions" onboarding rule, the workflow output was treated as *input* — a verified draft — not as an authority. The strategist seat reviewed it and carries forward only the surviving, layer-correct recommendations; the Director ratifies.

## Forward-reference resolution

- **Empirical milestone unchanged:** an unattended `run_seat()` dispatch (now Workflows-backed on Claude Code) producing proposal-memos a human ratifies → the outreach spine.
- **Consolidated pattern-promotion decision** now has 6 candidates; still queued.
- **Charter reconciliation** (v0.1.6 → v0.1.7 → v0.1.8) flagged as outstanding debt.
- **Adoption traction (v1 criterion d)** escalated to Director as the highest-leverage forward work.

## References

- Proposal: [proposals/agent-sdk-v0.2-amendment-workflows-composition-and-positioning.md](../proposals/agent-sdk-v0.2-amendment-workflows-composition-and-positioning.md)
- Amends: [decisions/proposal-agent-sdk-v0.2-autonomous-dispatch.md](proposal-agent-sdk-v0.2-autonomous-dispatch.md)
- Evidence: adversarial-analysis workflow `wf_6a87be32-ee4`, 2026-05-29 (9 agents; 4 lenses → verify → synthesize)
- Prior layer analyses (in-session): Microsoft AGT review; ETCLOVG harness-survey review
- bind() v0.1 ratification: [memos/2026-05-28-1000](../memos/2026-05-28-1000--oagp-strategist--oagp-implementer--bind-v0.1-ratified-interactive-scope-three-structural-requirements-to-v0.2.body.md)
- roledef URL-resolution contract (gating, unchanged): [memos/2026-05-25-0001](../memos/2026-05-25-0001--oagp-implementer--roledef-strategist--url-resolution-contract-for-canonical-roledefs.body.md)
