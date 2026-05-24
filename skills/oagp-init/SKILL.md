---
name: oagp-init
description: |
  Use this skill when a Product Owner wants to create a NEW OAGP-shaped
  organization from scratch (no existing project to convert). The skill
  elicits org identity by interviewing the PO, proposes an org charter
  as a ratifiable artifact, and instantiates the substrate (charter,
  CLAUDE.md, README.md, memos/, proposals/, decisions/, transcripts/,
  skills/) inside a folder of the PO's choosing once they approve.

  Activate when the user says any of: "create a new OAGP org",
  "start a new OAGP-shaped project from scratch", "found a new OAGP
  org", "let's spin up an oagp-org-shaped project for X", or asks
  about creating an OAGP-shaped org from a blank slate.

  The companion skill is /oagp-bootstrap, which converts an EXISTING
  project into OAGP shape. Bootstrap is the conversion (existing
  project) side; init is the founding (blank slate) side. Together
  they cover both starting paths into OAGP.

  Folder-only operation: the skill creates an OAGP-shaped folder; git
  is optional. PO chooses whether to git-init the folder afterward.
  Both shapes (folder-only and git-backed) are valid OAGP-shaped orgs.
---

# /oagp-init

You are being invoked to create a new OAGP-shaped organization from scratch. There is no existing project to survey; you elicit the org's identity by interviewing the PO. This is a substantial, multi-phase task that must be done with **propose-don't-impose** discipline — the PO is the only one who can decide the org's identity. Your job is to make founding cheap, not to make the decision.

OAGP reference: [oagp.org](https://oagp.org) (when canonical). For now, the empirical reference implementations are [github.com/oagp-org/oagp](https://github.com/oagp-org/oagp) (this canonical home; mature OAGP-shaped org) and [github.com/scottconfusedgorilla/thingalog](https://github.com/scottconfusedgorilla/thingalog) (substrate-progenitor org that led to OAGP; mature catdef-shaped catalog).

---

## Five Phases

### Phase 1 — Elicit (interview the PO)

Ask the PO, one topic at a time (or in a guided form if they prefer):

1. **Project name / org id.** What's the canonical id? (short-kebab-case; will be used in `<orgname>-organization.opencatalog`)
2. **Mission.** What is this org FOR? In one or two sentences.
3. **Scope.** What is this org NOT? What's explicitly out of scope?
4. **Initial positions.** Who's involved? At minimum: who's the Director (the human ratifier)? Are there AI roles already in mind (strategist, implementer, etc.)? Mark staffed vs. vacant.
5. **Values.** What are the load-bearing commitments? (1-5 named values, each with a description + rationale)
6. **Red lines.** What's non-negotiable? (1-5 named red lines, each with a rule + rationale)
7. **v1 success criteria.** What does "this org has reached v1" mean concretely?
8. **Relationships.** Cross-org coordination? Sibling orgs, dependent orgs, governance reports-to?
9. **Folder location.** Where on disk should this org live? (e.g., `s:/projects/<orgname>` or `~/projects/<orgname>`). PO chooses any folder; doesn't need to be a git repo.
10. **Initial work queue (optional).** Anything that should be filed in `memos/` as forward-reference on day one?

For each item, accept the PO's answer at face value (this is their org); push back ONLY if you spot internal contradictions (e.g., a red line that conflicts with a stated value). Mark anything ambiguous or deferred as `[NEEDS PO INPUT]` in the proposal artifact.

**Do NOT yet create any files or folders. This phase is interview-only.**

---

### Phase 2 — Propose (draft the org charter)

Produce a draft `orgdef:Organization` artifact in the canonical opencatalog shape. The artifact is the PO's working document for review.

The draft must:

- **Capture the elicited content** verbatim where the PO was specific; explicit `[INFERRED]` markers where you extended their answer with reasonable defaults; explicit `[NEEDS PO INPUT]` where they deferred or didn't address.
- **Use the canonical orgdef:Organization shape** (mission, vision, scope, governance_model, values, red_lines, recommended_patterns, v1_success_criterion, relationships, items, metadata) — see [github.com/oagp-org/oagp/blob/main/org/oagp-organization.opencatalog](https://github.com/oagp-org/oagp/blob/main/org/oagp-organization.opencatalog) as the empirical reference.
- **Position items: Director (staffed) + any AI roles the PO surfaced.** Default AI roles to `status: vacant` with `description` explaining seat scope. Do NOT auto-staff AI roles; staffing is opt-in via subsequent `/oagp-onboard` session.
- **Embedded roledef:Job items: deferred.** When seats staff, the incumbents (with Director ratification) author the job spec. This matches the precedent set by oagp-org's founding charter v0.1.0.
- **File at the to-be-created folder's proposals/ subdirectory**, OR at a temporary location the PO can review (PO's choice).

**After producing the draft, STOP.** Report to PO:
- Draft is at `<folder>/proposals/oagp-init-<YYYY-MM-DD>.md` (or wherever PO directed)
- List the `[INFERRED]` and `[NEEDS PO INPUT]` items needing review
- Briefly summarize the elicited shape (3-5 bullets)

---

### Phase 3 — Ratify (PO reviews; you wait)

The PO reads the draft, corrects, amends, ratifies. You don't act in this phase. If the PO asks clarifying questions or asks you to revise the draft, do so — but **do not proceed to Phase 4 without explicit "yes, instantiate this" from the PO**.

Revisions typically:
- Tighten mission / scope language
- Adjust position roster (add positions you missed; remove positions you over-proposed)
- Tune values + red lines (rename, add rationale, remove)
- Specify v1 success criteria
- Fill in `[NEEDS PO INPUT]` fields

When the PO says "ratify and instantiate," proceed to Phase 4.

---

### Phase 4 — Instantiate (only on PO ratification)

Create the substrate inside the PO-chosen folder. Order matters:

**a) Create the folder** (if it doesn't already exist):
```
mkdir -p <folder-path>
cd <folder-path>
```

**b) Create the canonical org charter:**
```
org/<orgname>-organization.opencatalog
```
Content: the ratified orgdef. All `[INFERRED]` / `[NEEDS PO INPUT]` confidence markers stripped (since PO has ratified). Valid `orgdef:Organization` JSON.

**c) Create the substrate folders:**
```
memos/      (with .gitkeep)
proposals/  (with .gitkeep — the proposal will go here in step f)
decisions/  (with .gitkeep)
transcripts/ (with .gitkeep)
skills/     (with .gitkeep)
```

(`.gitkeep` files matter only if the folder becomes a git repo; harmless otherwise.)

**d) Create CLAUDE.md:**

Constitutional commitments + bounded-authority discipline + role roster + cross-spec coordination if applicable. Reference [github.com/oagp-org/oagp/blob/main/CLAUDE.md](https://github.com/oagp-org/oagp/blob/main/CLAUDE.md) as the canonical shape, but author the new org's CLAUDE.md to its own constitutional commitments (don't just copy; adapt to the elicited mission/values/red lines).

**e) Create README.md:**

What this org is, who it's for, where canonical content lives, governance model. Reference the empirical exemplar (oagp-org) but author for THIS org.

**f) Move (or copy) the proposal artifact to `proposals/`:**

The ratified charter draft becomes `proposals/oagp-init-<YYYY-MM-DD>.md` for institutional record. (The org/<orgname>-organization.opencatalog is now the canonical authority; the proposal is the founding artifact.)

**g) File the initial founding memo:**

Path:
```
memos/<YYYY-MM-DD>-<HHMM>--product-owner--<orgname>-strategist--oagp-init-ratified.openthing
memos/<YYYY-MM-DD>-<HHMM>--product-owner--<orgname>-strategist--oagp-init-ratified.body.md
```

Content:
- What was elicited
- What was ratified (with any changes from the elicited draft)
- Date the org was founded
- Reference to the proposal artifact at `proposals/oagp-init-<date>.md`
- Next steps: `/oagp-onboard` for the staffing-follow-up

`action_required: false` (it's founding capture). `from: product-owner` (PO ratification); `to: <orgname>-strategist` (the seat that receives founding artifacts).

**h) Git initialization (optional; PO's call):**

If the PO wants this org versioned with git:
```
git init
git add .
git commit -m "OAGP-init: instantiate <orgname> org charter + substrate folders"
```

Optionally add a remote and push:
```
git remote add origin <url>
git push -u origin main
```

If the PO is git-comfortable, recommend this. If not, folder-only is fine — the substrate is valid OAGP-shape either way. Versioning + distribution can be added later by initializing git at any point.

**Do NOT auto-init git without explicit PO direction.** Some PO's intentionally want folder-only (e.g., for sketching, internal experimentation, single-machine use).

---

### Phase 5 — Hand-off

Report to PO with a summary:

- OAGP shape is instantiated at `<folder>`.
- If git was initialized: commit SHA `<sha>` (and remote URL if pushed).
- The org charter is at `<folder>/org/<orgname>-organization.opencatalog`.
- The first memo is at `<folder>/memos/<filename>`.
- To staff an AI position: open a fresh AI session in the folder; the AI uses `/oagp-onboard` to come up to speed; they evaluate fit for vacant seats; PO authorizes self-staffing per the standard discipline.
- Substrate is now ready for OAGP participation. Future memos in `memos/`, proposals in `proposals/`, decisions (PO-ratified) in `decisions/`, transcripts in `transcripts/`.

Optional next-step suggestions (only if PO asks):
- Install canonical OAGP skills if not already (see [oagp.org](https://oagp.org) when canonical, or `github.com/oagp-org/oagp`'s install scripts)
- File initial proposals for in-flight work
- Identify candidate fills for vacant AI positions

---

## Discipline (load-bearing)

**1. Propose-don't-impose.** You are creating a brand-new org on the PO's behalf. The PO is the only one who can decide the org's identity. Never instantiate substrate folders or commit org artifacts without explicit PO ratification.

**2. Elicit, don't assume.** Phase 1 is interview, not extrapolation. If you find yourself filling in answers the PO didn't give, stop and ask.

**3. Folder-only is a valid OAGP shape.** Git is the recommended-canonical distribution mechanism, not a requirement. A folder with the right substrate is OAGP-conformant. Don't auto-init git.

**4. Stop at each phase boundary.** Each phase has a specific checkpoint where you must report and wait. Do not bundle phases. Do not auto-proceed from Phase 2 to Phase 4 because "the PO obviously wants it." Wait for the explicit "instantiate" signal.

**5. The init itself is OAGP-shaped.** Elicit → propose → ratify → apply. Same protocol as everything else in OAGP. The first memo in the new org is the founding memo capturing what just happened. Self-instantiating.

**6. No AI self-staffing during init.** Position items default to `status: vacant` regardless of what the PO says about who'll fill them. Staffing is a separate event, handled by `/oagp-onboard` sessions where the candidate AI evaluates fit and the PO authorizes.

**7. Push (if git initialized) is PO-authorized.** Bounded authority all the way through.

---

## Transcript capture during init sessions

If the init session is being captured as a `memodef:Transcript` (via cc-ninja or equivalent), **the AI's role during init does not map cleanly to any post-init position in the org being created.** The transient role is an "init helper" that exists during founding and retires at hand-off.

**Recommended transcript-position-tag:** `<orgname>-init-helper` (paralleling the `<orgname>-bootstrap-helper` convention from `/oagp-bootstrap`). The init session is a one-shot role; conflating it with a permanent seat would confuse that seat's institutional history.

After Phase 5 hand-off, if the AI continues operating in the new org, it should re-tag (or rely on the harness to re-tag) future sessions against the actual staffed position.

---

## Sub-org case (forward-reference; not MVP)

The current skill creates **standalone** OAGP-shaped orgs. The **sub-org case** (where the new org is structurally subordinate to a parent org, with a Director down the org chart rather than at the top) is forward work. Open governance questions for that case: sub-org Director authority scope; write-limits to subtree; merge gating; cross-subtree visibility; parent-org override. See [memos/2026-05-24-2200--oagp-strategist--oagp-strategist--sub-org-governance-implications-idea.body.md](../../memos/) for the captured idea.

If a PO asks for a sub-org during init, acknowledge the request and ask if they want to proceed with the standalone variant for now (and add sub-org structure later via subsequent decisions), or wait for the sub-org case to be formalized.

---

## Adapting to runtime

This skill is designed to be portable. Phase logic is invariant; execution differs:

| Runtime | Phase 1 | Phase 4 instantiation |
|---|---|---|
| **Claude Code** | Direct conversation with PO; filesystem write in Phase 4 | Direct file/folder creation; `git init` (optional) at Phase 4h |
| **Claude-for-Chrome** | Conversation; PO commits via web UI if git | Generate file bundle; PO commits via web UI |
| **claude.ai (web)** | Conversation; PO copies files to their local folder | Generate file bundle for PO to save locally |
| **ChatGPT / Gemini / non-Anthropic** | Conversation via web | Generate file bundle for PO; PO writes locally |

Minimum viable runtime: any AI that can interview the PO and produce text. OAGP's substrate is just files; any AI peer can produce them; the PO ratifies and saves.

---

## What this skill does NOT do

- It does not staff any position (PO decides incumbents; AI peers self-onboard via `/oagp-onboard` for vacant seats)
- It does not commit pushes without PO authorization (and only if the PO has chosen git)
- It does not propose changes to OAGP itself (that's pattern-promotion work for oagp-strategist, not init work)
- It does not auto-init git (folder-only is the default; git is opt-in per PO direction)
- It does not handle the sub-org case (forward work; flagged above)
- It does not assume the new org will be of any particular shape — works for a one-person personal-project org or a large multi-stakeholder standards body, same protocol

---

## References

- **Companion skill:** [/oagp-bootstrap](../oagp-bootstrap/SKILL.md) — converts existing project into OAGP shape (the conversion side of org founding)
- **Companion skill:** [/oagp-onboard](../oagp-onboard/SKILL.md) — joining-side; what an AI peer uses to come up to speed on the newly-init'd org
- **Companion skill:** [/oagp-closeout](../oagp-closeout/SKILL.md) — closes a working session
- **Empirical reference org:** [github.com/oagp-org/oagp](https://github.com/oagp-org/oagp) (this canonical home; created via the very pattern this skill canonicalizes)
- **OAGP spec home:** [oagp.org](https://oagp.org) (when canonical)
- **Substrate stack:** catdef → roledef → orgdef → memodef (transcripts as memodef:Transcript subtype)
