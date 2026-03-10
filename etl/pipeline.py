from sources.base_source import BaseSource
from transform.base_transformer import BaseTransformer
#from etl.loaders import BaseLoader
from etl.logger import get_logger
import pandas as pd


logger = get_logger(__name__)

# def run_pipeline():

#     logger.info("Pipeline started")

#     try:
#         logger.info("Loading data")

#         # tu np. pandas
#         # df = pd.read_csv(...)

#         logger.info("Data loaded successfully")

#     except Exception as e:
#         logger.error(f"Pipeline error: {e}")

class Pipeline:
    """Class that represents the ETL pipeline."""
    
    
    def __init__(self, 
        source: BaseSource,
        transformer: BaseTransformer,
        # loader: BaseLoader
        ) -> None:
        
        self.source = source
        self.transformer = transformer
        #self.loader = loader
    
    def run(self) -> pd.DataFrame:
        """Execute the ETL pipeline."""
        
        raw_data = self.source.get_data()
        transformed_data = self.transformer.transform(raw_data)
        
        # self.loader.save(transformed_data)
        
        return transformed_data
        