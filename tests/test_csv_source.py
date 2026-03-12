import pandas as pd

from sources.csv_source import CsvSource


def test_csv_source_loads_data(tmp_path) -> None:

    df = pd.DataFrame({
        "price": [1000, 2000],
        "brand": ["BMW", "Audi"]
    })

    input_file = tmp_path / "input.csv"

    df.to_csv(input_file, index=False)

    source = CsvSource(str(input_file))

    result = source.get_data()

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2