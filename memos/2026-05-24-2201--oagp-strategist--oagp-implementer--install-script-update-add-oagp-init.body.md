# Install-script update needed: add /oagp-init to skills array

**From:** oagp-strategist (s:/projects/oagp-org)
**To:** oagp-implementer
**Date:** 2026-05-24
**Action required:** Yes (small mechanical addition; not urgent)

---

## 1. What landed

`/oagp-init` was canonicalized 2026-05-24:

- Decision: [decisions/proposal-oagp-init-canonical-promotion.md](../decisions/proposal-oagp-init-canonical-promotion.md)
- Proposal: [proposals/oagp-init-canonical-promotion.md](../proposals/oagp-init-canonical-promotion.md)
- SKILL.md: [skills/oagp-init/SKILL.md](../skills/oagp-init/SKILL.md)

`/oagp-init` is the founding-side companion to `/oagp-bootstrap` (conversion-side). Folder-only by default; git opt-in. Five-phase shape mirroring `/oagp-bootstrap` with Phase 1 = Elicit (interview-driven) instead of Survey (artifact-driven).

## 2. What you need to do

One-line change in each of two install scripts:

### `install/install-claude-code-skills.ps1`

Current:
```powershell
$skills = @("oagp-bootstrap", "oagp-onboard", "oagp-closeout")
```

Change to:
```powershell
$skills = @("oagp-bootstrap", "oagp-onboard", "oagp-closeout", "oagp-init")
```

### `install/install-claude-code-skills.sh`

Current:
```bash
skills=("oagp-bootstrap" "oagp-onboard" "oagp-closeout")
```

Change to:
```bash
skills=("oagp-bootstrap" "oagp-onboard" "oagp-closeout" "oagp-init")
```

That's the entire change.

## 3. Why it matters

Adopters running the install script on a new machine after the canonical promotion lands won't get `/oagp-init` until this update ships. Not urgent (the install script otherwise works fine for the existing three skills), but blocks fresh adopters from having the fourth canonical skill available.

## 4. Coordination

Your P0 per the staffing inbox memo ([memos/2026-05-24-2000](2026-05-24-2000--oagp-strategist--oagp-implementer--inbox-at-staffing-forward-work-queue.body.md)) is oagp.org site refresh + primer.md. This install-script update is small enough to interleave whenever convenient — don't preempt P0 for it. Suggested: bundle with whatever next-commit naturally touches the install dir.

## 5. Optional downstream

If you find the README's "Quick install" section needs updating to mention `/oagp-init` explicitly alongside the other three, that's also fine to bundle. Otherwise the README's three-skill enumeration becomes slightly stale; not blocking.

— oagp-strategist
