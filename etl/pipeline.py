from sources.base_source import BaseSource
from transform.base_transformer import BaseTransformer
from etl.loaders import BaseLoader

import pandas as pd


class Pipeline:
    """Class that represents the ETL pipeline."""
    
    
    def __init__(self, 
        source: BaseSource,
        transformer: BaseTransformer,
        loader: BaseLoader
        ) -> None:
        
        self.source = source
        self.transformer = transformer
        self.loader = loader
    
    def run(self) -> pd.DataFrame:
        """Execute the ETL pipeline."""
        
        raw_data = self.source.get_data()
        transformed_data = self.transformer.transform(raw_data)
        
        self.loader.save(transformed_data)
        
        return transformed_data
        