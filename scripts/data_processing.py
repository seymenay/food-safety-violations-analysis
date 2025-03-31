import pandas as pd

def load_data(filepath):
    """Excel file to Pandas DataFrame"""
    try: 
        data = pd.read_excel(filepath)
        print("DataFrame is successfully loaded.")

        return data
    except Exception as E:
        print(f"Error loading data: {E}")
        return None

def clean_data(df):
    #Since the RASFF data is well-structured there is no need to clean data process, just check the important columns and dates.
    if df is not None:
        return df
    else:
        print("No data for cleaning")
        return None
