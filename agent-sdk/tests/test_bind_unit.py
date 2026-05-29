"""Unit tests for oagp_agent_sdk.bind internals.

These exercise the pure helpers (_slugify, _yaml_escape, _render_frontmatter,
_find_position, _resolve_roledef) without writing any files or hitting the
network. Integration tests live in test_bind_integration.py.
"""

import pytest

from oagp_agent_sdk.bind import (
    _slugify,
    _yaml_escape,
    _render_frontmatter,
    _find_position,
    _resolve_roledef,
)


# -- _slugify --------------------------------------------------------------

class TestSlugify:
    def test_lowercases(self):
        assert _slugify("SecurityTester") == "securitytester"

    def test_replaces_non_alnum_with_hyphen(self):
        assert _slugify("security tester") == "security-tester"
        assert _slugify("security_tester") == "security-tester"

    def test_collapses_consecutive_hyphens(self):
        assert _slugify("security--tester") == "security-tester"
        assert _slugify("security   tester") == "security-tester"

    def test_strips_leading_trailing_hyphens(self):
        assert _slugify("-security-tester-") == "security-tester"

    def test_preserves_existing_single_hyphens(self):
        assert _slugify("security-tester") == "security-tester"

    def test_collapses_special_chars(self):
        assert _slugify("foo!@#bar") == "foo-bar"


# -- _yaml_escape ----------------------------------------------------------

class TestYamlEscape:
    def test_wraps_in_quotes(self):
        assert _yaml_escape("hello") == '"hello"'

    def test_escapes_double_quotes(self):
        assert _yaml_escape('he said "hi"') == '"he said \\"hi\\""'

    def test_escapes_backslash(self):
        assert _yaml_escape("path\\to\\file") == '"path\\\\to\\\\file"'

    def test_collapses_newlines_to_spaces(self):
        assert _yaml_escape("line1\nline2") == '"line1 line2"'


# -- _render_frontmatter ---------------------------------------------------

class TestRenderFrontmatter:
    def test_minimal(self):
        out = _render_frontmatter({"name": "foo", "description": "bar"})
        assert out.startswith("---\n")
        assert out.endswith("\n---")
        assert 'name: "foo"' in out
        assert 'description: "bar"' in out

    def test_skips_none(self):
        out = _render_frontmatter({"name": "foo", "tools": None})
        assert "tools" not in out

    def test_skips_empty_list(self):
        out = _render_frontmatter({"name": "foo", "tools": []})
        assert "tools" not in out

    def test_list_renders_as_comma_separated(self):
        out = _render_frontmatter({"tools": ["Read", "Write", "Bash"]})
        assert "tools: Read, Write, Bash" in out

    def test_bool_renders_lowercase(self):
        out = _render_frontmatter({"flag": True, "other": False})
        assert "flag: true" in out
        assert "other: false" in out

    def test_numeric_passthrough(self):
        out = _render_frontmatter({"maxTurns": 25, "ratio": 0.5})
        assert "maxTurns: 25" in out
        assert "ratio: 0.5" in out

    def test_initial_prompt_uses_literal_block(self):
        out = _render_frontmatter({"initialPrompt": "line1\nline2\nline3"})
        assert "initialPrompt: |" in out
        assert "  line1" in out
        assert "  line2" in out
        assert "  line3" in out


# -- _find_position --------------------------------------------------------

class TestFindPosition:
    def test_finds_existing_position(self):
        orgdef = {
            "items": [
                {"type": "orgdef:Position", "id": "alpha", "name": "Alpha"},
                {"type": "orgdef:Position", "id": "beta", "name": "Beta"},
                {"type": "orgdef:Organization", "id": "org", "name": "Org"},
            ]
        }
        pos = _find_position(orgdef, "beta")
        assert pos["id"] == "beta"
        assert pos["name"] == "Beta"

    def test_missing_position_raises(self):
        orgdef = {
            "items": [
                {"type": "orgdef:Position", "id": "alpha"},
            ]
        }
        with pytest.raises(ValueError, match="Position 'missing' not found"):
            _find_position(orgdef, "missing")

    def test_error_lists_available_positions(self):
        orgdef = {
            "items": [
                {"type": "orgdef:Position", "id": "alpha"},
                {"type": "orgdef:Position", "id": "beta"},
                {"type": "orgdef:Organization", "id": "org"},
            ]
        }
        with pytest.raises(ValueError) as exc_info:
            _find_position(orgdef, "missing")
        # Available positions enumerated; org metadata excluded
        assert "alpha" in str(exc_info.value)
        assert "beta" in str(exc_info.value)


# -- _resolve_roledef ------------------------------------------------------

class TestResolveRoledef:
    def test_embedded_only(self):
        position = {
            "id": "test",
            "role_definition": {
                "job_definition": {"id": "test-role", "version": "1.0"}
            }
        }
        roledef, source, url = _resolve_roledef(position)
        assert roledef == {"id": "test-role", "version": "1.0"}
        assert source == "embedded"
        assert url is None

    def test_url_fetch_failure_falls_back_to_embedded(self, capsys):
        position = {
            "id": "test",
            "role_definition": {
                "url": "https://example.invalid/nonexistent.json",
                "job_definition": {"id": "fallback", "version": "0.1"}
            }
        }
        roledef, source, url = _resolve_roledef(position)
        assert roledef["id"] == "fallback"
        assert source == "embedded"
        assert url == "https://example.invalid/nonexistent.json"
        captured = capsys.readouterr()
        assert "URL fetch failed" in captured.out

    def test_no_url_no_embedded_raises(self):
        position = {
            "id": "naked",
            "role_definition": {},
        }
        with pytest.raises(ValueError, match="no resolvable roledef"):
            _resolve_roledef(position)

    def test_missing_role_definition_raises(self):
        position = {"id": "barren"}
        with pytest.raises(ValueError, match="no resolvable roledef"):
            _resolve_roledef(position)
