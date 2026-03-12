import pandas as pd

from transform.transformers import Transformer

def test_transformer_removes_duplicates_and_nulls():

    df = pd.DataFrame({
        "price": [10, 10, None],
        "brand": ["BMW", "BMW", "Audi"]
    })

    transformer = Transformer()

    result = transformer.transform(df)

    assert len(result) == 1