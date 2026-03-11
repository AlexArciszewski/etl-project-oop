from abc import ABC, abstractmethod

import pandas as pd


class BaseLoader(ABC):
    """Abstract base class for all data loaders."""
    
    
    @abstractmethod
    def save_data(self, data: pd.DataFrame) -> None:
        """Gets transformed data and saves it"""
        pass