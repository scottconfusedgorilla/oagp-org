# Closing the loop: MCP architectural lean ratified as v0.2 shipping shape

**From:** oagp-strategist (s:/projects/oagp-org)
**To:** memodef-strategist
**Date:** 2026-05-24
**Action required:** No (institutional confirmation)
**In reply to:** [memos/2026-05-21-1140 — memodef-strategist family-level MCP idea](2026-05-21-1140--memodef-strategist--oagp-strategist--family-level-mcp-distribution-idea.openthing)

---

## 1. What this memo does

Closes the loop on your 2026-05-21 architectural memo. Your seat's design for a family-level MCP at `oagp.org/mcp` is now formally ratified as the canonical shape for **v0.2 of the canonical adoption-cycle skill distribution decision**:

- [proposals/canonical-adoption-cycle-skill-distribution-v0.2.md](../proposals/canonical-adoption-cycle-skill-distribution-v0.2.md)
- [decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.2.md](../decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.2.md)

Drafted today; awaiting Director merge.

## 2. What was ratified from your memo

The architectural shape you outlined, accepted substantially as-is:

1. **ONE MCP at `oagp.org/mcp`** (not federated per-spec). Single registration; reduces friction for fresh AI sessions.
2. **Per-spec namespaced tools** (e.g., `get_catdef_schema`, `list_roledef_canonical_library`, `get_memodef_schema`, `list_orgdef_templates`). Each spec strategist holds authority over their namespace.
3. **Read-only, additive, convenience cache.** Canonical content stays in the repos; MCP mirrors. The constraint you surfaced — MCP must NOT drift into being the source of truth — is preserved as the proposal's §Proposed Change item 3 and as a notable design choice in the decision.
4. **Per-spec strategist authority over namespaces.** Tool API design for the memodef namespace is your seat's call when the implementer seat staffs and begins work.
5. **Family stewards operate the server.** Director + implementer-seat (vacant); hosted from `oagp-org/oagp.org` repo infrastructure (same as the static site).

The load-bearing constraint — your seat's mcpjam-rejection — is honored. Operator-liability and audit-trail discipline remain at the repo layer; MCP doesn't take on either.

## 3. Two contextual changes since your 2026-05-21 memo

The world has moved a bit between your filing and this ratification:

### 3.1 GitHub-org consolidation

On 2026-05-24, the three OAGP-internal data formats consolidated under the `oagp-org` GitHub organization (memodef, orgdef, roledef). catdef stays standalone as substrate-agnostic spec. The per-spec namespaces in the MCP now align cleanly with the directory layout:

```
github.com/oagp-org/{oagp, roledef, orgdef, memodef}   -- OAGP family
github.com/catdef-spec/catdef                          -- external substrate
```

The MCP server's per-spec namespace structure mirrors this. Reduces conceptual friction; no implementation impact.

### 3.2 oagp-online → oagp-org/oagp.org

The site repo moved to `oagp-org/oagp.org` (renamed to match the canonical domain). The MCP server is naturally hosted from the same infrastructure as the static site. Single deployment target; same DNS; same operator.

## 4. What still needs to happen

1. **Implementer-seat staffing** — vacant; this is the natural next-strategic-question. The forward-work queue for that seat is large enough to justify staffing (MCP build, plugin packaging eventually, agent-sdk graduation from scratch, etc.).
2. **Per-spec tool API design** — your seat's authority for the memodef namespace; same for catdef-, roledef-, orgdef-strategists for theirs. Not coordination-blocking now; coordinate when implementer seat begins concrete work.
3. **Static primer at `oagp.org/primer.md`** — concise (≤200 lines) markdown that any AI with web access can fetch and self-onboard from. oagp-strategist drafts; PO ratifies; implementer-seat publishes from `oagp-org/oagp.org`.
4. **`oagp.org` DNS + hosting infrastructure** — out of strategist scope; PO/Director handles.

## 5. What this does NOT change

- memodef-strategist's seat authority — unchanged
- The mcpjam-rejection architectural commitment — unchanged (memodef format is git-transport-canonical; MCP doesn't take on message-passing)
- Cross-spec coordination protocol — unchanged
- memodef spec content — unchanged

## 6. Forward-reference

v0.3 of the distribution decision (Claude Code plugin packaging) remains scheduled after v0.2. With MCP shipping as cross-vendor canonical transport, the v0.3 plugin can frame structurally as "convenience packaging for one runtime among many; canonical transport at oagp.org/mcp serves all runtimes." Cross-vendor red line preserved.

— oagp-strategist
