import pandas as pd


def choose_loader() -> str | None:
    """
    Prompts user to choose the appropriate data loader for their file type.
    
    Returns:
        str | None: Name of pandas read function ('read_csv' or 'read_excel'),
                    or None if user chooses to exit or enters invalid input.
    """
    
    print("Choose a type of a file you want load the data from: ")
    print("Press 1 for .csv file.")
    print("Press 2 for .xls/.xlsx file.")
    print("Press 3 for exit to main menu.")
    
    user_choice:str = input("Your choice: ")
    
    if user_choice == '1':
        loader = "read_csv"
        
    elif user_choice == '2':
        loader = "read_excel"
        
    elif user_choice == '3':
        return None
    
    else:
        print("Invalid choice, try again and choose 1, 2 or 3.")
        
        return None
    
    return loader 


def data_extractor(loader:str | None) -> pd.DataFrame | None:
    """
    Extract data from a file using the specified pandas loader function.
    
    Continuously prompts user for file path until valid file is loaded
    or user exits. Handles common file loading errors gracefully.
    
    Args:
        loader: Name of pandas read function to use ('read_csv' or 'read_excel'),
                or None to exit.
    
    Returns:
        pd.DataFrame | None: Loaded DataFrame if successful, None if user exits
                             or loader is None.
    
    """
    
    if loader is None:
        print("Exiting to main menu")
        return None
    
    file_extension: str = loader.replace("read_", "")
    
    print(f"Chosen data type is {file_extension}")
    
    df: pd.DataFrame |None = None
    
    while True:
        
        file_path:str = input("Enter the path of a file to open: ")
            
        print(f"Chosen function to open the file is {loader}")
        print(f"Chosen path is {file_path}")
            
        if not file_path:
            print("No file path given, try again")
            continue
            
        try:
            
            df = getattr(pd, loader)(file_path)
            
            print(
                f"File loaded with {len(df)} rows"
                f"and {len(df.columns)} columns."
            )
            print(f"The head is: \n {df.head(2)}")
            
            return df    
                
        except FileNotFoundError:
            
            print(f"File not found: {file_path}.")
            
            
            
        except pd.errors.EmptyDataError:
            
            print(f"File {file_path} is empty.")
            
        
            
        except Exception as e:
            
            print(f"Error loading file from {file_path}:{e}")
        
    
