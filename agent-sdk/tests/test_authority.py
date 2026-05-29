"""Unit tests for the Tier-1/Tier-2 authority construction (authority.py)."""

import pytest

from oagp_agent_sdk.authority import (
    DEFAULT_PROPOSE_TOOLS,
    DIRECTOR_CAPABLE_TOOLS,
    Tier1ViolationError,
    UnknownDirectorActionError,
    authority_block,
    construct_toolset,
    resolve_tier,
    validate_director_actions,
)


class TestResolveTier:
    def test_no_grant_is_tier1(self):
        assert resolve_tier(None) == 1
        assert resolve_tier([]) == 1

    def test_grant_is_tier2(self):
        assert resolve_tier(["commit"]) == 2


class TestValidateDirectorActions:
    def test_none_and_empty(self):
        assert validate_director_actions(None) == []
        assert validate_director_actions([]) == []

    def test_normalizes_case_and_whitespace(self):
        assert validate_director_actions([" Commit ", "PUSH"]) == ["commit", "push"]

    def test_unknown_action_raises(self):
        with pytest.raises(UnknownDirectorActionError, match="frobnicate"):
            validate_director_actions(["commit", "frobnicate"])


class TestConstructToolset:
    def test_tier1_default_toolset_has_no_capable_tools(self):
        """Conformance: default produces no push/merge-capable tools."""
        toolset, tier, withheld = construct_toolset(None, None)
        assert tier == 1
        assert toolset == list(DEFAULT_PROPOSE_TOOLS)
        assert not (set(toolset) & DIRECTOR_CAPABLE_TOOLS)
        assert "Bash" in withheld

    def test_tier1_rejects_requested_capable_tool(self):
        """Conformance: Tier-1 cannot smuggle in Director-capable tools."""
        with pytest.raises(Tier1ViolationError, match="Bash"):
            construct_toolset(["Read", "Write", "Bash"], None)

    def test_tier1_custom_safe_tools_preserved(self):
        toolset, tier, _ = construct_toolset(["Read", "Grep"], None)
        assert tier == 1
        assert toolset == ["Read", "Grep"]

    def test_tier2_adds_bash_when_absent(self):
        toolset, tier, withheld = construct_toolset(["Read", "Write"], ["commit"])
        assert tier == 2
        assert "Bash" in toolset
        assert withheld == []

    def test_tier2_preserves_requested_and_does_not_duplicate_bash(self):
        toolset, tier, _ = construct_toolset(["Read", "Bash"], ["push"])
        assert tier == 2
        assert toolset.count("Bash") == 1


class TestAuthorityBlock:
    def test_tier1_is_propose_only(self):
        block = authority_block(1, [])
        assert "Tier 1" in block
        assert "propose-only" in block.lower()
        assert "cannot dispatch, bind, or elevate" in block

    def test_tier2_names_granted_actions(self):
        block = authority_block(2, ["commit", "push"])
        assert "Tier 2" in block
        assert "commit, push" in block
        assert "cannot dispatch, bind, or elevate" in block
