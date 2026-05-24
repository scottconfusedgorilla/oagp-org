---
name: oagp-bootstrap
description: |
  Use this skill when a Product Owner wants to convert an existing
  project into OAGP shape (catdef → roledef → orgdef → memodef →
  transcriptdef). The skill surveys the project, proposes an org
  charter as a ratifiable artifact, and instantiates the substrate
  folders + initial memos once the PO approves.

  Activate when the user says any of: "make this OAGP-shaped",
  "bootstrap OAGP", "add OAGP to this project", "convert this to
  OAGP", or asks about OAGP adoption for an existing codebase.

  The companion skill is /oagp-onboard-<orgname>, which a fresh AI
  peer uses to join an already-bootstrapped org. Bootstrap is the
  founding side; onboard is the joining side. Together they are the
  complete OAGP adoption cycle.
---

# /oagp-bootstrap

You are being invoked to bootstrap an existing project into OAGP shape. This is a substantial, multi-phase task that must be done with the discipline of **propose-don't-impose** — the Product Owner is the only one who can decide the org's identity. Your job is to make adoption cheap, not to make the decision.

**Note for invokers:** When pasting this skill content into a fresh AI session, replace "an existing project" in the opening sentence above with the specific project name (e.g., "the dangerstorm project", "the caliper project"). The skill template is generic; the invocation should be project-specific so the AI doesn't have to guess which project is the target. This parameterization is the invoker's responsibility, not the AI's.

OAGP reference: [oagp.org](https://oagp.org) (when canonical). For now, the empirical reference implementation is `github.com/scottconfusedgorilla/thingalog`. **When fetching from the reference, read `org/`, `CLAUDE.md`, `memos/`, `proposals/`, and `skills/` for canonical patterns. Do NOT read `transcripts/` — those are per-seat conversation records specific to the operating org and not part of the canonical reference shape.** One transcript may be skimmed to learn the format; reading the full set is unnecessary and exposes operational specifics.

---

## Five Phases

### Phase 1 — Survey (read-only)

Read everything available about the project to form a working model of its current shape. Sources, in approximate order of priority:

- `README.md`, `ARCHITECTURE.md`, `CONTRIBUTING.md`, anything in `docs/`
- `CLAUDE.md` if present (existing constitutional commitments)
- Recent commit history (last ~50 commits): what's been shipping, by whom?
- Recent PR descriptions: how are decisions captured?
- Issue tracker if accessible: what failure modes are being tracked?
- Package config (`package.json`, `pyproject.toml`, `Cargo.toml`, etc.): tech stack
- Any existing `org/`, `memos/`, `proposals/` folders (the project may already have *some* OAGP shape — respect what's there)

From these sources, form a working model of:

- **Project mission**: what is this project FOR?
- **Project scope**: what is this project NOT?
- **Implicit positions**: who works on this and in what capacity? Are there roles being filled (PM, lead engineer, designer, AI peer) even if not formalized?
- **Implicit values**: what does observable practice (test discipline, code-review patterns, commit message style) tell you about what this project cares about?
- **Implicit red lines**: what does CLAUDE.md (if present) or repeated enforcement (in PR comments, in CI requirements) tell you is non-negotiable?
- **v1 / launch criteria**: what does "shipped" mean here? Is there a roadmap? A success metric?
- **Recent strategic decisions**: what big architectural calls have been made recently? Why?

**Do NOT yet create any files or folders. This phase is read-only.**

If you don't have repo access in your current runtime, ask the PO to share the repo URL or paste relevant documents as text. Adapt Phase 1 to whatever input is available.

---

### Phase 2 — Propose (draft a proposal artifact)

Produce a draft orgdef in the canonical opencatalog shape, filed at:

```
proposals/oagp-bootstrap-<YYYY-MM-DD>.md
```

The draft must:

- **Capture what you observed in Phase 1**, with citation to source files where possible ("CLAUDE.md line 14 establishes...", "commit messages from the last 30 days consistently use 'fix:' / 'feat:' style suggesting...")
- **Mark every section with a confidence label**: `[HIGH CONFIDENCE]`, `[INFERRED]`, or `[NEEDS PO INPUT]`
- **Use explicit "I observed X; I infer this means Y; please confirm or correct" framing** for everything inferred
- **Propose positions with status (staffed/vacant)** but **DO NOT auto-staff anyone** — the PO decides incumbents. You can propose that the PO's GitHub identity (extracted from recent commits) is the staffed Product Owner, but that proposal needs PO confirmation
- **Propose values with rationale** tied to observed practice ("This project's CI requires 100% test coverage on new code, suggesting `test-discipline-as-value`")
- **Propose red lines defensively** — better to propose more red lines than fewer; PO can remove. Examples to consider proposing if the evidence supports them: tenant isolation, no destructive operations without authorization, accessibility floor, content moderation, no AI runtime lock-in
- **Propose v1 success criteria** as best-effort with explicit "PO must ratify or revise" flag
- **Include a "What I couldn't determine" section** explicitly listing every field where you needed PO input

The proposal artifact follows the canonical orgdef shape (see Thingalog's `org/thingalog-organization.opencatalog` as the empirical reference). Field structure:

```json
{
  "catdef": "1.4",
  "orgdef": "1.0.0",
  "type": "orgdef:Organization",
  "id": "<proposed-id>",
  "name": "<proposed-name>",
  "version": "1.0.0",
  "mission": "[INFERRED] ...",
  "vision": "[NEEDS PO INPUT] ...",
  "scope": "[INFERRED] ...",
  "governance_model": "[INFERRED] ...",
  "values": [
    { "name": "...", "description": "...", "rationale": "...", "_confidence": "[INFERRED]" }
  ],
  "red_lines": [
    { "rule": "...", "rationale": "...", "_confidence": "[NEEDS PO RATIFICATION]" }
  ],
  "recommended_patterns": { /* propose defensively */ },
  "v1_success_criterion": "[NEEDS PO INPUT] ...",
  "relationships": [ /* propose minimal: PO → Implementer, etc. */ ],
  "items": [
    { "type": "orgdef:Position", "id": "product-owner", "status": "staffed",
      "incumbent": "[INFERRED from commits: ...]" },
    { "type": "orgdef:Position", "id": "implementer", "status": "[NEEDS PO INPUT]" },
    /* other positions discovered */
  ]
}
```

**After filing the proposal, STOP.** Report to PO:

- The proposal is filed at `proposals/oagp-bootstrap-<date>.md`
- You need PO review + ratification before proceeding
- List the key unknowns that need PO input
- Briefly summarize what you observed (3-5 bullets)

---

### Phase 3 — Ratify (PO does this; you wait)

The PO reads the proposal, corrects and amends, ratifies. You don't act in this phase. If the PO asks clarifying questions or asks you to revise the proposal, do so — but **do not proceed to Phase 4 without explicit "yes, instantiate this" from the PO**.

Revisions in this phase may include:
- Removing positions you proposed that don't actually exist
- Adding positions you missed
- Renaming things (the PO's vocabulary may differ from your inferred terminology)
- Tightening or loosening red lines
- Specifying v1 success criteria the PO had in mind but didn't document
- Filling in `[NEEDS PO INPUT]` fields

The proposal artifact is the working document. Revise it in place. When the PO says "ratify and instantiate," proceed to Phase 4.

---

### Phase 4 — Instantiate (only on PO ratification)

Create the substrate. The order matters:

**a) Create the canonical org charter:**
```
org/<orgname>-organization.opencatalog
```
Content: the ratified orgdef. All `[INFERRED]` / `[NEEDS PO INPUT]` confidence markers stripped (since the PO has now ratified). Should be valid `orgdef:Organization` JSON.

**b) Create the substrate folders:**
```
memos/      (empty, ready for first memo)
proposals/  (existing — the bootstrap proposal lives here)
transcripts/ (empty, ready for first transcript)
```

For each folder that would be empty at commit time, **add a `.gitkeep` file** so git tracks the folder. Otherwise empty folders won't be committed and the substrate won't be reproducible from clone. Phase 4d will add the first memo to `memos/`, so `memos/.gitkeep` may not be needed; `transcripts/.gitkeep` typically is.

**c) Update or create CLAUDE.md:**

If `CLAUDE.md` exists, **augment it; do not overwrite**. Add the ratified constitutional commitments (red lines as MUSTs, values as principles) at the end, with a separator header (`## OAGP-shape commitments (added <date>)`).

If `CLAUDE.md` does not exist, create it with the ratified content. Keep it concise — CLAUDE.md is the constitutional layer, not a project manual.

**d) File the bootstrap memo:**

Path:
```
memos/<YYYY-MM-DD>-<HHMM>--product-owner--<orgname>-strategist--oagp-bootstrap-ratified.openthing
```

The memo (envelope + body_ref sibling `.body.md`) documents:
- What was proposed
- What was ratified (including changes from the proposal)
- Date the org committed to OAGP shape
- Reference to the proposal artifact at `proposals/oagp-bootstrap-<date>.md`
- A "next steps" section pointing future participants at `/oagp-onboard-<orgname>` for the joining side

The memo is `action_required: false` (it's institutional capture). It's `from: product-owner` to acknowledge the PO ratification; `to: <orgname>-strategist` because that's the receiving seat (vacant or staffed, the memo is for that seat's history).

**Why a memo to a (possibly vacant) Strategist seat?** The OAGP convention is that org-shape decisions land in the relevant Strategist seat's institutional history, regardless of staffing status. When the seat eventually staffs (if it does), the incoming AI peer reads its inbox and finds this ratification record waiting — establishing on day zero what was decided, when, by whom, and what the org's constitutional commitments are. If the seat never staffs, the memo remains as the artifact of record for any future participant reading the `memos/` folder. The decision belongs to the SEAT, not to the incumbent; the memo persists either way.

**e) Commit + push (with explicit PO authorization for the push):**

```
git add org/ memos/ proposals/ transcripts/ CLAUDE.md
git commit -m "OAGP-bootstrap: instantiate org charter + substrate folders"
git push origin <branch>
```

Confirm with the PO before pushing. Pushes are PO-authorized actions per the bounded-authority pattern that OAGP uses.

**If no remote is configured** (e.g., on a test fork created specifically to validate the bootstrap workflow): commit only and report "no remote; push step N/A — PO will configure a remote later if needed." Do not attempt to add a remote without explicit PO direction. The bounded-authority discipline applies regardless of remote state.

---

### Phase 5 — Hand-off

Report to PO with a summary:

- OAGP shape is instantiated. Commit SHA: `<sha>`.
- To onboard a fresh AI peer (including yourself in a new session), use `/oagp-onboard-<orgname>`.
- To staff a position, the PO can directly authorize an incumbent, OR an AI peer can self-onboard and file an application memo for evaluation.
- The org charter is at `org/<orgname>-organization.opencatalog`.
- The org is now ready for OAGP participation. Future memos go in `memos/`, proposals in `proposals/`, transcripts in `transcripts/`.

Optional next-step suggestions (only if the PO asks for them):
- Set up an `/oagp-onboard-<orgname>` shortcut/skill for the PO's preferred runtime (mirror the Thingalog example)
- Draft the first proposal in `proposals/` (whatever architectural work is in flight)
- Identify candidate fills for vacant positions

---

## Discipline (load-bearing)

These constraints are what distinguish "AI peer bootstrapping a project safely" from "AI peer imposing an organizational structure on a project."

**1. Propose-don't-impose.** You are an AI peer arriving at someone's existing project. Your job is to make adoption CHEAP by drafting a solid first cut. The human PO is the only one who can DECIDE the org's identity. Never instantiate substrate folders or commit org artifacts without explicit PO ratification.

**2. Humility about inference.** Your Phase 1 reading produces inferences, not facts. Mark them as such. The PO knows their project better than you do.

**3. Preserve, don't overwrite.** If `CLAUDE.md` exists, augment it. If the project already has some OAGP shape (`memos/` exists, say), respect it; propose to align with it, not supersede it. If positions are already informally filled, name them as such — don't pretend the slate is clean.

**4. Stop at each phase boundary.** Each phase has a specific checkpoint where you must report and wait. Do not bundle phases. Do not auto-proceed from Phase 2 to Phase 4 because "the PO obviously wants it." Wait for the explicit "instantiate" signal.

**5. The bootstrap itself is OAGP-shaped.** Propose → ratify → apply. Same protocol as everything else in OAGP. The first memo filed in the new org is the bootstrap memo capturing what just happened. Self-instantiating.

**6. Push is PO-authorized.** Even when instantiating, the final `git push` requires explicit PO go-ahead. Bounded authority all the way through.

**7. Test on a fork before live.** If you (or the PO) want to test this skill on an existing project, fork the project first (per the org-state-fork-for-time-travel pattern). Bootstrap into the fork. Validate. Iterate. Only apply to the live repo once the workflow is proven.

---

## Transcript capture during bootstrap sessions

If the bootstrap session is being captured as a `memodef:Transcript` (via ccc-ninja, a C4C-capture equivalent, or a future cross-runtime equivalent), **the AI's role during the bootstrap does not map cleanly to any post-bootstrap position in the org being created.** During Phase 1-2 the AI is strategist-shaped (proposing); during Phase 4 it's implementer-shaped (instantiating). The transient role is some kind of "founding helper" that exists during adoption and retires at hand-off.

**Recommended transcript-position-tag:** `<orgname>-bootstrap-helper` or `<orgname>-bootstrap-strategist` rather than any of the org's permanent positions. The bootstrap session is a one-shot role; conflating it with a permanent staffed seat would confuse the seat's institutional history.

After Phase 5 hand-off, if the AI continues operating in the new org, it should re-tag (or rely on the harness to re-tag) future sessions against the actual staffed position (e.g., `<orgname>-implementer`).

This is a small OAGP-spec-level convention worth being explicit about; the bootstrap session is the moment where the org's positions don't exist yet, so the position-tagging primitive has to bend to accommodate.

---

## Adapting to runtime

This skill is designed to be portable across AI runtimes. The phase logic is invariant; the execution differs:

| Runtime | Phase 1 | Phase 4 instantiation |
|---|---|---|
| **Claude Code** | Direct filesystem read + git log | Direct file/folder creation + `git commit` + `git push` |
| **Claude-for-Chrome** | GitHub web UI navigation (with PAT for private repos) | Commit-via-web for each file; slower but works |
| **claude.ai (web)** | Discussion + paste-text input from PO | Produce file bundle for PO to commit manually |
| **ChatGPT / Gemini / non-Anthropic** | Same as claude.ai; whatever browse/read tools are available | Produce file bundle; PO commits |
| **Anything-else AI with web access** | Read the repo's public URLs | Same as above |

The minimum viable runtime: any AI that can read text (the PO pastes documents) and produce text (the proposal + the final files). The cross-vendor adoption story holds because OAGP's substrate is just files in a git repo — any AI peer can read them, any AI peer can propose them, the PO ratifies and commits.

---

## What this skill does NOT do

- It does not staff any position (PO decides incumbents)
- It does not commit pushes without PO authorization
- It does not propose changes to OAGP itself (that's `pattern_promotion_memo` work for oagp.org / orgdef-strategist, not bootstrap work)
- It does not migrate an existing project's data; only its organizational shape
- It does not assume project size or complexity — works for a 100-line script or a 100KLOC enterprise codebase, same protocol
- It does not require pre-existing OAGP knowledge from the PO; the proposal is designed to be PO-readable and ratifiable without spec-level depth

---

## References

- **Companion skill**: `/oagp-onboard-<orgname>` for the joining side of the adoption cycle
- **Empirical reference org**: `github.com/scottconfusedgorilla/thingalog` (look at `org/thingalog-organization.opencatalog` for canonical orgdef shape; `CLAUDE.md` for constitutional layer; `memos/` for inter-position communication pattern)
- **OAGP spec home**: [oagp.org](https://oagp.org) (when canonical)
- **Substrate stack**: catdef (schema-as-data) → roledef (role specs) → orgdef (org structure) → memodef (inter-position memos) → transcriptdef (per-seat reasoning records)
- **The time-travel property**: Forking an OAGP-shaped repo preserves the entire organizational context, not just code. See `memos/2026-05-19-2200--thingalog-strategist--thingalog-strategist--org-state-forks-as-time-travel-substrate.body.md` in the Thingalog repo.
