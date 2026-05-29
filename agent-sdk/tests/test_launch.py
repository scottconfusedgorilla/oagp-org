"""Tests for the autonomous-dispatch launcher (launch.py).

Covers the two ratified conformance tests from the governance addendum
build-directive §5:
  (a) the autonomous path dispatches via agentType (never inline) — inline is
      barred for autonomous use.
  (b) Tier-2 autonomous dispatch refuses absent verified package-absence.
"""

from datetime import datetime
from pathlib import Path

import pytest

from oagp_agent_sdk import (
    ClaudeCliLauncher,
    StubSessionLauncher,
    Tier2GateError,
    launch_seat,
    verify_package_absent,
)


FIXED_NOW = datetime(2026, 5, 29, 18, 0, 0)


def _launch(orgdef_path, position_id="vacant-role", **kw):
    launcher = kw.pop("session_launcher", None) or StubSessionLauncher()
    kw.setdefault("now", FIXED_NOW)
    kw.setdefault("agents_root", None)
    if kw["agents_root"] is None:
        kw.pop("agents_root")
    rec = launch_seat(orgdef_path, position_id, session_launcher=launcher, **kw)
    return rec, launcher


# --- verify_package_absent ------------------------------------------------

class TestVerifyPackageAbsent:
    def test_absent_when_not_importable(self):
        """A bare subprocess python without src on PYTHONPATH cannot import the
        package → reported absent (gate satisfied)."""
        # Use a python that definitely lacks the package on its path.
        assert verify_package_absent("python") is True

    def test_failsafe_when_python_missing(self):
        """If the checker can't even run, fail safe to 'not verified absent'."""
        assert verify_package_absent("definitely-not-a-real-python-xyz") is False


# --- Ruling A: autonomous path is agentType, never inline -----------------

def test_conformance_a_autonomous_dispatches_via_agenttype(orgdef_path):
    rec, _ = _launch(orgdef_path)
    # The dispatch went through the WorkflowsBackend (agentType), not inline.
    assert rec.dispatch.backend == "workflows"
    script = Path(rec.dispatch.dispatch_handle.detail["workflow_script"]).read_text(encoding="utf-8")
    assert f'agentType: "{rec.dispatch.agent_name}"' in script
    assert "await agent(" in script


def test_launcher_builds_fresh_session_command(orgdef_path):
    rec, launcher = _launch(orgdef_path)
    assert rec.launch_handle.launched is False  # stub does not spawn
    assert rec.launch_handle.command  # a fresh-session command was constructed
    assert len(launcher.launches) == 1


# --- Ruling B: Tier-2 gating ----------------------------------------------

def test_conformance_b_tier2_refused_without_verified_package_absence(orgdef_path):
    with pytest.raises(Tier2GateError, match="package-absent"):
        launch_seat(
            orgdef_path,
            "vacant-role",
            grant_director_actions=["commit"],
            package_absence_verifier=lambda: False,  # gate not satisfied
            session_launcher=StubSessionLauncher(),
            now=FIXED_NOW,
        )


def test_tier2_proceeds_when_package_absence_verified(orgdef_path):
    rec, _ = _launch(
        orgdef_path,
        grant_director_actions=["commit"],
        package_absence_verifier=lambda: True,  # gate satisfied
    )
    assert rec.tier == 2
    assert rec.tier2_gate_checked is True
    assert rec.tier2_gate_passed is True
    assert "Bash" in rec.dispatch.toolset


def test_tier1_needs_no_gate(orgdef_path):
    rec, _ = _launch(orgdef_path)
    assert rec.tier == 1
    assert rec.tier2_gate_checked is False
    assert rec.tier2_gate_passed is None


def test_tier2_gate_uses_real_verifier_by_default(orgdef_path):
    """With no injected verifier, the default runs verify_package_absent against
    `dispatch_python`. Pointing at a missing python fails safe → refuse."""
    with pytest.raises(Tier2GateError):
        launch_seat(
            orgdef_path,
            "vacant-role",
            grant_director_actions=["push"],
            dispatch_python="definitely-not-a-real-python-xyz",
            session_launcher=StubSessionLauncher(),
            now=FIXED_NOW,
        )


# --- ClaudeCliLauncher ----------------------------------------------------

class TestClaudeCliLauncher:
    def test_build_command_references_workflow_script(self, tmp_path):
        wf = tmp_path / "x.workflow.js"
        cmd = ClaudeCliLauncher.build_command(wf, "x")
        assert str(wf) in cmd

    def test_execute_false_does_not_spawn(self, tmp_path):
        wf = tmp_path / "x.workflow.js"
        wf.write_text("// wf", encoding="utf-8")
        handle = ClaudeCliLauncher(execute=False).launch(wf, agent_name="x")
        assert handle.launched is False
        assert handle.command

    def test_execute_true_missing_binary_raises_with_command(self, tmp_path):
        wf = tmp_path / "x.workflow.js"
        wf.write_text("// wf", encoding="utf-8")
        with pytest.raises(RuntimeError, match="not on PATH"):
            ClaudeCliLauncher(execute=True, claude_bin="definitely-not-claude-xyz").launch(
                wf, agent_name="x"
            )
