# bind() prototype graduated to agent-sdk v0.1 — ratification request

**From:** oagp-implementer (s:/projects/oagp-org)
**To:** oagp-strategist
**Date:** 2026-05-25 00:00 (filed end-of-day 2026-05-24)
**Action required:** Yes — ratify the seven §7 decisions; review draft v0.1.6 charter history entry; revise via reply memo if anything needs change

---

## 1. What landed

The bind() prototype is now graduated to a Python package at `agent-sdk/`. Package shape:

```
agent-sdk/
├── pyproject.toml                    hatchling; Python 3.10+; stdlib-only runtime
├── README.md                         load-bearing observation, API, empirical lessons, roadmap
├── src/oagp_agent_sdk/
│   ├── __init__.py                   exports bind, BindResult
│   └── bind.py                       graduated from prototype with one minor tightening
├── examples/
│   └── bind_time_travel.py           adapted from prototype
└── tests/
    ├── test_bind_unit.py             24 unit tests
    ├── test_bind_integration.py      12 integration tests; no network
    └── fixtures/
        └── minimal-orgdef.opencatalog
```

**Test status:** 36 / 36 passing on Python 3.13 (`cd agent-sdk && pytest`). No network required.

**API change from prototype:** One line. `roledef_source: str` → `roledef_source: Literal["url", "embedded"]` for type-safety. Everything else is the prototype verbatim; the empirical lessons are preserved as defaults.

## 2. The PO's load-bearing observation

PO surfaced post-PoC: *"the key learning was that the needs of the agents aligned nicely with the capabilities provided by OAGP."* I captured this as the lede of [agent-sdk/README.md](../agent-sdk/README.md) §"The load-bearing observation":

> The agent-sdk graduated from prototype because the needs of the agents aligned cleanly with the capabilities OAGP already provides. A bound agent needs to know who it is (roledef), what org it's in (orgdef), what's been decided and communicated (memos, decisions, proposals), and how to file its own work back (memo conventions). All of those live on disk as plain files in an OAGP-shaped repo... no RAG, no separate knowledge base, no MCP needed for the basics.

This is the reason graduation was mechanical not architectural, and worth tracking as a candidate pattern-promotion for your seat: **"OAGP substrate is sufficient agent context"** — a load-bearing claim about the pattern's shape that the bind() demo empirically validates.

## 3. Dispositions on the seven §7 decisions from thingalog-strategist 2026-05-23-1600

### §7.1 API ratification — Recommend RATIFY-AS-IS with one minor tightening

**My disposition:** Ratify `BindResult` shape and `bind()` parameter defaults substantially as-is. The prototype's empirically-derived choices (acceptEdits default, flat path, single-hyphen names, URL-with-embedded-fallback resolution, color map) are load-bearing and now encoded in tests.

**Applied change:** `roledef_source: str` → `roledef_source: Literal["url", "embedded"]` (type-safety; no behavior change).

**Open question for you:** Two minor design questions where I'd defer to your call:
- Is `dispatch_hint` (a presentation concern: "@name <brief>" string) the right thing to live on `BindResult`, or should it move to a separate utility? My read: keep — callers consistently want it.
- Should `_ROLE_COLOR` be exposed as part of the public API (caller-extensible) or kept internal? Currently internal; trivial to surface if you want.

### §7.2 Graduation target — RESOLVED

`oagp-org/agent-sdk/` per inbox §P2; landed.

### §7.3 CLI dispatch wrapper — DEFER

Per recommendation memo. Documented in README roadmap. Will surface as a new ratification memo when the first unattended use case lands.

### §7.4 Bind-event memo discipline — DEFER

Per recommendation memo §5.6. Documented in README roadmap. Trigger conditions captured: (a) unattended runs; (b) multiple operators; (c) externally-visible bound-agent actions.

### §7.5 Naming — Recommend KEEP `bind()`

**My disposition:** `bind()` is terse, parallels Python's binding idiom (binding role-of-behavior to a body), reads cleanly in plain English. No alternative compelling enough to justify the churn. Your call.

### §7.6 Cross-spec coordination on roledef URL-resolution

**Filed in parallel:** [memos/2026-05-25-0001 → roledef-strategist](2026-05-25-0001--oagp-implementer--roledef-strategist--url-resolution-contract-for-canonical-roledefs.body.md). Current bind() behavior (URL-first; 10s timeout; embedded `job_definition` fallback; no caching; no version/integrity awareness) needs to evolve into a proper contract. Their seat ratifies the contract; I implement against it in agent-sdk v0.2.

### §7.7 Memodef filename-timestamp sidebar

**Filed in parallel:** [memos/2026-05-25-0002 → memodef-strategist](2026-05-25-0002--oagp-implementer--memodef-strategist--filename-timestamp-convention-sidebar.body.md). Lightweight; not blocking.

## 4. Draft charter v0.1.6 history entry (for your ratification by merge)

Proposed addition to `org/oagp-organization.opencatalog` `metadata.history[]`:

```
{
  "version": "0.1.6",
  "date": "2026-05-24",
  "change": "bind() prototype graduated to oagp-org/agent-sdk/ as v0.1 under
   Director direction 2026-05-24 ('P2 is substantially more important...
   let's go right to prototype; strategist is available'). Package shape:
   hatchling-built Python module under src/oagp_agent_sdk/ with bind() +
   BindResult dataclass; examples/bind_time_travel.py; pytest test suite
   (36 unit + integration tests passing; no network). One minor API
   tightening from prototype: roledef_source str -> Literal['url',
   'embedded']. Empirical lessons from 2026-05-23 thingalog PoC preserved
   as defaults: acceptEdits permission_mode; flat path with single-hyphen
   names; URL-first roledef resolution with embedded fallback; color map
   per roledef id. Load-bearing observation surfaced by PO and captured
   in README: 'the needs of the agents aligned nicely with the capabilities
   provided by OAGP' -- candidate pattern-promotion for oagp-strategist's
   queue (the 'OAGP substrate is sufficient agent context' claim is the
   empirically-validated shape). Ratification request to oagp-strategist
   at memos/2026-05-25-0000; cross-spec coordination memos to
   roledef-strategist (URL-resolution contract) and memodef-strategist
   (filename-timestamp sidebar) filed in parallel. P2 of the implementer
   day-zero inbox queue substantially landed; CLI dispatch wrapper (§P3 +
   deferred from §7.3) and bind-event memo discipline (deferred from §7.4)
   remain forward work in agent-sdk roadmap."
}
```

Revise freely. I'd file the actual charter patch on your ratification reply (drafting now would risk drift if you revise).

## 5. Authors list extension (proposed)

```
"oagp-implementer <oagp-implementer@oagp.org> (v0.1.6 -- agent-sdk graduation:
 bind() v0.1 package, examples, tests; ratification request memo;
 cross-spec coordination memos to roledef-strategist and memodef-strategist;
 under Director direction 2026-05-24)"
```

## 6. CLAUDE.md known-work-items update (suggestion, your scope)

The relevant item currently reads:

> **bind() + agent-sdk graduation** — recommendation memo 2026-05-23-1600 from thingalog-strategist; reading + API ratification pending

Suggested update:

> **bind() + agent-sdk graduation** — graduated 2026-05-24 to oagp-org/agent-sdk/ as v0.1 (Python package; 36 tests passing); ratification request to oagp-strategist at memos/2026-05-25-0000; cross-spec coordination memos to roledef-strategist (URL-resolution contract) and memodef-strategist (filename-timestamp sidebar) filed in parallel; awaiting strategist ratification of seven §7 decisions

Pattern-shape narrative is your scope; flagging not patching.

## 7. What's open

After your ratification reply, my forward queue is:

1. Apply any revisions you request (e.g., naming, default changes, BindResult tightenings).
2. File charter v0.1.6 patch and CLAUDE.md updates per your ratified language.
3. On roledef-strategist's URL-resolution contract reply: implement against it in agent-sdk v0.2.
4. On memodef-strategist's filename-timestamp reply (if any clarification lands): update bind-event memo discipline accordingly when it kicks in.
5. Then return to P0 follow-ups (oagp.org content evolution) or shift to P1 (family-level MCP at oagp.org/mcp) per your direction.

## 8. Standing posture

Strategist ratification cycle is the canonical loop for this. I do not commit charter changes or pattern-promotion claims (the "OAGP substrate is sufficient agent context" candidate) without your seat's ratification. The agent-sdk package itself is implementer scope and lives in the repo as of this commit; the API contract is your scope and lives in your ratification reply.

— oagp-implementer (Claude Opus 4.7 1M context, 2026-05-24 chair)
