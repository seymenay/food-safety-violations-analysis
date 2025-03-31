import pandas as pd
import matplotlib as plt
import seaborn as sns
import sqlite3
from data_processing import load_data, clean_data
from analysis import data_analysis_sql, data_analysis_pd, to_datetime
from visualization import bar_plot, line_plot, pivot_table

def main():
    """
    1. Loads the dataset from the specified file.
    2. Cleans the data by handling missing values and inconsistencies.
    3. Converts necessary columns to datetime format.
    4. Performs exploratory data analysis.
    5. Generates visualizations based on the processed data.
    """
    file_path = "/Users/seymenay/food-safety-violations-analysis/data/RASFF_window_results_2.xlsx"
    df = load_data(file_path)
    cleaned_data = clean_data(df)
    df = to_datetime(df)
    """
    - Uncomment `data_analysis_pd(df)` to perform data analysis using Pandas.
    - Uncomment `data_analysis_sql(df)` to perform SQL-based analysis.
    - Uncomment `bar_plot(df)`, `pivot_table(df)`, or `line_plot(df)` for different visualizations.
    """
    #analysed_data = data_analysis_pd(df) #(!)# If you want to write them in a .text file you should convert to_dict() to to_string()!
    #sql_query = data_analysis_sql(df) 
    #bar_plot(df)
    #pivot_table(df)
    #line_plot(df)

if __name__ == "__main__":
    main()
