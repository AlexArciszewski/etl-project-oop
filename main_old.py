from typing import Callable, Dict, Optional
import pandas as pd
from colorama import init

from extract import data_extractor, choose_loader
from transform import data_transform
from load import choose_path, save_data
from logo import show_logo


init(autoreset=True)


def main() -> None:
    """Entry point for ETL CLI application"""
    
    show_logo()
    
    raw_df: Optional[pd.DataFrame] = None
    transformed_df: Optional[pd.DataFrame] = None
    saved_path: str | None = None
    
    etl_status: Dict[str, bool] = {
        "extract": False,
        "transform": False,
        "load": False
    }    
        
    def menu_loader() -> None:
        """Show program menu"""
        show_logo()  
        print("This is menu: ")
    
    def load_raw_data() -> pd.DataFrame | None:
        """Extracting raw data from the file"""
        nonlocal raw_df
        
        loader = choose_loader()
        data = data_extractor(loader)

        if data is not None:
            raw_df = data
            etl_status["extract"] = True
            print("Data extraction completed")
        else:
            print("Error during extraction of a data")
        return data
    
    def transform_data() -> None:
        """Tranforming loaded data"""
        nonlocal raw_df, transformed_df
        
        if raw_df is None:
            print("No data loaded Please extract the data first.")
            return 
        
        transformed_df = data_transform(raw_df)
        
        print("Data transformed completed")
        etl_status["transform"] = True
    
    def data_saver() -> None:
        """Save tranformed data to a file"""
        nonlocal transformed_df, saved_path
        
        if transformed_df is None:
            print("There is no data to save...")
            return
        
        full_path = choose_path()
    
        save_data(transformed_df, full_path)
        
        saved_path = full_path
        
        etl_status["load"] = True
        
        print(f"Data saved to: {saved_path}")
            
    def program_exit() -> None:
        """Exit the program"""
        print("Program will now exit. Have a nice day!")
        raise SystemExit()
    
    def check_status() -> None:
        """Show ETL operation status"""
        print("\n---ETL STATUS check--- ")
        
        print(
            f"Extraction: "
            f"{'Done' if etl_status['extract'] else 'Waiting' }"
        )
        
        print(
            f"Transforming: "
            f"{'Done' if etl_status['transform'] else 'Waiting' }"
        )
        
        print(
            f"Loading: "
            f"{'Done' if etl_status['load'] else 'Waiting' }"
        )
        
        print("\n")
        
    options: Dict[int, Callable[[], None]] = {
        1: menu_loader,
        2: load_raw_data,
        3: transform_data,
        4: data_saver,
        5: check_status,
        6: program_exit,
    }
    
    while True:
        
        print("\nChoose options:")
        print("1 - Menu")
        print("2 - Extract Data")
        print("3 - Transform Data")
        print("4 - Load Data ")
        print("5 - Check Data status")
        print("6 - Exit")

        try:
            user_choice: int = int(input("Chose your option: "))
        except ValueError:
            print("Pls give men the proper number:")
            continue
        
        if user_choice in options:
            options[user_choice]()
        else:
            print("Incorrect number")
    
        
if __name__ == "__main__":
    main()

