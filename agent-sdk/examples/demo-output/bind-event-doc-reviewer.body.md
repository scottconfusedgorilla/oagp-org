# Bind-event: doc-reviewer

**From:** director (dispatching human's seat)
**To:** doc-reviewer (dispatched seat)
**Dispatched:** 2026-05-29T16:00:00
**Tier:** 1 (propose-only)
**Org-state SHA:** 53fb190230d98c9d6b71ea092ea5898f7ef97f7c

---

## Grant

Propose-only. No commit/push/merge/tag/release capability granted; the agent is constructed without Director-capable tools. Output is draft files a human reviews and commits.

## Roledef

- id: doc-reviewer
- version: 0.1.0
- source: embedded

## Brief

# Documentation review engagement (propose-only demo)

Target document: s:/Projects/oagp-org/agent-sdk/README.md
Engagement workspace: s:/Projects/oagp-org/agent-sdk/examples/demo-output/

Read the target README fully. Produce a concrete improvement proposal per your
output contract and WRITE it to:
  s:/Projects/oagp-org/agent-sdk/examples/demo-output/review-proposal.md

Quote the exact passage for every proposed change. Group by severity
(blocking / improvement / nit). Propose only -- do NOT edit the README itself.
Keep it focused: 4-8 concrete proposals is plenty. Stop when the proposal is written.


---

_Tier-3 floor: this agent cannot dispatch, bind, or elevate another agent. Enforced environmentally; no override exists._

_Emitted by oagp_agent_sdk.run_seat() on autonomous dispatch._
