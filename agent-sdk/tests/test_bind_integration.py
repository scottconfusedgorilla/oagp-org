"""Integration tests for oagp_agent_sdk.bind.

These exercise the full bind() path against a fixture orgdef. No external
network calls are made (the fixture's URL points at example.invalid, which
fails fast and triggers the embedded fallback).
"""

from pathlib import Path

import pytest

from oagp_agent_sdk import bind, BindResult


FIXTURE_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixture_project(tmp_path: Path) -> Path:
    """Lay out a temporary OAGP-shaped project rooted at tmp_path.

    Structure:
        tmp_path/
          org/
            minimal-orgdef.opencatalog   (copied from tests/fixtures/)
          memos/                          (empty)

    Returns the project root path.
    """
    org_dir = tmp_path / "org"
    org_dir.mkdir()
    (tmp_path / "memos").mkdir()

    src = FIXTURE_DIR / "minimal-orgdef.opencatalog"
    dst = org_dir / "minimal-orgdef.opencatalog"
    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    return tmp_path


def test_bind_writes_agent_file(fixture_project: Path):
    result = bind(
        orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
        position_id="test-tester",
    )
    assert isinstance(result, BindResult)
    assert result.agent_file.exists()
    assert result.agent_file.name == "test-tester.md"
    # Default agents_root relative to project root
    assert result.agent_file.parent == fixture_project / ".claude" / "agents"


def test_bind_result_fields_populated(fixture_project: Path):
    result = bind(
        orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
        position_id="test-tester",
    )
    assert result.agent_name == "test-tester"
    assert result.org_name == "Test Org"
    assert result.org_id == "test-org"
    assert result.position_id == "test-tester"
    assert result.position_name == "Test Tester"
    assert result.position_status == "staffed"
    assert result.roledef_id == "test-role"
    assert result.roledef_version == "0.1.0"
    # The fixture URL is example.invalid; URL fetch fails -> embedded fallback
    assert result.roledef_source == "embedded"
    assert result.roledef_url == "https://example.invalid/nonexistent-roledef.json"


def test_context_tag_appended_with_single_hyphen(fixture_project: Path):
    """Empirical lesson: VSCode agent view rejects double-hyphen separators."""
    result = bind(
        orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
        position_id="test-tester",
        context_tag="tt-2026-05-16",
    )
    assert result.agent_name == "test-tester-tt-2026-05-16"
    assert "--" not in result.agent_name


def test_initial_prompt_simplifies_dispatch_hint(fixture_project: Path):
    result_with = bind(
        orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
        position_id="test-tester",
        initial_prompt="Do the thing.",
    )
    assert result_with.dispatch_hint == "@test-tester"

    result_without = bind(
        orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
        position_id="test-tester",
    )
    assert "engagement brief" in result_without.dispatch_hint


def test_frontmatter_contains_expected_fields(fixture_project: Path):
    result = bind(
        orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
        position_id="test-tester",
        tools=["Read", "Write"],
        initial_prompt="Hello.",
    )
    content = result.agent_file.read_text(encoding="utf-8")
    assert content.startswith("---\n")
    assert 'name: "test-tester"' in content
    assert "tools: Read, Write" in content
    assert 'model: "inherit"' in content
    assert 'permissionMode: "acceptEdits"' in content
    assert "initialPrompt: |" in content


def test_body_contains_synthesized_sections(fixture_project: Path):
    result = bind(
        orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
        position_id="test-tester",
    )
    body = result.agent_file.read_text(encoding="utf-8")
    assert "# Bind context" in body
    assert "# Identity" in body
    assert "# Voice" in body
    assert "# Guardrails" in body
    assert "# Conversation rules" in body
    assert "# Workflow" in body
    assert "# Output contract" in body


def test_extra_context_appears_in_body(fixture_project: Path):
    result = bind(
        orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
        position_id="test-tester",
        extra_context="Time-travel to commit deadbeef.",
    )
    body = result.agent_file.read_text(encoding="utf-8")
    assert "# Additional context" in body
    assert "Time-travel to commit deadbeef." in body


def test_missing_position_raises(fixture_project: Path):
    with pytest.raises(ValueError, match="Position 'nonexistent' not found"):
        bind(
            orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
            position_id="nonexistent",
        )


def test_position_without_roledef_raises(fixture_project: Path):
    with pytest.raises(ValueError, match="no resolvable roledef"):
        bind(
            orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
            position_id="no-roledef",
        )


def test_absolute_agents_root_respected(fixture_project: Path, tmp_path: Path):
    elsewhere = tmp_path / "elsewhere"
    result = bind(
        orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
        position_id="test-tester",
        agents_root=elsewhere,
    )
    assert result.agent_file.parent == elsewhere
    assert result.agent_file.exists()


def test_color_defaults_when_roledef_id_unknown(fixture_project: Path):
    """test-role is not in the _ROLE_COLOR map, so color defaults to cyan."""
    result = bind(
        orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
        position_id="test-tester",
    )
    content = result.agent_file.read_text(encoding="utf-8")
    assert 'color: "cyan"' in content


def test_explicit_color_overrides_default(fixture_project: Path):
    result = bind(
        orgdef_path=fixture_project / "org" / "minimal-orgdef.opencatalog",
        position_id="test-tester",
        color="magenta",
    )
    content = result.agent_file.read_text(encoding="utf-8")
    assert 'color: "magenta"' in content
