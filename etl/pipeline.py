import pandas as pd

from sources.base_source import BaseSource
from transform.base_transformer import BaseTransformer
from loaders.base_loader import BaseLoader
from etl.logger import get_logger




logger = get_logger(__name__)


class Pipeline:
    """Class that represents the ETL pipeline."""
    
    def __init__(
        self, 
        source: BaseSource,
        transformer: BaseTransformer,
        loader: BaseLoader
        ) -> None:
        
        self.source = source
        self.transformer = transformer
        self.loader = loader
    
    def run(self) -> pd.DataFrame:
        """Execute the ETL pipeline."""
        
        logger.info("Pipeline started")
        
        raw_data = self.source.get_data()
        
        print("\nRAW DATA")
        print(raw_data.head())
        
        logger.info("Data loaded")
        
        transformed_data = self.transformer.transform(raw_data)
        
        print("\nTRANSFORMED DATA")
        print(transformed_data.head())
        
        logger.info("Data transformed")
        
        self.loader.save_data(transformed_data)
        
        logger.info("Data saved")
        logger.info("Pipeline process completed")
        
        return transformed_data
        