from .base_transformer import BaseTransformer
from etl.logger import get_logger

import pandas as pd

logger = get_logger(__name__)

class Transformer(BaseTransformer): 
    
    def transform(self, df: pd.DataFrame)-> pd.DataFrame:
        """Transform input DataFrame and return cleaned DataFrame."""
        
        df = df.copy()
        
        df = df.drop(columns=["Unnamed: 0"], errors="ignore")
        df = df.drop_duplicates()
        df = df.dropna()
        
        
        logger.info(f"Data transformed successfully")
        # print(f"Data transformed successfully")
        
        
        return df
