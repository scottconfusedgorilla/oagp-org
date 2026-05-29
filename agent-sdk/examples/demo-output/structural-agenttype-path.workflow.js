export const meta = {
  name: "oagp-seat-doc-reviewer",
  description: "OAGP autonomous bound-agent dispatch: doc-reviewer (Tier-1, propose-only). Composes over the native Workflows dispatcher via agentType so the bound toolset (the structural authority bound) is enforced.",
  phases: [{ title: "Engage", detail: "doc-reviewer runs its bound engagement" }]
};

// Tier-3 note: the bound agent is dispatched via agentType, inheriting the
// tools: frontmatter of .claude/agents/doc-reviewer.md (the hard authority
// layer). The OAGP_BOUND_AGENT env marker cannot be injected into a
// workflow-spawned subagent; the Tier-3 non-delegable floor for this path
// therefore rests on PACKAGE-ABSENCE (oagp_agent_sdk must not be importable in
// the dispatch environment) plus the bound toolset. See README + the
// implementer status memo for the coordination finding.

phase("Engage");
const BRIEF = "# Documentation review engagement (propose-only demo)\n\nTarget document: s:/Projects/oagp-org/agent-sdk/README.md\nEngagement workspace: s:/Projects/oagp-org/agent-sdk/examples/demo-output/\n\nRead the target README fully. Produce a concrete improvement proposal per your\noutput contract and WRITE it to:\n  s:/Projects/oagp-org/agent-sdk/examples/demo-output/review-proposal.md\n\nQuote the exact passage for every proposed change. Group by severity\n(blocking / improvement / nit). Propose only -- do NOT edit the README itself.\nKeep it focused: 4-8 concrete proposals is plenty. Stop when the proposal is written.\n";
const result = await agent(BRIEF, {
  agentType: "doc-reviewer",
  label: "doc-reviewer",
  phase: "Engage",
});
return { agent_name: "doc-reviewer", tier: 1, granted_authority: [], result };
