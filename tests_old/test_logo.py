import pytest

from logo_old import show_logo


def test_show_logo_outputs_text(capsys) -> None:
    """Logo should be printed to stdout."""

    show_logo()

    captured = capsys.readouterr()

    assert "E  T  L" in captured.out
    assert "Project" in captured.out