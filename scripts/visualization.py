import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from analysis import data_analysis_pd, data_analysis_sql

mpl.style.use(['ggplot'])

# To visualize a bar plot, update the 'selected_key' with any valid key from the dictionary.
def bar_plot(df, selected_key="Category", stacked=True):
    results = data_analysis_pd(df)
    if selected_key in results and isinstance(results[selected_key], dict):
        data = results[selected_key]
        if not data:
            print(f"No data available for {selected_key}.")
            return
        
        plt.figure(figsize=(10,5))
        plt.bar(data.keys(), data.values(), color="lightcoral")
        plt.xlabel(selected_key)
        plt.ylabel("Counts")
        plt.title(f"Distribution of {selected_key}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        print("Plotting the bar chart...")
        plt.show()
        print("Bar chart displayed successfully.")
        
    else:
        print("Invalid key or data format.")

def line_plot(df):
    # Data retrieved from SQL query is saved in data_analysis.txt.
    years = ['2020', '2021', '2022', '2023', '2024', '2025']
    values = [959, 1367, 1148, 1773, 1921, None]

    plt.figure(figsize=(8,5))
    plt.plot(years, values, marker='o', linestyle='-', color='blue', label='Violations counts by years')
    plt.xlabel('Years')
    plt.ylabel('Violation Counts')
    plt.title('Annual Violation Counts')
    plt.legend()
    plt.grid(True)
    print("Plotting the line chart...")
    plt.show()
    print("Line chart displayed successfully.")

def pivot_table(df, selected_key="Origin&Hazards"):
    results = data_analysis_pd(df)
    if selected_key in results and isinstance(results[selected_key], dict):
        data = results[selected_key]
        if not data:
            print(f"No data available for {selected_key}.")
            return
        
    # I added it because there is no 'count' column.
    if 'count' not in df.columns:
        df['count'] = 1

    # To visualize data, I first convert the dict to a DataFrame in order to use it with a pivot table.
    df = pd.DataFrame.from_dict(data, orient='index', columns=['count']).reset_index()
    df[['origin', 'hazards']] = pd.DataFrame(df['index'].to_list(), index=df.index)
    df.drop(columns=['index'], inplace=True)
    pivot_table = df.pivot_table(values='count', index='origin', columns='hazards', aggfunc='sum', fill_value=0)
    #choose color
    colors = ['green', 'red', 'purple', 'skyblue']

    pivot_table.plot(kind='bar', stacked=True, figsize=(10,6), color=colors)
    
    plt.title('Origin vs Hazards')
    plt.xlabel('Origin')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    print("Plotting the pivot chart...")
    plt.show()
    print("Pivot chart displayed successfully.")
