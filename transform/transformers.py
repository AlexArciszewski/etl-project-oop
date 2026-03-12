import pandas as pd

from .base_transformer import BaseTransformer
from etl.logger import get_logger


logger = get_logger(__name__)


class Transformer(BaseTransformer):

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transform input DataFrame and return cleaned DataFrame."""

        df = df.copy()

        rows_before = len(df)
        
        df = df.drop(columns=["Unnamed: 0"], errors="ignore")
        df = df.drop_duplicates()
        df = df.dropna()
        
        rows_after = len(df)
        
        logger.info(f"Rows before: {rows_before}, rows after: {rows_after}")
        logger.info("Data transformed successfully")

        return df