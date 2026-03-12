import os
import pandas as pd
import pytest

from loaders.csv_loader import CsvLoader


@pytest.fixture
def loader(tmp_path) -> CsvLoader:
    """Return CsvLoader instance with temporary file path."""
    
    output_file = tmp_path / "output.csv"
    
    return CsvLoader(str(output_file))


def test_csv_loader_saves_file(loader: CsvLoader) -> None:
    """Test that CsvLoader creates a CSV file."""

    df = pd.DataFrame({
        "price": [1000, 2000],
        "brand": ["BMW", "Audi"]
    })

    loader.save_data(df)

    assert os.path.exists(loader.path)


def test_csv_loader_saves_correct_data(loader: CsvLoader) -> None:
    """Test that CsvLoader saves correct data to CSV."""

    df = pd.DataFrame({
        "price": [1000, 2000],
        "brand": ["BMW", "Audi"]
    })

    loader.save_data(df)

    loaded_df = pd.read_csv(loader.path)

    assert loaded_df.equals(df)