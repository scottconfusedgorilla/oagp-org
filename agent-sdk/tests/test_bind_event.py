"""Unit tests for bind-event memo emission (bind_event.py)."""

import json
from datetime import datetime
from pathlib import Path

import pytest

from oagp_agent_sdk.bind_event import emit_bind_event_memo


FIXED_NOW = datetime(2026, 5, 29, 14, 30, 0)


@pytest.fixture
def memos_dir(tmp_path: Path) -> Path:
    return tmp_path / "memos"


def _emit(memos_dir, **overrides):
    kwargs = dict(
        from_seat="director",
        to_seat="security-tester",
        agent_name="security-tester",
        position_id="security-tester",
        org_state_sha="abc1234",
        granted_authority=[],
        tier=1,
        brief="Do a static review.",
        now=FIXED_NOW,
        roledef_id="blackhat-tester",
        roledef_version="1.0.0",
        roledef_source="url",
    )
    kwargs.update(overrides)
    return emit_bind_event_memo(memos_dir, **kwargs)


def test_emits_envelope_and_body(memos_dir):
    env_path = _emit(memos_dir)
    assert env_path.exists()
    assert env_path.suffix == ".openthing"
    body_path = env_path.with_suffix("").with_suffix(".body.md")
    # body shares the stem with .body.md suffix
    body_path = memos_dir / (env_path.stem + ".body.md")
    assert body_path.exists()


def test_filename_uses_injected_timestamp(memos_dir):
    env_path = _emit(memos_dir)
    assert env_path.name.startswith("2026-05-29-1430--director--security-tester--bind-event-")


def test_envelope_is_valid_memodef(memos_dir):
    env_path = _emit(memos_dir)
    env = json.loads(env_path.read_text(encoding="utf-8"))
    assert env["type"] == "memodef:Memo"
    assert env["from"] == "director"
    assert env["to"] == "security-tester"
    assert env["action_required"] is False
    assert env["metadata"]["memo_subtype"] == "bind-event"
    assert env["metadata"]["org_state_sha"] == "abc1234"
    assert env["metadata"]["tier"] == 1


def test_propose_only_body_language(memos_dir):
    env_path = _emit(memos_dir, granted_authority=[], tier=1)
    body = (memos_dir / (env_path.stem + ".body.md")).read_text(encoding="utf-8")
    assert "Propose-only" in body
    assert "No commit/push/merge" in body


def test_elevated_body_records_grant(memos_dir):
    env_path = _emit(memos_dir, granted_authority=["commit", "push"], tier=2)
    env = json.loads(env_path.read_text(encoding="utf-8"))
    assert env["metadata"]["granted_authority"] == ["commit", "push"]
    body = (memos_dir / (env_path.stem + ".body.md")).read_text(encoding="utf-8")
    assert "Director-elevated" in body
    assert "commit, push" in body


def test_creates_memos_dir_if_absent(tmp_path):
    target = tmp_path / "does-not-exist-yet"
    env_path = _emit(target)
    assert env_path.exists()
