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
    orgdef_path="path/to/org/<orgname>-organization.opencatalog",
    position_id="security-tester",
    initial_prompt="Read your role + the org's recent memos, then file a status memo back. Stop.",
    tools=["Read", "Write", "Glob", "Grep"],
    color="red",
)

print(f"Bound: {result.agent_name}")
print(f"Dispatch: {result.dispatch_hint}")
# -> Bound: security-tester
# -> Dispatch: @security-tester
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

## Empirical lessons (encoded in defaults)

Six things learned from the prototype run against thingalog 2026-05-16; preserved as load-bearing defaults in `bind()` and documented at [memos/2026-05-23-1600 §5](https://github.com/oagp-org/oagp/blob/main/memos/2026-05-23-1600--thingalog-strategist--oagp-strategist--bind-and-agent-view-empirically-validated-recommend-graduation.body.md):

1. **Claude Code's agent view is the canonical observation surface.** This SDK does NOT ship a separate UI. Anthropic maintains the panel; we target it.
2. **Subagent file shape.** `.claude/agents/<name>.md` with YAML frontmatter; required `name` + `description`; useful `tools`, `model`, `permissionMode`, `color`, `initialPrompt`, `maxTurns`.
3. **Flat path; single-hyphen names.** VSCode agent view does not recurse into subdirectories; the `name:` frontmatter rejects double-hyphen separators.
4. **`permission_mode="acceptEdits"` is the default.** `bypassPermissions` cannot be loaded from frontmatter without prior interactive acceptance (Claude Code security floor).
5. **Time-travel mechanics.** `git worktree add <path> <SHA>` + bind against the worktree's orgdef = a bound agent that sees org state as it was at any commit. Per-commit granularity is the natural OAGP unit.
6. **Bind-event memo discipline is deferred** until first unattended use. Interactive dispatch's audit trail is the agent view's session list (visible, supervised, persistent).

## Status

**v0.1 — graduated 2026-05-24** from prototype at `s:/scratch/oagp-agent-prototype/` per [thingalog-strategist's recommendation memo (2026-05-23-1600)](https://github.com/oagp-org/oagp/blob/main/memos/2026-05-23-1600--thingalog-strategist--oagp-strategist--bind-and-agent-view-empirically-validated-recommend-graduation.body.md). Awaiting oagp-strategist ratification on the v0.1 API surface and the seven §7 decisions from the recommendation memo.

Empirical proof: 2026-05-23 time-travel engagement (thingalog 2026-05-16 snapshot, bound as `security-tester`) surfaced C-1 (photo moderation absence) + H-1 (admin JWT not validated) findings against current main — both directly actionable.

## Roadmap

| Item | When |
|---|---|
| CLI dispatch wrapper (`claude --bg --agent <name>`) | When first unattended use case lands |
| `run_seat()` / scheduler | After CLI dispatch |
| Bind-event memo filing | Triggered when bind() runs unattended, when multiple operators share runtime, or when bound agents make externally-visible changes |
| Caller-provided inline roledef override | When a use case surfaces (none yet) |
| URL-resolution contract for canonical roledefs (caching, versioning, fallback) | Coordination memo with roledef-strategist filed on graduation |

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
