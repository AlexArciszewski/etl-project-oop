import pandas as pd
import pytest

from transform.transformers import Transformer



@pytest.fixture
def transformer() -> Transformer:
    """Return Transformer instance."""
    return Transformer()


def test_transformer_removes_duplicates_and_nulls(transformer: Transformer) -> None:
    df = pd.DataFrame({
        "price": [10, 10, None],
        "brand": ["BMW", "BMW", "Audi"]
    })

    result = transformer.transform(df)

    assert len(result) == 1


def test_transformer_removes_unnamed_column(transformer: Transformer) -> None:
    df = pd.DataFrame({
        "Unnamed: 0": [1, 2],
        "price": [1000, 2000]
    })

    result = transformer.transform(df)

    assert "Unnamed: 0" not in result.columns


def test_transformer_removes_nulls(transformer: Transformer) -> None:
    df = pd.DataFrame({
        "price": [1000, None],
        "brand": ["BMW", "Audi"]
    })

    result = transformer.transform(df)

    assert result.isnull().sum().sum() == 0


def test_transformer_keeps_valid_columns(transformer: Transformer) -> None:
    df = pd.DataFrame({
        "price": [1000, 2000],
        "brand": ["BMW", "Audi"]
    })

    result = transformer.transform(df)

    assert {"price", "brand"}.issubset(result.columns)


def test_transformer_handles_missing_column(transformer: Transformer) -> None:
    df = pd.DataFrame({
        "price": [1000, 2000]
    })

    result = transformer.transform(df)

    assert isinstance(result, pd.DataFrame)