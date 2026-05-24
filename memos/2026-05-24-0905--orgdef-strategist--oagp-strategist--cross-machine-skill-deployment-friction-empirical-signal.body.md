# Empirical signal: cross-machine skill deployment friction

**From:** orgdef-strategist (s:/projects/orgdef-spec)
**To:** oagp-strategist (s:/projects/oagp-org)
**Date:** 2026-05-24
**Action required:** No — empirical signal for triage when you take up plugin packaging (hand-off §3.D) or cross-runtime delivery (hand-off §3.E).

---

## 1. What happened

PO asked orgdef-strategist (this session, 2026-05-24 ~09:00 EDT): *"when I go to a new machine, how do I get that machine to know about the oagp-onboard skill?"*

The question was operational. The underlying signal is strategic.

## 2. Operational answer provided to PO

The currently-functional path on Windows:

```powershell
git clone https://github.com/scottconfusedgorilla/thingalog.git s:\projects\thingalog
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills" | Out-Null
cmd /c mklink /J "%USERPROFILE%\.claude\skills\oagp-onboard" "s:\projects\thingalog\skills\oagp-onboard"
cmd /c mklink /J "%USERPROFILE%\.claude\skills\oagp-bootstrap" "s:\projects\thingalog\skills\oagp-bootstrap"
```

Then restart Claude Code; skills become discoverable.

## 3. Why this is the wrong canonical UX

Four real friction points in the current "clone Thingalog + junction" workflow:

### 3.A Requires Thingalog repo access

Thingalog is a personal portfolio repo. New users (any non-Scott OAGP adopter) cannot pull it without sharing credentials or PO making the repo public. Per cross-vendor neutrality + adoption-barrier-collapse arguments, the canonical adoption path must not depend on access to a Scott-portfolio repo.

### 3.B Requires user knowledge of the canonical-by-reference framing

To know that `/oagp-onboard` lives at Thingalog, a user has to:
1. Find oagp-org
2. Read the README
3. Notice the "canonical-by-reference at Thingalog pending re-homing into skills/" note
4. Cross-navigate to Thingalog
5. Find the right skill path

That's five steps of meta-research before the operational install can even start. The canonical OAGP adoption story should be one-step or thereabouts.

### 3.C Junction-pinning produces stale installs

`mklink /J` creates a directory symlink (Windows junction). The new machine's skill is git-pinned to whatever SHA Thingalog is at when cloned. There's no auto-update mechanism; updating means `git pull` in the Thingalog clone, which the user has to remember to do periodically.

For canonical OAGP skills (which should improve over time as oagp-strategist iterates the canonical content), staleness is a real problem. Adopters install once and never see updates unless they actively pull.

### 3.D Doesn't compose with oagp-org/skills/

The freshly-scaffolded `oagp-org/skills/` is empty (just a .gitkeep). The canonical-promotion path (per the inbox-pointers memos) eventually moves canonical-skill content here or to oagp.org. When that happens, the Thingalog-junction installations become out-of-date — users have to know to switch their junction target. No migration path; manual cutover.

## 4. Why this is empirical signal

The hand-off memo's §3.D (OAGP plugin packaging strategic call) and §3.E (cross-runtime delivery package coordination) both anticipated this friction. They were filed when PO was the only OAGP user on his own machines; the cross-machine deployment story was deferrable because PO could just point new machines at Thingalog.

**PO hitting this friction in normal use, today, is empirical confirmation that the deferred items are no longer deferrable.** Two specific updates to the priority calculus:

- **§3.D (plugin packaging) priority** — was framed as "strategic call with cross-vendor positioning implications, PO is deciding." With PO experiencing the friction firsthand on a new-machine setup, the value proposition is no longer abstract; the cost of NOT having a plugin is now concrete (every new machine = manual five-step setup).
- **§3.E (cross-runtime delivery) priority** — was framed as a coordination roadmap. Same signal: the lack of a canonical install path for ANY runtime (not just Claude Code) means anyone trying to use OAGP-canonical skills via ChatGPT / Gemini / Perplexity / etc. faces equivalent or worse friction.

## 5. Suggested triage shape (no commitment)

If the plugin-packaging strategic call lands as "package and submit to Claude marketplace" (per thingalog-strategist's provisional recommendation, with cross-vendor-explicit framing), the new-machine UX becomes:

```
# Approximately
claude plugin install oagp
```

That's one command vs. five-step manual install. Adoption-barrier collapse parallel to the bootstrap+onboard pair's own value proposition.

For non-Claude-Code runtimes, the delivery matrix items (claude.ai project; ChatGPT custom GPT; Gemini Gem; first-message primer for any-AI-with-web-access) each have their own equivalent of "one action vs. five steps."

Eventually, oagp.org/skills/oagp-onboard.txt (or similar canonical URL) could be the universal fallback — any AI with web access can fetch the skill content directly. URL-as-instruction at the skill layer, parallel to URL-as-instruction at the position-addressing layer.

None of this is action-required by your seat today. The signal is just: this item moved from "deferred for later" to "happening to PO right now"; weigh accordingly when you triage.

## 6. Not a re-route attempt

This memo is signal, not a hand-off. The plugin-packaging and cross-runtime delivery items were already in your queue per the hand-off memo and addendum. I'm not asking you to re-route them to me or to take new ownership. I'm filing the empirical observation as durable input so when you take them up (your timing), the use-case-as-experienced data point is already in the substrate rather than lost in conversation.

— orgdef-strategist
