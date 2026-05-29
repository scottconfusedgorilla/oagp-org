# Review proposal: agent-sdk/README.md

**Reviewer:** doc-reviewer (Tier-1, propose-only)
**Target:** s:/Projects/oagp-org/agent-sdk/README.md
**Org-state SHA at dispatch:** 53fb190230d98c9d6b71ea092ea5898f7ef97f7c
**Authority:** propose-only — no edits applied to the README; these are recommendations a human ratifies.

Grouped by severity: blocking / improvement / nit.

---

## Blocking

### B-1. "OAGP" is never expanded for a first-time reader

The very first line uses the acronym with no expansion anywhere in the document:

> **Bind an OAGP position to a runnable Claude Code subagent.**

A reader who lands on this repo cold has no idea what OAGP is until the License line, which only links out:

> MIT. Part of the OAGP family. See [oagp.org](https://oagp.org) and the [charter](...).

**Proposed change:** Expand OAGP on first use, with a one-clause gloss, e.g.:
> **Bind an OAGP (Open Agent Governance Pattern — an org pattern where all org state lives as plain files on disk) position to a runnable Claude Code subagent.**

Adjust the expansion to match the canonical name; the point is that the term must be defined before it is relied on six times.

### B-2. Quick-start example references a position that does not exist in the example org

The quick start and the `run_seat` example both bind `position_id="security-tester"`:

> ```python
> result = bind(
>     orgdef_path="path/to/org/<orgname>-organization.opencatalog",
>     position_id="security-tester",
> ```

But the only example org shipped in this repo (`examples/demo-orgdef.opencatalog`) defines a single position, `doc-reviewer`. A reader who copies the snippet against the bundled example gets a position-not-found failure with no nearby explanation. The `orgdef_path` placeholder also does not match the example file name (`demo-orgdef.opencatalog`).

**Proposed change:** Either (a) point the quick-start example at the bundled example org and the `doc-reviewer` position so it runs as written, or (b) add one line stating that `security-tester` is illustrative and the runnable example lives at `examples/demo-orgdef.opencatalog` (position `doc-reviewer`).

---

## Improvement

### I-1. "Quick start" runs `bind()` but the document's headline feature is `run_seat()`

The Quick start section demonstrates `bind()` (v0.1). The current Status header is:

> **v0.2 — autonomous-dispatch governance core, 2026-05-29.**

A first-time reader at v0.2 reaches a runnable `run_seat()` example only after the entire API section. The fastest path to "what does this thing actually do now" is buried.

**Proposed change:** Either retitle the current section "Quick start: bind()" and add a short "Quick start: run_seat()" companion near the top, or lead Quick start with the Tier-1 `run_seat()` example (which is the demo this repo's example org exists to prove) and keep `bind()` as the lower-level primitive below it.

### I-2. Dispatch instructions assume tool/environment knowledge not stated

> Then in Claude Code's agent view panel, start a new session and type the dispatch hint. The bound agent runs supervised; observe progress via the panel's per-session peek/attach.

"the panel's per-session peek/attach" names UI affordances without saying where they are or what they look like, and "the dispatch hint" was shown as `@security-tester` — but a reader binding `doc-reviewer` would need `@doc-reviewer`. The earlier mention gives the two invocation surfaces:

> shows up in the agent view panel (terminal: `claude agents`; VSCode: built-in panel)

but the dispatch step does not reconnect to them.

**Proposed change:** State the concrete action per surface (e.g., "type `@<agent_name>` in the VSCode panel's new-session box, or run `claude agents` in the terminal") and define "peek/attach" on first use or drop the jargon.

### I-3. `StubBackend` caveat is load-bearing but easy to miss

Two separate places tell the reader nothing actually launches yet:

> current default is `StubBackend`, which records dispatch intent without launching

> test 8 (live Workflows delegation) is deferred with the backend wiring.

A reader running the `run_seat()` example will see `record.bind_event_memo.exists()` pass and reasonably assume an agent ran. It did not.

**Proposed change:** Add an explicit one-liner to the `run_seat()` example or its intro, e.g. "Note: with the default `StubBackend`, this records dispatch intent and emits the bind-event memo but does **not** launch a live session yet (live backend deferred — see Roadmap)."

---

## Nit

### N-1. Cross-vendor claim is asserted but unsupported in-document

> **Dispatch backend.** `run_seat()` is the cross-vendor seam.

"cross-vendor seam" is asserted; the only backend named is Claude Code's. Either name a second backend (even as planned) or soften to "the cross-vendor seam (Claude Code backend today; other runtimes target the same `run_seat` surface)."

### N-2. Tests block mixes `bash` fence with a Windows-style repo

> ```bash
> cd agent-sdk/
> pip install -e ".[test]"
> ```

The repo lives under a Windows path (`S:\Projects\...`); the `cd agent-sdk/` assumes the reader is already one level up. Minor, but a reader at the repo root may already be in `agent-sdk/`. Consider noting the command is relative to the parent of `agent-sdk/`, or drop the `cd`.

### N-3. Long parenthetical quote in the Tier intro buries the tiers

> **Three tiers** (per the v0.2 build-direction; *"we provide a gun, you provide a foot; the gun ships with instructions not to aim at the foot; and even then the gun can never give instructions to another gun"*):

The metaphor is good but is wedged into the header line ahead of the actual list. Consider moving it to a one-line callout above the list so the three bolded tier names lead.

---

## Sections that are already clear (no change proposed)

- "The load-bearing observation" — clear, well-motivated, no jargon left undefined within its own frame.
- "Empirical lessons (encoded in defaults)" — concrete, numbered, each tied to a default.
- The `BindResult` and API parameter table — clear; the "Why" column is genuinely useful.
- Roadmap table — clear status vocabulary.
