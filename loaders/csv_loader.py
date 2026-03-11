from .base_loader import BaseLoader 
from etl.logger import get_logger
import pandas as pd


logger = get_logger(__name__)


class CsvLoader(BaseLoader):
    
    def __init__(self, path: str):
        self.path = path
    
    def save_data(self, data:pd.DataFrame) -> None:
        """Saving transformed data into  csv file"""
        
        data.to_csv(self.path, index=False)
        
        logger.info(f"Data saved to {self.path}")