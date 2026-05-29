"""Reproducible run_seat() autonomous-dispatch demo (Tier-1 propose-only).

Generates the dispatch artifacts for a propose-only `doc-reviewer` bound agent:
the subagent file, the bind-event audit memo, and the Claude Code workflow
script that dispatches it via agentType.

Run:
    cd agent-sdk
    PYTHONPATH=src python examples/run_demo.py [AGENTS_ROOT]

AGENTS_ROOT defaults to the agent file landing next to this demo (so the run is
self-contained). To make the bound agent dispatchable by Claude Code Workflows,
point AGENTS_ROOT at your project's `.claude/agents/` AND run the generated
workflow from a FRESH session (see examples/README.md — the session-start rule:
agentType only resolves agent files that pre-existed the dispatching session).
"""

import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from oagp_agent_sdk import run_seat, select_backend  # noqa: E402

HERE = Path(__file__).resolve().parent
DEMO_ORGDEF = HERE / "demo-orgdef.opencatalog"
OUTPUT = HERE / "demo-output"

BRIEF = f"""# Documentation review engagement (propose-only demo)

Target document: {HERE.parent / 'README.md'}
Engagement workspace: {OUTPUT}

Read the target README fully. Produce a concrete improvement proposal per your
output contract and WRITE it to {OUTPUT / 'review-proposal.md'}. Quote the exact
passage for every proposed change; group by severity (blocking / improvement /
nit); 4-8 proposals. Propose-only -- do NOT edit the README. Stop when written.
"""


def main() -> None:
    agents_root = Path(sys.argv[1]) if len(sys.argv) > 1 else (OUTPUT / "agents")
    rec = run_seat(
        DEMO_ORGDEF,
        "doc-reviewer",
        brief=BRIEF,
        backend=select_backend("workflows"),
        agents_root=agents_root,
        tools=["Read", "Write", "Glob", "Grep"],  # propose-only; no Bash
        now=datetime(2026, 5, 29, 16, 0, 0),
    )
    print(f"tier             : {rec.tier} (propose-only)" if not rec.granted_authority
          else f"tier             : {rec.tier} ({rec.granted_authority})")
    print(f"toolset          : {rec.toolset}")
    print(f"withheld         : {rec.withheld_tools}")
    print(f"org_state_sha    : {rec.org_state_sha}")
    print(f"agent_file       : {rec.agent_file}")
    print(f"bind_event_memo  : {rec.bind_event_memo}")
    print(f"backend          : {rec.backend}")
    print(f"workflow_script  : {rec.dispatch_handle.detail.get('workflow_script')}")
    print()
    print("Next: run the workflow script via Claude Code Workflows FROM A FRESH")
    print("SESSION (so agentType resolves the just-written agent file).")


if __name__ == "__main__":
    main()
