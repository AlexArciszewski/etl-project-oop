import pytest
from typing import Iterator

from main import main


def test_main_exit(monkeypatch, capsys) -> None:
    """Program should exit when user selects option 6."""

    inputs: Iterator[str] = iter(["6"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()

    assert "Program will now exit" in captured.out


def test_main_show_menu_then_exit(monkeypatch, capsys) -> None:
    """Program should show menu and then exit."""

    inputs: Iterator[str] = iter(["1", "6"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()

    assert "Choose options" in captured.out


def test_main_check_status_then_exit(monkeypatch, capsys) -> None:
    """Program should show status menu and exit."""

    inputs: Iterator[str] = iter(["5", "6"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()

    assert "Check Data status" in captured.out
    
    
def test_main_invalid_option_then_exit(monkeypatch, capsys) -> None:
    """Program should handle invalid input and exit."""

    inputs: Iterator[str] = iter(["999", "6"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()

    assert "Choose options" in captured.out