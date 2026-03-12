import pandas as pd

from etl.pipeline import Pipeline
from sources.csv_source import CsvSource
from transform.transformers import Transformer
from loaders.csv_loader import CsvLoader


def test_pipeline_runs(tmp_path) -> None:

    data = pd.DataFrame({
        "price": [1000, None],
        "brand": ["BMW", "Audi"]
    })

    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    data.to_csv(input_file, index=False)

    source = CsvSource(str(input_file))
    transformer = Transformer()
    loader = CsvLoader(str(output_file))

    pipeline = Pipeline(source, transformer, loader)

    result = pipeline.run()

    assert isinstance(result, pd.DataFrame)
    assert output_file.exists()
    
    
def test_pipeline_removes_nulls(tmp_path) -> None:

    data = pd.DataFrame({
        "price": [1000, None],
        "brand": ["BMW", "Audi"]
    })

    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    data.to_csv(input_file, index=False)

    source = CsvSource(str(input_file))
    transformer = Transformer()
    loader = CsvLoader(str(output_file))

    pipeline = Pipeline(source, transformer, loader)

    result = pipeline.run()

    assert result.isnull().sum().sum() == 0