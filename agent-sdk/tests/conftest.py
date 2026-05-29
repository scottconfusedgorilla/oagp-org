"""Shared pytest fixtures for the agent-sdk test suite."""

from pathlib import Path

import pytest

FIXTURE_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixture_project(tmp_path: Path) -> Path:
    """Lay out a temporary OAGP-shaped project rooted at tmp_path.

        tmp_path/
          org/minimal-orgdef.opencatalog   (copied from tests/fixtures/)
          memos/                            (empty)

    Returns the project root.
    """
    org_dir = tmp_path / "org"
    org_dir.mkdir()
    (tmp_path / "memos").mkdir()
    src = FIXTURE_DIR / "minimal-orgdef.opencatalog"
    (org_dir / "minimal-orgdef.opencatalog").write_text(
        src.read_text(encoding="utf-8"), encoding="utf-8"
    )
    return tmp_path


@pytest.fixture
def orgdef_path(fixture_project: Path) -> Path:
    return fixture_project / "org" / "minimal-orgdef.opencatalog"
