from .base_source import BaseSource
from etl.logger import get_logger

import pandas as pd

logger = get_logger(__name__)

class CsvSource(BaseSource):
    """CSV data source."""
    
    def __init__(self, path: str) -> None:
        
        self.path = path
    
    def get_data(self) -> pd.DataFrame:
        """Load CSV file into DataFrame."""
        
        logger.info(f"Loading CSV file: {self.path}")
        
        df = pd.read_csv(self.path)
        
        logger.info(f"Loaded {len(df)} rows from {self.path}")
        
        return df
