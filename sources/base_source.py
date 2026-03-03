from abc import ABC, abstractmethod

import pandas as pd


class BaseSource(ABC):
    """Abstract base class for all data sources."""
    
    
    @abstractmethod
    def get_data(self) -> pd.DataFrame:
        """Gets data and return it as a DataFrame"""
        pass
    