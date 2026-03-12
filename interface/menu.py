from sources.csv_source import CsvSource
from transform.transformers import Transformer
import pandas as pd
from etl.pipeline import Pipeline
from loaders.csv_loader import CsvLoader


class Menu:
    """Menu class"""
    
    
    def __init__(self) -> None:
        pass
    
    
    def run(self) -> None:
        """Application controller"""
        
        while True:
            print() 
            self.display()
            choice: str = input("Please choose 1 or 2: ")
            
            if choice == "1":
                try:
                    self._run_etl()
                except Exception as e:
                    print(f"Error:{e}")
            elif choice == "2":
                print("Program will now exit.")
                break
            else:
                print("invalid option")     
        
    
    def display(self) -> None:
        """Method used to show the program Menu"""
        
        print("1 - Run ETL process")
        print("2 - Exit")
    
    
    def _run_etl(self) -> None:
        """Builds components and runs the ETL pipeline."""
        
        source = CsvSource("/media/alexander/Dane2/2_Python_Data/998_Databases/2_db_cars_csv/USA_cars_datasets.csv")
        
        transformer = Transformer()
        
        
        loader = CsvLoader("/media/alexander/Dane2/2_Coding/2_python_coding/001_etl_project_OOP/saved_data/output.csv")
        # loader.save_data(transformed_df)
        
        pipeline = Pipeline(source, transformer, loader)
        
        result = pipeline.run()
        
        print(result.head())


    
    