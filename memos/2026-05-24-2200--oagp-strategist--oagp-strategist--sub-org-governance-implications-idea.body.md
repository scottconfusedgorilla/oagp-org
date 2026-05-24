# Sub-org governance implications -- idea memo for forward analysis cycle

**From:** oagp-strategist (s:/projects/oagp-org)
**To:** oagp-strategist (institutional capture for the seat's history)
**Date:** 2026-05-24
**Action required:** No (forward-reference)

---

## 1. Why this memo

Filed per Director direction 2026-05-24 during `/oagp-init` design discussion:

> "Agreed, parameter, but I don't think that's MVP. Now, you should absolutely file that as an idea, but it has all kinds of implications (among others, that means that we now have a human down further in the org chart, what does that actually mean? Are they write-limited to only their subtree?"

The standalone-org case is `/oagp-init` MVP. The sub-org case — where the new org is structurally subordinate to a parent org — is forward work. This memo captures the implications while the design discussion is fresh so the future analysis cycle starts with the questions already enumerated.

## 2. The core question

OAGP currently assumes **one Director** at the top with bounded-authority discipline applying uniformly across the org. The sub-org case introduces a **second Director** (or sub-Director-equivalent) lower in the org chart. This is structurally novel; the existing OAGP model doesn't address it.

The meta-question lurking: **does OAGP want to be a hierarchical-governance pattern (sub-orgs allowed), or does it stay flat (each org standalone, with peer coordination as the only inter-org relationship)?**

Both shapes are coherent:

- **Flat (current empirical default).** Each org is standalone. Inter-org coordination is peer-to-peer via memos. Example: oagp-org and catdef-spec are peers structurally, even though oagp-org consumes catdef formats as recommended-canonical substrate.
- **Hierarchical (sub-org enhancement).** Orgs can contain sub-orgs. The parent-org Director is "above" the sub-org Director in some authority sense. Example use case: a company might want to have a parent "company-org" with sub-orgs for "product-team-A", "product-team-B", etc.

## 3. Open governance questions

If the hierarchical shape is pursued, these questions need answers:

1. **Authority topology.** Does the sub-org Director have full authority within their subtree, or is parent-org Director the ultimate ratifier? Possibilities: (a) Sub-org is fully sovereign within its subtree; parent-org Director is a peer who happens to host them; (b) Parent-org Director is final-tiebreaker on everything including sub-org decisions; (c) Tiered: sub-org Director ratifies within scope, parent-org Director ratifies cross-subtree or parent-affecting decisions.

2. **Override.** Can parent-org Director override sub-org decisions? Under what circumstances? Edge cases: red-line violations, security incidents, compliance issues, dispute resolution.

3. **Merge gating.** If the sub-org has its own repo (or sub-folder in the parent repo): who ratifies merges? Sub-org Director alone? Sub-org Director with parent-org countersign for certain types of changes? Cross-cutting concerns (changes that affect parent-org artifacts) probably need parent ratification.

4. **Write-limits.** Per Director's question: *"Are they write-limited to only their subtree?"* Likely yes by default — sub-org Director has write access to sub-org/ subtree, read-only to parent and sibling subtrees. Edge cases: cross-subtree memos must be possible (one sub-org sends FYI memo to another); is that a write into the recipient's `memos/`, or a write into the sender's `memos/` that the recipient reads?

5. **Cross-subtree visibility.** Can sub-org A see sub-org B's institutional history? By default? With permission? Privacy-shape options: (a) Default open within parent-org boundary; (b) Default closed with opt-in sharing; (c) Per-artifact visibility flags.

6. **Sub-org creation chain.** Can a sub-org create its own sub-sub-orgs, recursively? Or is the hierarchy capped at depth-1? Practical: most adoption stories don't need depth > 1, but the substrate model should be explicit either way.

7. **Strategist-seat topology.** Do sub-orgs have their own strategist seats, or do they inherit from the parent-org strategist? If they have their own, do those strategists report-to the parent-org strategist, or to their sub-org Director directly?

8. **Cross-org coordination conventions.** The current convention (memos to/from peer strategists) assumes peer relationships. Sub-org relationships aren't peer-shaped; new conventions needed.

9. **Governance-change governance.** If the parent-org changes its CLAUDE.md or charter, do sub-orgs inherit the change automatically, or does each sub-org ratify the inheritance separately?

## 4. Why this matters now

Standalone-org is the immediate need for `/oagp-init` MVP. The sub-org case is forward work BUT worth capturing in this memo for three reasons:

1. **Director's question landed at the right time** (during /oagp-init design). The questions are easier to enumerate when the standalone-org case is fresh in working memory.
2. **The hierarchical shape might surface naturally** as adoption grows (e.g., a large org adopting OAGP and wanting team-level sub-structure).
3. **The substrate model should be explicit** about whether hierarchy is allowed; ambiguity is worse than either flat-only or hierarchical-with-rules.

## 5. Not addressed by this memo

This is an idea memo, not a proposal. It captures the questions; it does NOT propose answers. The future analysis cycle that takes up sub-org governance will need:

- A proposal artifact enumerating design alternatives for each question above
- Director ratification of the chosen shape
- SKILL.md update for `/oagp-init` adding sub-org parameter handling
- Possibly: an `/oagp-init-sub-org` separate skill if the workflow diverges enough

## 6. Standing posture

Not blocking. Standalone-org `/oagp-init` proceeds as MVP. Sub-org enhancement is forward work for a future analysis cycle. When that cycle starts, this memo is the input artifact.

— oagp-strategist
