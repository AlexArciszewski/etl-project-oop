from abc import ABC, abstractmethod
import pandas as pd


class BaseTransformer(ABC):
    """Abstract base class for all data transformations."""
    
    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Transform input DataFrame and return transformed DataFrame.

        Args:
            df (pd.DataFrame): Raw data from source

        Returns:
            pd.DataFrame: Transformed data 
        """
        pass
    