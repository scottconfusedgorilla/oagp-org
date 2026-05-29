# oagp-agent-sdk

**Bind an OAGP position to a runnable Claude Code subagent.**

`bind()` turns an `orgdef:Position` + its referenced roledef into a Claude Code subagent file. The bound agent shows up in the agent view panel (terminal: `claude agents`; VSCode: built-in panel), runs supervised in a background session, and reads the org's substrate (charter, memos, decisions, proposals) directly from disk as its primary context.

## The load-bearing observation

The agent-sdk graduated from prototype because **the needs of the agents aligned cleanly with the capabilities OAGP already provides.** A bound agent needs to know who it is (roledef), what org it's in (orgdef), what's been decided and communicated (memos, decisions, proposals), and how to file its own work back (memo conventions). All of those live on disk as plain files in an OAGP-shaped repo. The agent reads its position's roledef once, then operates directly against the substrate — no RAG, no separate knowledge base, no MCP needed for the basics. The "all org state is data on disk" property of OAGP turned out to be exactly the right context shape for AI peers acting as bound roles.

This alignment is why the prototype worked the first time, why time-travel binding (`git worktree add <path> <SHA>` + `bind(orgdef_path=<worktree>/...)`) needed no special machinery, and why this v0.1 graduation is mechanical rather than architectural.

## Quick start

```python
from oagp_agent_sdk import bind

result = bind(
    orgdef_path="examples/demo-orgdef.opencatalog",   # bundled, runnable
    position_id="doc-reviewer",
    initial_prompt="Review the target doc and file a proposal. Propose-only. Stop.",
    tools=["Read", "Write", "Glob", "Grep"],
)

print(f"Bound: {result.agent_name}")
print(f"Dispatch: {result.dispatch_hint}")
# -> Bound: doc-reviewer
# -> Dispatch: @doc-reviewer
```

Then in Claude Code's agent view panel, start a new session and type the dispatch hint. The bound agent runs supervised; observe progress via the panel's per-session peek/attach.

## API

### `bind(orgdef_path, position_id, *, ...) -> BindResult`

Parameters and defaults are documented in [src/oagp_agent_sdk/bind.py](src/oagp_agent_sdk/bind.py) docstrings. Key defaults:

| Parameter | Default | Why |
|---|---|---|
| `agents_root` | `.claude/agents` (under orgdef's project root) | VSCode agent view does not recurse; flat path is required |
| `model` | `"inherit"` | Use the dispatcher's session model unless overridden |
| `permission_mode` | `"acceptEdits"` | `bypassPermissions` rejected from frontmatter without prior interactive acceptance; `acceptEdits` is the practical default |
| `color` | (roledef-id colormap fallback `cyan`) | Visual identification in the panel |

### `BindResult`

Dataclass containing everything the caller needs to know about the bind: file path, agent name, dispatch hint, position + roledef provenance (id, version, source: `"url"` or `"embedded"`, URL if used).

### `run_seat(orgdef_path, position_id, *, ...) -> DispatchRecord` (v0.2)

Autonomous dispatch built on `bind()`: dispatch a bound agent as an **unattended** session where bounded authority is **structural**, not prompt-level. Returns a `DispatchRecord` (agent name, org-state SHA, tier, granted authority, toolset, bind-event memo path, backend, dispatch handle).

**Three tiers** (per the v0.2 build-direction; *"we provide a gun, you provide a foot; the gun ships with instructions not to aim at the foot; and even then the gun can never give instructions to another gun"*):

- **Tier 1 — propose-only by construction (default).** The default toolset contains no commit/push/merge/tag/release-capable tools (in Claude Code, that capability rides on `Bash`). The agent drafts files; a human commits. Requesting a Director-capable tool at Tier 1 raises `Tier1ViolationError` — the agent is *constructed* unable, not asked to refrain.
- **Tier 2 — explicit, audited Director elevation.** `grant_director_actions=["commit", "push", ...]` adds the capable tools (hard layer) **and** fires a bind-event memo recording the grant (audit layer). Never silent; never prompt-only.
- **Tier 3 — non-delegable dispatch (hard floor, no override).** No bound agent may dispatch/bind/elevate another. Enforced environmentally: `bind()` / `run_seat()` refuse when the `OAGP_BOUND_AGENT` marker is present in the environment (set by the dispatch backend), with package-absence as a deployment-layer backstop.

Autonomous-mode roledef resolution is **fail-closed**: a URL-fetch failure aborts (`RoledefResolutionError`) unless `allow_embedded_fallback=True`. Interim default pending the roledef-strategist URL-resolution contract ([memos/2026-05-25-0001](https://github.com/oagp-org/oagp/blob/main/memos/2026-05-25-0001--oagp-implementer--roledef-strategist--url-resolution-contract-for-canonical-roledefs.body.md)).

```python
from oagp_agent_sdk import run_seat

# Tier 1 (default): propose-only autonomous dispatch
record = run_seat(
    orgdef_path="examples/demo-orgdef.opencatalog",
    position_id="doc-reviewer",
    brief="Review the agent-sdk README; file improvement proposals. Propose-only.",
)
assert record.tier == 1                 # no Bash; cannot push/merge
assert record.bind_event_memo.exists()  # audit trail for the unattended run
```

**Dispatch backend.** `run_seat()` is the cross-vendor seam. On Claude Code, `select_backend("auto")` returns the `WorkflowsBackend`, which generates a workflow that dispatches the bound agent via `agentType` (so the bound `tools:` frontmatter governs). `run_seat()` *generates* the dispatch artifacts; the **launcher** runs them (see below). `StubBackend` records dispatch intent for tests.

### `launch_seat(orgdef_path, position_id, *, ...) -> LaunchRecord` (v0.2 — canonical autonomous dispatch)

`launch_seat()` is the **canonical autonomous-dispatch operational layer** (ratified in [decisions/proposal-agent-sdk-v0.2-governance-addendum-autonomous-dispatch-constraints.md](https://github.com/oagp-org/oagp/blob/main/decisions/proposal-agent-sdk-v0.2-governance-addendum-autonomous-dispatch-constraints.md)). It is the single locus of two MUST-conventions:

- **Launcher-per-dispatch (fresh session + `agentType`).** Autonomous dispatch MUST start a clean session per dispatch, against which the bound agent file pre-exists so `agentType` resolves and its `tools:` frontmatter binds. This is *why* it works, not a limitation: the session-start registry rule is what loads the structural Tier-1 bound. Inline / same-session dispatch is **barred** for autonomous use (it substitutes the workflow's broad default toolset). `launch_seat()` therefore always dispatches via `WorkflowsBackend` (agentType); it does not accept an inline backend.
- **Tier-2 package-absence gate.** Tier-2 (elevated) autonomous dispatch is refused (`Tier2GateError`) unless the launcher verifies the dispatch environment cannot `import oagp_agent_sdk` — the in-band enforcement of the Tier-3 non-delegable floor for the Workflows path (where the `OAGP_BOUND_AGENT` env marker cannot reach a workflow-spawned subagent). Tier-1 needs no gate (safe by toolset). Until run in a verified package-absent environment, **Tier-1 is the only sanctioned autonomous path.**

```python
from oagp_agent_sdk import launch_seat, ClaudeCliLauncher

# Tier-1 propose-only autonomous dispatch (default launcher records the
# fresh-session command; pass ClaudeCliLauncher(execute=True) to spawn).
record = launch_seat(
    orgdef_path="examples/demo-orgdef.opencatalog",
    position_id="doc-reviewer",
    brief="Review the agent-sdk README; file improvement proposals. Propose-only.",
)
assert record.tier == 1 and record.tier2_gate_checked is False
```

The fresh-session spawn is environment-dependent: `StubSessionLauncher` (default) records the intent + the `claude` command that would run; `ClaudeCliLauncher(execute=True)` runs it. A fresh-session structural run (agentType, launcher-driven) is what closes the full end-to-end demo — see [examples/README.md](examples/README.md).

## Empirical lessons (encoded in defaults)

Six things learned from the prototype run against thingalog 2026-05-16; preserved as load-bearing defaults in `bind()` and documented at [memos/2026-05-23-1600 §5](https://github.com/oagp-org/oagp/blob/main/memos/2026-05-23-1600--thingalog-strategist--oagp-strategist--bind-and-agent-view-empirically-validated-recommend-graduation.body.md):

1. **Claude Code's agent view is the canonical observation surface.** This SDK does NOT ship a separate UI. Anthropic maintains the panel; we target it.
2. **Subagent file shape.** `.claude/agents/<name>.md` with YAML frontmatter; required `name` + `description`; useful `tools`, `model`, `permissionMode`, `color`, `initialPrompt`, `maxTurns`.
3. **Flat path; single-hyphen names.** VSCode agent view does not recurse into subdirectories; the `name:` frontmatter rejects double-hyphen separators.
4. **`permission_mode="acceptEdits"` is the default.** `bypassPermissions` cannot be loaded from frontmatter without prior interactive acceptance (Claude Code security floor).
5. **Time-travel mechanics.** `git worktree add <path> <SHA>` + bind against the worktree's orgdef = a bound agent that sees org state as it was at any commit. Per-commit granularity is the natural OAGP unit.
6. **Bind-event memo discipline is deferred** until first unattended use. Interactive dispatch's audit trail is the agent view's session list (visible, supervised, persistent).

## Status

**v0.2 — autonomous dispatch, 2026-05-29.** `run_seat()` + the three-tier structural bounded-authority model + bind-event memos + fail-closed roledef resolution; live `WorkflowsBackend` (agentType dispatch); and `launch_seat()` — the canonical launcher-per-dispatch layer with the Tier-2 package-absence gate (per the [governance addendum](https://github.com/oagp-org/oagp/blob/main/decisions/proposal-agent-sdk-v0.2-governance-addendum-autonomous-dispatch-constraints.md)). All conformance tests pass (105 total). The propose-only dispatch flow is empirically validated (see [examples/](examples/)); the full structural end-to-end run is a fresh-session launcher run (`ClaudeCliLauncher(execute=True)`), environment-dependent.

**v0.1 — graduated 2026-05-24** from prototype; **ratified 2026-05-28** by oagp-strategist (interactive scope; bounded authority by supervision-convention). Empirical proof: 2026-05-23 time-travel engagement (thingalog 2026-05-16 snapshot, bound as `security-tester`) surfaced C-1 + H-1 findings against current main.

## Roadmap

| Item | Status |
|---|---|
| `run_seat()` autonomous dispatch + three tiers | **Done (v0.2 core)** |
| Bind-event memo filing | **Done (v0.2)** — every autonomous dispatch emits one |
| Fail-closed roledef resolution | **Done (v0.2 interim)** — abort on URL failure absent explicit fallback |
| Live Workflows-class dispatch backend (Claude Code) | **Done (v0.2)** — `WorkflowsBackend`, agentType dispatch |
| `launch_seat()` launcher-per-dispatch + Tier-2 package-absence gate | **Done (v0.2)** — canonical autonomous-dispatch layer |
| Empirical propose-only dispatch demo (reads substrate, files a proposal) | **Done** — see [examples/](examples/) |
| Fresh-session structural end-to-end run (`ClaudeCliLauncher(execute=True)`) | Environment-dependent; closes the full demo when run from a real fresh session |
| URL-resolution contract for canonical roledefs (caching, versioning, integrity) | Awaiting roledef-strategist reply ([memos/2026-05-25-0001](https://github.com/oagp-org/oagp/blob/main/memos/2026-05-25-0001--oagp-implementer--roledef-strategist--url-resolution-contract-for-canonical-roledefs.body.md)); swap interim fail-closed default for the ratified contract |
| Caller-provided inline roledef override | When a use case surfaces (none yet) |

## Tests

```bash
cd agent-sdk/
pip install -e ".[test]"
pytest                          # unit tests
pytest -m integration           # integration tests (skipped by default)
```

Integration tests use a fixture orgdef under `tests/fixtures/`; no external services required.

## License

MIT. Part of the OAGP family. See [oagp.org](https://oagp.org) and the [charter](https://github.com/oagp-org/oagp/blob/main/org/oagp-organization.opencatalog).
