import pandas as pd
import pytest

from transform import data_transform


@pytest.fixture
def sample_df() -> pd.DataFrame:
    """Sample DataFrame used fo tests."""
    
    return pd.DataFrame({
        "name": ["Alex", "John"],
        "age": [30,25]
    })


def test_transform_returns_dataframe(sample_df: pd.DataFrame) -> None:
    
    result: pd.DataFrame = data_transform(sample_df)
    
    assert isinstance(result, pd.DataFrame)
    

def test_transform_preserves_row_count(sample_df: pd.DataFrame) -> None:
    
    result: pd.DataFrame = data_transform(sample_df)
    
    #assert len(result) == len(sample_df)
    assert result.shape[0] == sample_df.shape[0]


def test_transform_preserves_columns(sample_df: pd.DataFrame) -> None:
    
    result: pd.DataFrame = data_transform(sample_df)
    
    assert list(result.columns) == list(sample_df.columns)


def test_transform_does_not_modify_input(sample_df: pd.DataFrame) -> None:
    
    df_copy: pd.DataFrame = sample_df.copy(deep=True)
    
    _: pd.DataFrame = data_transform(sample_df)
    
    pd.testing.assert_frame_equal(sample_df, df_copy)


def test_transform_handles_empty_dataframe() -> None:
    """Transform should handle empty DataFrame."""

    df = pd.DataFrame()

    result = data_transform(df)

    assert isinstance(result, pd.DataFrame)
    assert result.empty