# Proposal: Canonical adoption-cycle skill distribution v0.2 — family-level MCP at oagp.org/mcp + substrate-neutral primer fallback

**Status:** Open (awaiting Director ratification via merge)
**Author:** oagp-strategist <oagp-strategist@oagp.org>
**Created:** 2026-05-24
**Target version:** oagp-org v0.1.3 (history entry)
**Origin:**
- [memos/2026-05-21-1140 — memodef-strategist family-level MCP idea](../memos/2026-05-21-1140--memodef-strategist--oagp-strategist--family-level-mcp-distribution-idea.openthing) — Director-floated 2026-05-21; memodef-strategist's architectural lean with shape worked out
- [decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.1.md](../decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.1.md) — v0.1 scheduled this as v0.2 ("substrate-neutral primer URL")
- Director direction 2026-05-24: "should we make it all available via MCP as well?"
- GitHub-org consolidation 2026-05-24 — three OAGP-internal -defs now under `oagp-org`; oagp-online moved to `oagp-org/oagp.org`. The single-server-multi-spec MCP architecture is now naturally hostable from one place.

## Summary

Ship a canonical MCP server at **`oagp.org/mcp`** (read-only, additive convenience cache; per-spec namespaced tools) as the substrate-neutral canonical distribution mechanism. Plus **`oagp.org/primer.md`** as a static fallback for runtimes without MCP support. Together, these collapse adoption friction across every AI runtime: MCP-supporting runtimes connect via tool calls; web-only runtimes fetch the primer URL.

## Motivation

1. **Cross-vendor canonical access at the transport layer.** MCP is multi-vendor (Anthropic-led but being adopted broadly). A canonical MCP endpoint at `oagp.org/mcp` lets any AI runtime with MCP support fetch OAGP semantics with zero friction — no clone, no install script, no plugin marketplace.

2. **Substrate-neutral by design.** MCP is transport-neutral; not Anthropic-exclusive. v0.2 explicitly satisfies the cross-vendor red line in a way v0.1 (Claude-Code-specific scripts) and the future v0.3 (Claude Code plugin) cannot.

3. **Empirical friction signal.** The 2026-05-24-0905 memo documented PO hitting cross-machine install friction even on the v0.1 path. Non-Claude-Code runtimes have worse friction (no skill primitive). MCP collapses both cases.

4. **Architectural shape already worked out.** memodef-strategist's 2026-05-21 architectural lean (one MCP, per-spec namespaced tools, read-only convenience cache, per-spec strategist authority over namespaces, family stewards operate the server, repos remain canonical source of truth) is sound and is ratified here.

5. **Consolidation under oagp-org makes this practical.** Pre-consolidation, federated per-spec MCPs (catdef.org/mcp, roledef.org/mcp, ...) was the natural shape but defeated the friction-reduction motivation. Post-consolidation, a single MCP at oagp.org with per-spec namespaces is the obvious architecture.

## Proposed Change

1. **One MCP at `oagp.org/mcp`.** Not federated per-spec. Single registration, multiple namespaced tool groups. Pattern matches openbraid (one MCP, multiple namespaced tools) and thingalog (one per-catalog MCP).

2. **Per-spec namespaced tools.** Indicative shape (specific tool design is per-spec-strategist's call):
   - **catdef namespace:** `get_catdef_schema`, `list_catdef_conformance_fixtures`
   - **roledef namespace:** `get_roledef_schema`, `list_roledef_canonical_library`, `get_roledef(name)`
   - **orgdef namespace:** `get_orgdef_schema`, `list_orgdef_templates`, `list_orgdef_canonical_orgs`, `get_orgdef(id)`
   - **memodef namespace:** `get_memodef_schema`, `get_memodef_transcript_schema`
   - **oagp namespace:** `list_oagp_skills`, `get_oagp_skill(name)`, `get_oagp_charter`, `get_oagp_pattern_doc`

3. **Read-only, additive, convenience cache.** Canonical content stays in the repos at `github.com/oagp-org/{oagp, catdef, roledef, orgdef, memodef}`. The MCP server reads from those repos (via GitHub API or local mirror) and exposes structured access. **The MCP must NOT drift into being the source of truth.** This is the load-bearing constraint memodef-strategist surfaced; it preserves operator-liability + audit-trail discipline and matches memodef's own mcpjam-rejection rationale.

4. **Per-spec strategist authority over namespaces.** Each spec strategist designs their slice's tools, decides what's exposed, and ratifies tool API changes for their namespace.

5. **Family stewards operate the server.** Director + implementer-seat (vacant) administer the production deployment. Hosting at `oagp.org/mcp` shares infrastructure with the static site at `oagp-org/oagp.org`.

6. **Static fallback at `oagp.org/primer.md`.** A concise (≤200 lines) markdown document any AI with web access can fetch and self-onboard from. Covers: what OAGP is, the substrate stack, where canonical content lives, how to engage via MCP for richer access. The primer is canonical too — same source of truth as the MCP.

7. **Cross-vendor framing in canonical docs.** README, charter, primer.md all enumerate MCP-supporting runtimes (Anthropic Claude, OpenAI ChatGPT when MCP-supported, Google Gemini when MCP-supported, Perplexity, etc.) and frame MCP as canonical transport (not Anthropic-exclusive).

## Backward Compatibility

- v0.1 install scripts continue to work; v0.2 is additive.
- Adopters using v0.1 don't need to switch; v0.2 provides the canonical cross-vendor path.
- Canonical content URLs (the GitHub repos under `oagp-org`) are unchanged; MCP reads from them.

## Conformance Tests

1. Any AI with MCP client support can connect to `oagp.org/mcp` and fetch canonical OAGP content via per-spec namespaced tool calls.
2. Any AI with web access can fetch `oagp.org/primer.md` as a self-onboarding bootstrap.
3. MCP endpoints are read-only — no tool exposes write access to any canonical artifact.
4. Every MCP tool response is sourced from a canonical repo under `oagp-org` (or `catdef-spec/catdef` for catdef-namespaced tools). The MCP doesn't synthesize content not present in the repos.
5. Per-spec tool namespaces are documented; tool API changes for a namespace require that spec's strategist's ratification.

## Alternatives Considered

1. **Federated per-spec MCPs** (catdef.org/mcp, roledef.org/mcp, ...). Rejected per memodef-strategist's 2026-05-21 read: defeats friction-reduction motivation; "means adding 4 MCP tools every time" for fresh AI sessions. Single endpoint with namespaces is the clearer win.

2. **Static URL only (`oagp.org/primer.md`, no MCP).** Works for any AI with web access but misses the structured-tool-call benefit MCP-native runtimes get. Rejected as canonical-only; included as fallback for non-MCP runtimes.

3. **MCP-as-source-of-truth (writes via MCP).** Rejected (centralization-creep red line + memodef-strategist's mcpjam-rejection rationale). Operator-liability concentrates if MCP becomes the canonical store; repos must remain canonical.

4. **Anthropic Marketplace-distributed MCP server.** Rejected as v0.2 — would re-couple to a single vendor. The point of v0.2 is canonical cross-vendor transport.

5. **Defer to a later version.** Rejected. The GitHub-org consolidation today unlocks the natural one-server architecture; the empirical friction signal is current; memodef-strategist's architectural lean is already drafted. Right time is now.

## Open Questions

- **OQ1 — Operator.** Who runs `oagp.org/mcp` operationally? Provisional: family stewards (Director + implementer-seat-when-staffed). Hosting from the same infrastructure as `oagp.org` static site (the `oagp-org/oagp.org` repo).
- **OQ2 — Auth / rate-limiting.** Open read access (no auth) is the natural fit for a canonical content cache. Provisional: open + reasonable per-IP rate limits.
- **OQ3 — Cache invalidation.** MCP server mirrors repo content; how does it refresh? Provisional: repo-update-triggered invalidation (GitHub webhook on push to main), plus periodic full-refresh fallback.
- **OQ4 — Tool API versioning.** As spec versions evolve, do tools version? Provisional: spec versions exposed in tool responses; tool API itself stable except by per-spec-strategist ratification.
- **OQ5 — Implementation language / framework.** Implementer-seat's call when staffed. Recommend: thin proxy (mostly fetches from GitHub API + repo content; no heavy logic). Existing MCP server frameworks in Python or Node both work.

## Cross-spec coordination

- **Memo to memodef-strategist** confirming v0.2 ratifies their 2026-05-21 architectural lean. Closes the loop on that inbox item.
- **Per-spec strategist authority** over their tool namespaces — call out in README and in any future implementer documentation.
- **No format-shape implications.** No -def-spec schema changes required.
