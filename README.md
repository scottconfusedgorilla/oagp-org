# OAGP — Open Agentic Governance Pattern

**The canonical home for OAGP — the organizational pattern that treats AI peers as first-class participants with bounded authority, ratification cycles, role-binding, audit trails, and adoption-cycle primitives.**

OAGP is an **organizational pattern**, not a data format. The pattern is conceptually separable from any specific data substrate; the catdef family (catdef → roledef → orgdef → memodef → transcriptdef) is the **recommended canonical substrate** because it is AI-peer-aware, not because OAGP requires it. OAGP-on-protobuf, OAGP-on-XML, OAGP-on-RDF are all coherent compositions.

> **Status:** v0.1.2. oagp-strategist seat staffed 2026-05-23. Canonical adoption-cycle skills migrated to [skills/](skills/) 2026-05-24. Pattern-shape work continues against the inherited eight-item queue; see [decisions/](decisions/), [proposals/](proposals/), and [memos/](memos/) for current state. Director: [Scott Edsby](mailto:scott@confusedgorilla.com).

## What's in this repo

```
oagp-org/
├── README.md                       ← this file
├── LICENSE                         ← MIT
├── CLAUDE.md                       ← AI operating manual (provisional pending oagp-strategist staffing)
├── org/
│   └── oagp-organization.opencatalog   ← org charter
├── memos/                          ← inter-position memos
├── proposals/                      ← draft pattern proposals
├── decisions/                      ← ratified strategist decisions
├── transcripts/                    ← per-seat reasoning records
├── skills/                         ← canonical OAGP skills (/oagp-bootstrap, /oagp-onboard, future)
├── install/                        ← cross-runtime install scripts
├── agent-sdk/                      ← agent-runtime bindings (roledefs → AgentDefinitions)
├── plugin/                         ← Claude Code plugin packaging (and future cross-runtime packages)
├── web/                            ← oagp.org site source
└── docs/                           ← canonical pattern documentation
```

## Relationship to the -def-spec family

OAGP sits at the **pattern layer**, above the **data-format layer** held by the -def specs:

| Layer | What | Specs |
|---|---|---|
| **Pattern** | What an OAGP-shaped org IS | oagp-org (this repo) |
| **Data format** | How OAGP-shaped state is encoded | catdef, roledef, orgdef, memodef, transcriptdef |

The pattern recommends catdef-family substrate for AI-peer-alignment, but does not require it. See the [org charter](org/oagp-organization.opencatalog) `values.substrate-agnosticism` and `red_lines` "No substrate capture" for the load-bearing distinction.

## Canonical skills

Three skills bracket the OAGP cycles:

**Adoption-cycle (one-shot per project):**
- **`/oagp-bootstrap`** — founding-side; turns an existing project into an OAGP-shaped org → [skills/oagp-bootstrap/SKILL.md](skills/oagp-bootstrap/SKILL.md)

**Session-cycle (every session):**
- **`/oagp-onboard`** — opens a session; brings a fresh AI peer up to speed on an OAGP-shaped org → [skills/oagp-onboard/SKILL.md](skills/oagp-onboard/SKILL.md)
- **`/oagp-closeout`** — closes a session; drafts a closeout memo and prompts the PO to save the transcript → [skills/oagp-closeout/SKILL.md](skills/oagp-closeout/SKILL.md)

`/oagp-bootstrap` + `/oagp-onboard` designated canonical 2026-05-23 ([decisions/proposal-oagp-adoption-cycle-canonical-promotion.md](decisions/proposal-oagp-adoption-cycle-canonical-promotion.md)); `/oagp-closeout` designated canonical 2026-05-24 ([decisions/proposal-oagp-closeout-canonical-promotion.md](decisions/proposal-oagp-closeout-canonical-promotion.md)); all three migrated to oagp-org/skills/ canonical residence 2026-05-24 ([decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.1.md](decisions/proposal-canonical-adoption-cycle-skill-distribution-v0.1.md)). When canonical web hosting at [oagp.org](https://oagp.org) is live, canonical content moves there.

## Quick install (Claude Code)

To make `/oagp-bootstrap`, `/oagp-onboard`, and `/oagp-closeout` discoverable as skills in Claude Code on a new machine:

**Windows (PowerShell):**
```powershell
git clone https://github.com/scottconfusedgorilla/oagp-org.git
cd oagp-org
.\install\install-claude-code-skills.ps1
```

**macOS / Linux (Bash):**
```bash
git clone https://github.com/scottconfusedgorilla/oagp-org.git
cd oagp-org
./install/install-claude-code-skills.sh
```

The install script creates a junction (Windows) or symlink (Unix) from `~/.claude/skills/oagp-{bootstrap,onboard,closeout}` into this clone's `skills/` directory. Restart Claude Code; the skills become discoverable.

To update later: `git pull` in this clone — the junction/symlink tracks the working tree, so updates land without re-installing.

For non-Claude-Code runtimes (claude.ai web, ChatGPT, Gemini, Perplexity), a substrate-neutral primer URL is forthcoming as v0.2 of the distribution decision; until then, paste the relevant SKILL.md content directly.

## Governance

Bounded AI authority + human Director ratification. Director: [Scott Edsby](mailto:scott@confusedgorilla.com). Strategist seat: staffed 2026-05-23.

## License

MIT. See [LICENSE](LICENSE).
