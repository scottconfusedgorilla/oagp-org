"""Conformance tests for run_seat() autonomous dispatch (run_seat.py).

Maps to the nine conformance tests in the v0.2 build-direction memo
(2026-05-29-1300 §6). Test 8 (Workflows delegation) is deferred with the live
backend and is marked skip.
"""

from datetime import datetime
from pathlib import Path

import pytest

from oagp_agent_sdk import (
    BoundAgentDispatchError,
    RoledefResolutionError,
    StubBackend,
    run_seat,
)
from oagp_agent_sdk.authority import DIRECTOR_CAPABLE_TOOLS, Tier1ViolationError
from oagp_agent_sdk.guard import BOUND_AGENT_ENV_MARKER


FIXED_NOW = datetime(2026, 5, 29, 14, 30, 0)


def _run(orgdef_path, position_id="vacant-role", **kw):
    """vacant-role has an embedded roledef and NO url -> no network fetch."""
    backend = kw.pop("backend", None) or StubBackend()
    kw.setdefault("now", FIXED_NOW)
    record = run_seat(orgdef_path, position_id, backend=backend, **kw)
    return record, backend


# 1 — default produces a subagent with no push/merge-capable tools
def test_conformance_1_default_has_no_capable_tools(orgdef_path):
    record, _ = _run(orgdef_path)
    assert record.tier == 1
    assert not (set(record.toolset) & DIRECTOR_CAPABLE_TOOLS)


# 2 — propose-only bind-context block present by default
def test_conformance_2_propose_only_block_present(orgdef_path):
    record, _ = _run(orgdef_path)
    body = record.agent_file.read_text(encoding="utf-8")
    assert "Tier 1" in body
    assert "propose-only" in body.lower()


# 3 — elevation requires the explicit param; absent it, no capable tools
def test_conformance_3_no_capable_tools_without_grant(orgdef_path):
    record, _ = _run(orgdef_path, tools=["Read", "Write"])
    assert "Bash" not in record.toolset
    # And requesting a capable tool at tier-1 is refused outright
    with pytest.raises(Tier1ViolationError):
        _run(orgdef_path, tools=["Read", "Bash"])


# 4 — elevation fires a bind-event memo recording the grant
def test_conformance_4_elevation_fires_bind_event_memo(orgdef_path):
    record, _ = _run(orgdef_path, grant_director_actions=["commit", "push"])
    assert record.tier == 2
    assert "Bash" in record.toolset
    assert record.bind_event_memo is not None and record.bind_event_memo.exists()
    import json
    env = json.loads(record.bind_event_memo.read_text(encoding="utf-8"))
    assert env["metadata"]["granted_authority"] == ["commit", "push"]
    body = record.agent_file.read_text(encoding="utf-8")
    assert "Tier 2" in body and "commit, push" in body


# 5 — a bound-agent context cannot invoke run_seat() (Tier-3 floor)
def test_conformance_5_tier3_floor_blocks_nested_dispatch(orgdef_path, monkeypatch):
    monkeypatch.setenv(BOUND_AGENT_ENV_MARKER, "1")
    with pytest.raises(BoundAgentDispatchError):
        run_seat(orgdef_path, "vacant-role", backend=StubBackend())


def test_conformance_5b_tier3_floor_blocks_bind(orgdef_path, monkeypatch):
    """bind() itself is also inert in a bound-agent context."""
    from oagp_agent_sdk import bind
    monkeypatch.setenv(BOUND_AGENT_ENV_MARKER, "1")
    with pytest.raises(BoundAgentDispatchError):
        bind(orgdef_path, "vacant-role")


# 6 — autonomous URL fetch failure fails closed absent explicit fallback
def test_conformance_6_fail_closed_resolution(orgdef_path):
    # test-tester has a URL pointing at example.invalid (fails) + embedded.
    with pytest.raises(RoledefResolutionError):
        run_seat(orgdef_path, "test-tester", backend=StubBackend(), now=FIXED_NOW)


def test_conformance_6b_explicit_fallback_opt_in(orgdef_path):
    record, _ = _run(orgdef_path, position_id="test-tester", allow_embedded_fallback=True)
    assert record.bind_result.roledef_source == "embedded"


# 7 — a bind-event memo is emitted on every autonomous dispatch
def test_conformance_7_bind_event_memo_always(orgdef_path):
    record, _ = _run(orgdef_path)  # tier-1, propose-only
    assert record.bind_event_memo is not None and record.bind_event_memo.exists()


# 8 — Workflows delegation: the Claude Code backend generates a workflow that
# dispatches via agentType (so the bound toolset governs). The live run is
# environment-dependent (a fresh session may be needed for agentType to
# resolve); here we verify the generated artifact delegates correctly.
def test_conformance_8_workflows_delegation(orgdef_path):
    from oagp_agent_sdk import WorkflowsBackend
    backend = WorkflowsBackend()
    record, _ = _run(orgdef_path, backend=backend)
    script_path = Path(record.dispatch_handle.detail["workflow_script"])
    assert script_path.exists()
    script = script_path.read_text(encoding="utf-8")
    # Delegates over the native dispatcher (agent()) and via agentType (so the
    # bound tools: frontmatter — not an inline prompt — governs capability).
    assert "await agent(" in script
    assert f'agentType: "{record.agent_name}"' in script
    assert "export const meta" in script


# 9 — runtime-neutral interface; backend is swappable
def test_conformance_9_backend_swappable(orgdef_path):
    backend = StubBackend()
    record, _ = _run(orgdef_path, backend=backend)
    assert record.backend == "stub"
    assert len(backend.dispatches) == 1


# Tier-3 marker propagation: dispatched env carries the bound-agent marker
def test_dispatch_env_carries_bound_agent_marker(orgdef_path):
    record, backend = _run(orgdef_path)
    handle = backend.dispatches[0]
    assert handle.env.get(BOUND_AGENT_ENV_MARKER) == "1"


# DispatchRecord captures the org-state SHA when in a git repo (None otherwise)
def test_dispatch_record_org_state_sha_field_present(orgdef_path):
    record, _ = _run(orgdef_path)
    # tmp_path is not a git repo -> None; field exists regardless
    assert hasattr(record, "org_state_sha")


def test_withheld_tools_recorded_at_tier1(orgdef_path):
    record, _ = _run(orgdef_path)
    assert "Bash" in record.withheld_tools


def test_emit_memo_false_skips_memo(orgdef_path):
    record, _ = _run(orgdef_path, emit_memo=False)
    assert record.bind_event_memo is None
