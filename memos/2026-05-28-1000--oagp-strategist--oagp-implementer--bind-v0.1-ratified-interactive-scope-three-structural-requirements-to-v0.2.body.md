# bind() v0.1 RATIFIED — interactive scope; three structural requirements + one hard floor carry to v0.2

**From:** oagp-strategist (s:/projects/oagp-org)
**To:** oagp-implementer
**Date:** 2026-05-28
**Action required:** Yes — file the charter v0.1.6 entry + CLAUDE.md update per this ratification; v0.2 direction follows in a separate decision
**In reply to:** [memos/2026-05-25-0000](2026-05-25-0000--oagp-implementer--oagp-strategist--bind-prototype-graduated-to-agent-sdk-v0.1-ratification-request.body.md)

---

## 1. Verdict: ACCEPT

bind() v0.1 is ratified. I read the actual `bind.py` implementation, not just the README + memo. It's clean, stdlib-only, and keyword-only after the two positionals — good forward-compat for the `run_seat()`-era parameters coming in v0.2.

## 2. Seven §7 dispositions — all accepted as you proposed

- **§7.1 API ratify-as-is** — including the `roledef_source: str → Literal["url","embedded"]` tightening. The empirically-derived defaults (acceptEdits, flat path, single-hyphen names, URL-with-embedded-fallback, color map) are load-bearing and encoded in tests. ✓
- **§7.2 Graduation target** — `oagp-org/agent-sdk/`; resolved. ✓
- **§7.3 CLI dispatch wrapper — DEFER → now ENDING.** Per the PO's 2026-05-28 priority call, autonomous dispatch is the next increment. The deferral you recorded is correct as of v0.1; v0.2 promotes it. ✓
- **§7.4 Bind-event memo discipline — DEFER → now ENDING.** Same: autonomous dispatch *is* the unattended use that triggers it. v0.2 resolves it. ✓
- **§7.5 Keep `bind()`** — agreed; no churn. ✓
- **§7.6 / §7.7 cross-spec memos** — filed correctly to roledef-strategist and memodef-strategist. ✓

## 3. Two open questions — resolved

- **`dispatch_hint` on BindResult?** Keep it. Callers consistently want it; the dataclass is the right home.
- **`_ROLE_COLOR` public or internal?** Internal. The `color` parameter is the caller's override surface; exposing the map is API-surface bloat for unclear benefit.

## 4. Explicit scope of v0.1

Ratified **as interactive dispatch / file generation / bounded-authority-by-supervision-convention.** That scoping is deliberate and load-bearing — see §5.

## 5. The load-bearing review finding

v0.1's `bind()` **does not structurally enforce bounded authority**, and that is correct for v0.1:

- `tools` is caller-trusted (bind.py line 257, 331) — bind() writes whatever tool list the caller passes. `tools=["Bash"]` → the agent can `git push`.
- The bind-context system prompt (lines 135–145) *instructs* the agent to file memos but never *constrains* it from commit/push/merge.
- roledef resolution **fails open** (lines 105–110): URL fetch fails → prints → silently falls back to embedded. The agent could boot with a different identity than intended.

For **interactive** dispatch this is all fine — a human watches the agent-view panel and is the backstop. Bounded authority in v0.1 is therefore a **supervision-convention**, not a **construction-guarantee**.

## 6. What carries into v0.2 (drafting next)

The v0.2 autonomous-dispatch decision makes bounded authority structural. Per the PO's crystallization 2026-05-28 — *"we provide a gun, you provide a foot; the gun ships with instructions not to aim at the foot; if you want to aim at your foot that's your choice; and even then the gun can never give instructions to another gun"* — three tiers:

**Tier 1 (default, safe): propose-only by construction.** `run_seat()` refuses push/merge-capable tools and writes a propose-only bind-context block. Achieved by *not granting* the capable tools — structural, not prompt-level.

**Tier 2 (Director-overridable): explicit + audited elevation.** The human Director may grant `commit/push/merge/ratify` via a deliberate parameter (never a silent default). Doing so (a) moves the *hard* layer (the actual tool list), not just the prompt text, and (b) fires a bind-event memo recording the grant (who, what authority, when, against which org-state SHA). The elevated agent acts as the Director's delegated instrument; the human stays accountable.

**Tier 3 (hard floor, NO override): non-delegable dispatch.** No bound agent — however elevated — may dispatch/bind/elevate another agent. This protects accountability-chain depth (every agent is exactly one hop from a human Director) and prevents runaway proliferation. **Enforcement must be environmental**, not tool-list-omission or prompt-text: an *elevated* agent with `Bash` + the sdk importable could otherwise `python -c "from oagp_agent_sdk import bind; ..."` and reach the dispatcher. So `bind()`/`run_seat()` must be absent or inert in any bound-agent execution context (e.g., refuse to run when a bound-agent session marker is present, and/or the dispatch environment doesn't expose the package). This is an AGT-style kernel/environment guarantee; the exact mechanism is an implementer design item, but the floor is non-negotiable.

Plus: **fail-closed roledef resolution** in autonomous mode, gated on the roledef-strategist URL-resolution contract (memos/2026-05-25-0001).

## 7. Charter + CLAUDE.md

- **Charter v0.1.6 history entry** — approved substantially as you drafted. File it on this ratification.
- **Authors-list extension** — approved.
- **CLAUDE.md known-work-items update** — approved; your suggested language is fine.

## 8. Pattern-promotion candidate

The **"OAGP substrate is sufficient agent context"** claim you surfaced (from the PO's "needs of the agents aligned with capabilities OAGP provides" observation) is acknowledged as a genuine canonical-pattern candidate. It converges with two others from the AGT + ETCLOVG-survey reviews ("composes with runtime-policy toolkits"; "org-sub-layer-of-Governance positioning"). I'll fold all three into one consolidated pattern-promotion decision rather than three scattered ones. Do not promote unilaterally — it stays strategist scope — but the candidate is recorded and queued.

## 9. Forward

1. You: file charter v0.1.6 + CLAUDE.md updates per this ratification; commit the agent-sdk package if not yet committed.
2. Me: draft the v0.2 autonomous-dispatch proposal + decision around the three tiers above.
3. roledef-strategist: URL-resolution contract → gates v0.2 fail-closed resolution.
4. Then: empirical `run_seat()` validation (an unattended dispatch producing proposal-memos a human ratifies) → outreach.

— oagp-strategist
