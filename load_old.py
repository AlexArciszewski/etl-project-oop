import pandas as pd
from pathlib import Path


def choose_saver() -> str | None:
    "Returns the name of the data to save"
    
    data_type:str | None = None
    
    print("How would like to save your data?")
    
    print("Press 1 for .csv file")
    print("Press 2 for .xls/.xlsx file")
    print("press 3 for a json file")
    print("Press 4 for exit to main menu")
    
    savedata_choice:str = input("Your choice: ")
    
    if savedata_choice == "1":
        data_type = "csv"
        
    elif savedata_choice == "2":
        data_type = "xlsx"
        
    elif savedata_choice == "3":
        data_type = "json"
                
    elif savedata_choice =="4":
        return None
    
    else:
        print("Invalid choice, try again and choose 1, 2, 3 or 4.")
        return None
    
    print(f"Chosen file type is{data_type}")
    
    return data_type


def choose_path() -> Path| None:
    """Returns the name of the data to save"""
    
    path:Path = input("Input the path included name of the file: ")
    
    print(f"Chosen path is: {path}")
    
    file_type:str|None = choose_saver()
     
    if file_type is None:
        print("Saving canceled")
        return None
    
    full_path = Path(path).with_suffix("." + file_type)
     
    print(f"Full path is {full_path}")
    
    return full_path


def save_data(df: pd.DataFrame, path: Path) -> bool:
    """Save DataFrame to file based on extension"""
    
    try:
        
        suffix = path.suffix.lower()
        
        print(suffix)
        
        if suffix == '.csv':
            
            df.to_csv(path, index=False)
            
        elif suffix in [ ".xlsx", ".xls"]:
            
            df.to_excel(path, index=False)
            
        elif suffix == '.json':
            
            df.to_json(path, orient="records", indent=4)
        
        else:
            
            print("Unsupported file type")
            
            return False
        
        print(f"Data saved to {path}")
        
        return True
    
    except Exception as e:
        
        print(f"Error saving file: {e}")
        
        return False
        
    
