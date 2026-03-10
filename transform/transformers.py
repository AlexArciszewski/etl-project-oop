from .base_transformer import BaseTransformer
import pandas as pd


class Transformer(BaseTransformer): 
    
    def transform(self, df: pd.DataFrame)-> pd.DataFrame:
        """Transform input DataFrame and return cleaned DataFrame."""
        
        df = df.copy()
        
        df = df.drop(columns=["Unnamed: 0"], errors="ignore")
        df = df.drop_duplicates()
        df = df.dropna()
        
        print(f"Data transformed successfully")
        
        print(df.head(2))
        
        return df
