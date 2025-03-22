import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import sqlite3
from data_processing import load_data, clean_data
from analysis import data_analysis_sql, data_analysis_pd, to_datetime

__all__ = ["pd", "np", "plt", "sns"]

def main():
    """"""
    file_path = "/Users/seymenay/food-safety-violations-analysis/data/RASFF_window_results_2.xlsx"
    df = load_data(file_path)
    cleaned_data = clean_data(df)

    df = to_datetime(df)
    analysed_data = data_analysis_pd(df)
    #sql_query = data_analysis_sql(df)

if __name__ == "__main__":
    main()
