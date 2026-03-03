import pandas as pd
import pytest
from pathlib import Path

from extract_old import choose_loader, data_extractor


def test_choose_loader_csv(monkeypatch) -> None:
    """User selects CSV."""

    monkeypatch.setattr("builtins.input", lambda _: "1")

    result: str | None = choose_loader()

    assert result == "read_csv"


def test_choose_loader_excel(monkeypatch) -> None:
    """User selects Excel."""

    monkeypatch.setattr("builtins.input", lambda _: "2")

    result: str | None = choose_loader()

    assert result == "read_excel"


def test_choose_loader_exit(monkeypatch) -> None:
    """User selects exit."""

    monkeypatch.setattr("builtins.input", lambda _: "3")

    result: str | None = choose_loader()

    assert result is None


def test_choose_loader_invalid(monkeypatch) -> None:
    """User selects invalid option."""

    monkeypatch.setattr("builtins.input", lambda _: "999")

    result: str | None = choose_loader()

    assert result is None


def test_data_extractor_csv(monkeypatch, tmp_path: Path) -> None:
    """Valid CSV file loads correctly."""

    test_file: Path = tmp_path / "test.csv"

    df: pd.DataFrame = pd.DataFrame({
        "name": ["Alex"],
        "age": [30],
    })

    df.to_csv(test_file, index=False)

    monkeypatch.setattr("builtins.input", lambda _: str(test_file))

    result: pd.DataFrame | None = data_extractor("read_csv")

    assert isinstance(result, pd.DataFrame)
    assert result.shape == (1, 2)
    assert list(result.columns) == ["name", "age"]


def test_data_extractor_excel(monkeypatch, tmp_path: Path) -> None:
    """Valid Excel file loads correctly."""

    test_file: Path = tmp_path / "test.xlsx"

    df: pd.DataFrame = pd.DataFrame({
        "name": ["John"],
        "age": [25],
    })

    df.to_excel(test_file, index=False)

    monkeypatch.setattr("builtins.input", lambda _: str(test_file))

    result: pd.DataFrame | None = data_extractor("read_excel")

    assert isinstance(result, pd.DataFrame)
    assert result.shape == (1, 2)
    assert list(result.columns) == ["name", "age"]


def test_data_extractor_none_loader() -> None:
    """None loader should return None immediately."""

    result: pd.DataFrame | None = data_extractor(None)

    assert result is None