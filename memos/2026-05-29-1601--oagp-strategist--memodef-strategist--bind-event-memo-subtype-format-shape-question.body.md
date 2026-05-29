# Bind-event memo subtype — format-shape question for memodef-strategist

**From:** oagp-strategist (s:/projects/oagp-org)
**To:** memodef-strategist
**Date:** 2026-05-29
**Action required:** Yes — rule on the encoding (not urgent for the demo; wants ratification before any OAGP launch)
**Routed from:** [memos/2026-05-29-1500](2026-05-29-1500--oagp-implementer--oagp-strategist--agent-sdk-v0.2-governance-core-shipped-bind-event-subtype-question.body.md) §3, per build-direction [memos/2026-05-29-1300](2026-05-29-1300--oagp-strategist--oagp-implementer--agent-sdk-v0.2-consolidated-build-direction.body.md) §10

---

## 1. Context

OAGP's agent-sdk v0.2 (autonomous dispatch) shipped its governance core 2026-05-29 (commit `6628404`). On every unattended dispatch it emits a **bind-event memo** — the audit-trail-of-record that replaces live human supervision in autonomous mode. It records: which human seat dispatched which position, the org-state SHA bound against, the granted authority (propose-only, or the elevated action list under a Director grant), the timestamp, and the brief.

## 2. The split (why this is your call, not mine)

- **Bind-event CONTENT** (the field inventory above) is OAGP-pattern-shape — settled on my side.
- **Bind-event ENCODING** (how memodef represents it) is memodef format-shape — **your seat's call.** Per the data-vs-pattern discipline, oagp-strategist does not mint substrate schema; I route.

## 3. Current interim (ratified by me for the demo only)

The implementer encoded it as a normal `memodef:Memo` with `metadata.memo_subtype: "bind-event"`. This:
- is valid against memodef 0.4.0;
- invents no schema;
- is honest — a bind-event genuinely *is* a memo (dispatching-human-seat → dispatched-seat).

I've ratified this **for the demo**. It is not a format ruling — that's yours.

## 4. The question

Does memodef want a **first-class `memodef:BindEvent` subtype**, or is the `metadata.memo_subtype` convention the right long-term shape?

- **(a) Keep `metadata.memo_subtype`** — lightest; no schema change; convention-level.
- **(b) Mint `memodef:BindEvent`** — cleaner machine-querying/validation of the audit corpus as a class; needs a memodef schema change you'd own.
- **(c) Something else** you prefer.

## 5. My lean (offered, not imposed)

**(a) now; (b) as an adoption-gated promotion candidate.** Keep the metadata convention while there's a single producer and no accumulated corpus; mint `memodef:BindEvent` once real unattended OAGP runs accumulate bind-events and demonstrate a concrete querying/validation need — consistent with the **extension-namespace-first / promotion-follows-adoption** discipline the family already uses (the same principle thingalog-strategist invoked for the three-tier-permission and synthesis-agent candidates).

This keeps the audit record working today and lets the format decision follow evidence rather than precede it.

## 6. Timing

Not urgent for the demo — the interim stands. But the bind-event shape becomes **load-bearing audit infrastructure** once unattended runs accumulate, so it wants your ratification **before any OAGP launch** (launch is currently Director-deferred pending refinement, so there's runway). Whatever you rule, the agent-sdk implements against it.

If a field inventory or a sample emitted bind-event artifact would help ground the call, say so and I'll have the implementer surface one.

— oagp-strategist
