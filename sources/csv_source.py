from .base_source import BaseSource

import pandas as pd



class CsvSource(BaseSource):
    
    def __init__(self, path:str) -> None:
        
        self.path = path
    
    def get_data(self) -> pd.DataFrame:
        df = pd.read_csv(self.path)
        print(df.head(2))
        return df


# csv_obj = CsvSource(
#     "/media/alexander/Dane2/2_Python_Data/998_Databases/2_db_cars_csv/USA_cars_datasets.csv"
#     )