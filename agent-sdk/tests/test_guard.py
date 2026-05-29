"""Unit tests for the Tier-3 non-delegable-dispatch floor (guard.py)."""

import pytest

from oagp_agent_sdk.guard import (
    BOUND_AGENT_ENV_MARKER,
    BoundAgentDispatchError,
    assert_dispatch_allowed,
    is_bound_agent_context,
)


class TestIsBoundAgentContext:
    def test_absent_marker_is_not_bound(self, monkeypatch):
        monkeypatch.delenv(BOUND_AGENT_ENV_MARKER, raising=False)
        assert is_bound_agent_context() is False

    @pytest.mark.parametrize("val", ["1", "true", "TRUE", "yes", "Yes"])
    def test_truthy_markers(self, monkeypatch, val):
        monkeypatch.setenv(BOUND_AGENT_ENV_MARKER, val)
        assert is_bound_agent_context() is True

    @pytest.mark.parametrize("val", ["", "0", "false", "no", "off"])
    def test_falsey_markers(self, monkeypatch, val):
        monkeypatch.setenv(BOUND_AGENT_ENV_MARKER, val)
        assert is_bound_agent_context() is False


class TestAssertDispatchAllowed:
    def test_allows_when_not_bound(self, monkeypatch):
        monkeypatch.delenv(BOUND_AGENT_ENV_MARKER, raising=False)
        assert_dispatch_allowed()  # no raise

    def test_raises_when_bound(self, monkeypatch):
        monkeypatch.setenv(BOUND_AGENT_ENV_MARKER, "1")
        with pytest.raises(BoundAgentDispatchError, match="non-delegable"):
            assert_dispatch_allowed("dispatch")

    def test_operation_name_in_message(self, monkeypatch):
        monkeypatch.setenv(BOUND_AGENT_ENV_MARKER, "1")
        with pytest.raises(BoundAgentDispatchError, match="run_seat"):
            assert_dispatch_allowed("run_seat")
