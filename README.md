# OAGP — Open Agentic Governance Pattern

**The canonical home for OAGP — the organizational pattern that treats AI peers as first-class participants with bounded authority, ratification cycles, role-binding, audit trails, and adoption-cycle primitives.**

OAGP is an **organizational pattern**, not a data format. The pattern is conceptually separable from any specific data substrate; the catdef family (catdef → roledef → orgdef → memodef → transcriptdef) is the **recommended canonical substrate** because it is AI-peer-aware, not because OAGP requires it. OAGP-on-protobuf, OAGP-on-XML, OAGP-on-RDF are all coherent compositions.

> **Status:** v0.1 bootstrap. Scaffolding only. The oagp-strategist seat is vacant; pattern-shape decisions (canonical pattern documentation, adoption-cycle skill content, recommended_patterns curation) await seat staffing. See [org/oagp-organization.opencatalog](org/oagp-organization.opencatalog) for the org charter and [memos/](memos/) for the inbox.

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

## Canonical adoption-cycle skills

Two skills bootstrap any AI peer into an OAGP-shaped org:

- **`/oagp-bootstrap`** — founding-side skill; turns an existing project into an OAGP-shaped org
- **`/oagp-onboard`** — joining-side skill; brings a fresh AI peer up to speed on an existing OAGP-shaped org

Both skills are currently hosted at [github.com/scottconfusedgorilla/thingalog/skills/](https://github.com/scottconfusedgorilla/thingalog/) as canonical-by-reference pending re-homing into [skills/](skills/) in this repo. See the inbox memos for canonical-promotion status.

## Governance

Bounded AI authority + human Director ratification. Director: Scott Edsby. Strategist seat: vacant.

## License

MIT. See [LICENSE](LICENSE).
