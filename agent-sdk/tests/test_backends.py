"""Unit tests for dispatch backends (backends.py)."""

from pathlib import Path

import pytest

from oagp_agent_sdk.backends import (
    StubBackend,
    WorkflowsBackend,
    render_dispatch_workflow,
    select_backend,
)


class TestRenderDispatchWorkflow:
    def test_has_meta_and_agent_call(self):
        script = render_dispatch_workflow(
            agent_name="security-tester", brief="Do X.", tier=1, granted_authority=[]
        )
        assert "export const meta" in script
        assert "await agent(" in script

    def test_dispatches_via_agenttype_not_inline_prompt(self):
        """The structural Tier-1 bound rides on the agent file's tools:
        frontmatter, which only applies when dispatched via agentType."""
        script = render_dispatch_workflow(
            agent_name="security-tester", brief="Do X.", tier=1, granted_authority=[]
        )
        assert 'agentType: "security-tester"' in script

    def test_brief_embedded(self):
        script = render_dispatch_workflow(
            agent_name="a", brief="Review the auth code.", tier=1, granted_authority=[]
        )
        assert "Review the auth code." in script

    def test_tier2_authority_in_meta(self):
        script = render_dispatch_workflow(
            agent_name="a", brief="x", tier=2, granted_authority=["commit", "push"]
        )
        assert "commit, push" in script
        assert 'granted_authority: ["commit", "push"]' in script

    def test_default_brief_when_none(self):
        script = render_dispatch_workflow(
            agent_name="a", brief=None, tier=1, granted_authority=[]
        )
        assert "bind context" in script.lower()


class TestWorkflowsBackend:
    def test_writes_workflow_script_next_to_agent_file(self, tmp_path: Path):
        agent_file = tmp_path / "security-tester.md"
        agent_file.write_text("---\nname: security-tester\n---\nbody", encoding="utf-8")
        backend = WorkflowsBackend()
        handle = backend.dispatch(agent_file, brief="Do X.", env={"OAGP_BOUND_AGENT": "1"})
        script_path = Path(handle.detail["workflow_script"])
        assert script_path.exists()
        assert script_path.name == "security-tester.workflow.js"
        assert handle.launched is False

    def test_handle_records_tier3_floor_basis(self, tmp_path: Path):
        agent_file = tmp_path / "a.md"
        agent_file.write_text("x", encoding="utf-8")
        handle = WorkflowsBackend().dispatch(agent_file, brief="x", env={})
        assert "package-absence" in handle.detail["tier3_floor"]


class TestSelectBackend:
    def test_explicit_stub(self):
        assert isinstance(select_backend("stub"), StubBackend)

    def test_explicit_workflows(self):
        assert isinstance(select_backend("workflows"), WorkflowsBackend)
        assert isinstance(select_backend("claude-code"), WorkflowsBackend)

    def test_auto_detects_claude_code(self, monkeypatch):
        monkeypatch.setenv("CLAUDECODE", "1")
        assert isinstance(select_backend("auto"), WorkflowsBackend)

    def test_auto_falls_back_to_stub(self, monkeypatch):
        for var in ("CLAUDECODE", "CLAUDE_CODE", "CLAUDE_AGENT_SDK"):
            monkeypatch.delenv(var, raising=False)
        assert isinstance(select_backend("auto"), StubBackend)
