import pandas as pd


def data_transform(df: pd.DataFrame) -> pd.DataFrame:
    """Transform raw DataFrame into cleaned DataFrame.

    Args:
        df (pd.DataFrame): raw data from extract.py

    Returns:
        pd.DataFrame: cleaned data
    """
    
    print(f"\nDataFrame shape: {df.shape}")
    
    print("\nFirst 2 rows:")
    print(df.head(2))
    
    df = df.copy()
    
    df = df.dropna()
    
    df = df.drop_duplicates()
    
    print(f"Transformed DataFrame shape: {df.shape}") 
       
    return df


