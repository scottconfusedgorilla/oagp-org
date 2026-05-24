# Proposal: Canonical adoption-cycle skill distribution v0.1 — residence migration + Claude Code install path

**Status:** Open (awaiting Director ratification via merge)
**Author:** oagp-strategist <oagp-strategist@oagp.org>
**Created:** 2026-05-24
**Target version:** oagp-org v0.1.2 (history entry)
**Origin:**
- [memos/2026-05-24-0900 — schema-v1.1.0-ship-fyi-and-canonical-orgs-residence-fwd-ref](../memos/2026-05-24-0900--orgdef-strategist--oagp-strategist--schema-v1.1.0-ship-fyi-and-canonical-orgs-residence-fwd-ref.body.md) — coordination request from orgdef-strategist about canonical-content residence post-data-vs-pattern-sharpening
- [memos/2026-05-24-0905 — cross-machine-skill-deployment-friction-empirical-signal](../memos/2026-05-24-0905--orgdef-strategist--oagp-strategist--cross-machine-skill-deployment-friction-empirical-signal.body.md) — PO hit four-friction-point new-machine install
- PO direction 2026-05-24: "Tying to thingalog makes no sense"
- Builds on prior canonical-promotion decision: [decisions/proposal-oagp-adoption-cycle-canonical-promotion.md](../decisions/proposal-oagp-adoption-cycle-canonical-promotion.md) (which designated the skills as canonically OAGP's but left residence as forward work for the implementer seat)

## Summary

Migrate canonical SKILL.md content for `/oagp-bootstrap`, `/oagp-onboard`, and (newly canonicalized 2026-05-24) `/oagp-closeout` into `oagp-org/skills/`. Add a canonical Claude Code install path (README section + install scripts) covering all three skills. Defer substrate-neutral primer URL to v0.2 of this distribution decision and Claude Code plugin packaging to v0.3, with an explicit ordering commitment (primer before plugin) to preserve the cross-vendor red line structurally.

**Scope amendment 2026-05-24:** Per Director direction during the same v0.1.2 drafting window, `/oagp-closeout` was canonicalized as the session-cycle closing skill ([decisions/proposal-oagp-closeout-canonical-promotion.md](../decisions/proposal-oagp-closeout-canonical-promotion.md)). Its distribution rides on this v0.1 decision's mechanism (install scripts updated; README updated). Bootstrap + onboard + closeout = three canonical skills covering the adoption-cycle (bootstrap) and session-cycle (onboard + closeout).

## Motivation

Three signals converge:

1. **The 0905 friction memo** documents PO hitting four real friction points installing `/oagp-onboard` on a new machine, all rooted in the current "clone thingalog + `mklink /J`" workflow: (a) private-repo dependency, (b) five-step meta-research to find the canonical-by-reference pointer, (c) junction-pinning produces stale installs, (d) doesn't compose with eventually-canonical `oagp-org/skills/`.
2. **The 0900 coordination memo** asks where canonical-orgs library content properly lives post-data-vs-pattern-sharpening. The answer for skills is the same as the answer for templates: pattern-shape canonical content belongs in `oagp-org`, not in a sibling -def-spec.
3. **PO direction is conclusive.** Tying canonical OAGP content to a private portfolio repo violates the cross-vendor red line at the access layer.

The canonical-promotion decision yesterday already designated the skills as canonically OAGP's regardless of residence. This proposal triggers the residence move that the prior decision flagged as forward work.

## Proposed Change

1. **Skill content migration.** `oagp-org/skills/oagp-{bootstrap,onboard}/SKILL.md` populated with verbatim copies of the thingalog-hosted SKILL.md content as of 2026-05-23. Content updates (e.g., re-pointing references from "empirical reference is thingalog" to "canonical home is oagp-org, empirical-application example is thingalog") are **deferred to a v0.2 content-evolution decision** to keep residence migration decoupled from content changes. `oagp-org/skills/oagp-closeout/SKILL.md` newly authored 2026-05-24 by oagp-strategist (no migration required; this is the canonical first version).

2. **README install section.** `oagp-org/README.md` gets a "Quick install (Claude Code)" section with PowerShell and Bash recipes:
   ```
   git clone https://github.com/scottconfusedgorilla/oagp-org.git
   cd oagp-org
   .\install\install-claude-code-skills.ps1   # Windows
   ./install/install-claude-code-skills.sh    # macOS / Linux
   ```
   Plus an explanatory paragraph: junction/symlink keeps installs fresh; `git pull` in the oagp-org clone updates the skills.

3. **Install scripts.** Two parallel scripts in `oagp-org/install/`:
   - `install-claude-code-skills.ps1` — Windows; uses `mklink /J` for junctions
   - `install-claude-code-skills.sh` — macOS / Linux; uses `ln -s` for symlinks

   Both resolve `oagp-org/skills/<skill>` relative to the script's location, create `~/.claude/skills/` if needed, and idempotently replace any existing junction/symlink at the target. The `$skills` array includes all three canonical skills: `oagp-bootstrap`, `oagp-onboard`, `oagp-closeout`.

4. **Thingalog-side coordination.** Existing thingalog-hosted SKILL.md content stays in place (backward-compat for already-junctioned machines). A cross-spec coordination memo to thingalog-strategist proposes the timeline for thingalog/skills/ deprecation in favor of pointing at oagp-org/skills/ — thingalog-strategist controls the thingalog-side timeline.

5. **Cross-runtime delivery — explicit deferral, explicit ordering.**
   - **v0.2 (next):** substrate-neutral primer URL — a canonical markdown file at oagp-org root (`PRIMER.md`) that any AI with web access can fetch and self-onboard from. Enables ChatGPT, Gemini, Perplexity, claude.ai, future runtimes.
   - **v0.3 (after v0.2):** Claude Code plugin packaging. Ships AFTER the substrate-neutral primer is live so the plugin frames structurally as transport-not-canonical.

## Backward Compatibility

Existing machines junctioned to thingalog/skills/ continue to work. The migration adds a new canonical residence without breaking the old one. No forced cutover; thingalog-side deprecation is a separate coordination via thingalog-strategist.

## Conformance Tests

1. Fresh clone of oagp-org contains `SKILL.md` at `oagp-org/skills/oagp-{bootstrap,onboard}/`.
2. `install/install-claude-code-skills.ps1` on a fresh Windows machine creates `%USERPROFILE%\.claude\skills\oagp-bootstrap` and `...\oagp-onboard` as junctions pointing into the oagp-org clone.
3. `install/install-claude-code-skills.sh` on a fresh macOS/Linux machine creates equivalent symlinks at `~/.claude/skills/`.
4. After install + Claude Code restart, `/oagp-bootstrap` and `/oagp-onboard` appear in available skills.
5. `git pull` in the oagp-org clone updates the skill content live (junction/symlink tracks working tree).
6. `SKILL.md` content at the canonical residence matches the thingalog-hosted content as-of 2026-05-23 verbatim — residence migration is content-preserving.

## Alternatives Considered

1. **Keep thingalog as canonical; formalize canonical-by-reference.** Rejected. Private-repo dependency is a structural friction; cross-vendor adoption story breaks at the access layer.
2. **Migrate and immediately delete thingalog/skills/.** Rejected for v0.1. Existing machines have working junctions; breaking them is unnecessary churn. Deprecation timeline is thingalog-strategist's call.
3. **Deep-copy installs (not junction/symlink).** Rejected. Junction/symlink means `git pull` keeps installs fresh; copy means stale-install. Junction is the right default for v0.1; pinned-copy could be a future flag.
4. **Ship Claude Code plugin first as canonical.** Rejected per cross-vendor red line. Plugin is transport, not canonical. Substrate-neutral primer ships before-or-alongside (v0.2 before v0.3).
5. **Use git submodule rather than clone + junction.** Rejected. Submodules add complexity without solving the friction; clone + script is one command per OS.
6. **Use Anthropic Marketplace from day one.** Same as alternative 4 — premature vendor coupling; defer to v0.3 after primer URL is live.

## Open Questions

- **OQ1 — thingalog/skills/ deprecation timeline.** Once new machines use oagp-org, old machines still junction to thingalog. When do we update thingalog's README + the thingalog skill files to point at oagp-org as canonical and start treating thingalog-hosted as legacy? Resolution: cross-spec coordination memo to thingalog-strategist; their timeline call.
- **OQ2 — Install script vendoring.** Should scripts include their own canonical SHA reference / version pinning, or rely on "whatever's in HEAD"? Provisional: HEAD-tracking for v0.1; pinning is future enhancement.
- **OQ3 — Auto-update wrapper.** Junction-tracking solves stale-install when the user runs `git pull`, but doesn't auto-update. Is an `update-claude-code-skills.{ps1,sh}` script (wraps `git pull` + status output) worth adding? Provisional: yes, cheap; consider as a v0.1.1 follow-up if it's wanted.
- **OQ4 — Cross-runtime primer URL location.** When v0.2 ships, where does the primer live? Options: (a) `oagp-org/PRIMER.md` at repo root (interim), (b) `oagp.org/primer` when canonical site is live, (c) both with redirect. Resolution deferred to v0.2.

## Cross-spec coordination

- **Memo to thingalog-strategist** (build directive item; per OQ1): propose thingalog/skills/ deprecation timeline; not blocking.
- **No format-shape implications.** No coordination needed with -def-spec strategists.
- **Adjacent: canonical-orgs library residence** (the 0900 memo's main question) — orgdef-strategist asked about template residence, which is structurally parallel to skill residence. **This v0.1 decision resolves the skill case (canonical home: oagp-org); the canonical-orgs template case will be resolved in a separate decision since the templates' role differs from skills' role (validator-fixture vs. adoption-cycle).** Reply memo to orgdef-strategist forthcoming.
