import pandas as pd
import pytest
from pathlib import Path

from load_old import save_data


@pytest.fixture
def sample_df() -> pd.DataFrame:
    """Sample DataFrame used for save tests."""
    
    return pd.DataFrame({
        "name": ["Alex", "John"],
        "age": [30, 25],
    })


def test_save_data_csv(sample_df: pd.DataFrame, tmp_path: Path) -> None:

    path: Path = tmp_path / "test_output.csv"

    result: bool = save_data(sample_df, path)

    assert result is True
    assert path.exists()


def test_save_xlsx(sample_df: pd.DataFrame, tmp_path: Path) -> None:

    path: Path = tmp_path / "test_output.xlsx"

    result: bool = save_data(sample_df, path)

    assert result is True
    assert path.exists()


def test_save_json(sample_df: pd.DataFrame, tmp_path: Path) -> None:

    path: Path = tmp_path / "test_output.json"

    result: bool = save_data(sample_df, path)

    assert result is True
    assert path.exists()


def test_save_data_invalid_extension(sample_df: pd.DataFrame, tmp_path: Path) -> None:

    path: Path = tmp_path / "test_output.txt"

    result: bool = save_data(sample_df, path)

    assert result is False
    assert not path.exists()


def test_save_empty_dataframe(sample_df, tmp_path: Path) -> None:
    """Saving empty DataFrame should work."""

    empty_df = sample_df.iloc[0:0]

    path: Path = tmp_path / "empty.csv"

    result = save_data(empty_df, path)

    assert result is True
    assert path.exists()


def test_save_no_extension(sample_df: pd.DataFrame, tmp_path: Path) -> None:
    """Should return False if no extension."""

    path: Path = tmp_path / "output"

    result: bool = save_data(sample_df, path)

    assert result is False
    assert not path.exists()


def test_save_nested_directory(sample_df: pd.DataFrame, tmp_path: Path) -> None:
    """Should handle nested directory."""

    path: Path = tmp_path / "nested" / "output.csv"

    path.parent.mkdir()

    result: bool = save_data(sample_df, path)

    assert result is True
    assert path.exists()


def test_save_invalid_directory(sample_df: pd.DataFrame, tmp_path: Path) -> None:
    """Should fail if directory does not exist."""

    path: Path = tmp_path / "nonexistent" / "output.csv"

    result: bool = save_data(sample_df, path)

    assert result is False
    
    
def test_save_none_dataframe(tmp_path: Path) -> None:
    """Should return False if df is None."""

    path: Path = tmp_path / "output.csv"

    result: bool = save_data(None, path) 

    assert result is False
    

def test_save_json_content(sample_df: pd.DataFrame, tmp_path: Path) -> None:
    """JSON content should match DataFrame."""

    path: Path = tmp_path / "output.json"

    save_data(sample_df, path)

    loaded: pd.DataFrame = pd.read_json(path)

    assert loaded.shape == sample_df.shape
    assert list(loaded.columns) == list(sample_df.columns)


def test_save_invalid_path(sample_df: pd.DataFrame, tmp_path: Path) -> None:
    """Should handle invalid path."""

    invalid_path: Path = tmp_path / "nonexistent_dir" / "file.csv"

    result: bool = save_data(sample_df, invalid_path)

    assert result is False