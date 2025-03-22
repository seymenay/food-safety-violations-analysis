import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import sqlite3
from datetime import datetime

#change date type
def to_datetime(df):

    df['formatted_date'] = pd.to_datetime(df['date'], format='%d-%m-%Y %H:%M:%S', errors='coerce')
    df['formatted_date'] = df['formatted_date'].dt.strftime('%Y-%m-%d')
    return df

#data analysis with SQL
def data_analysis_sql(df):
    
    try:
        to_datetime(df)
        connection = sqlite3.connect('project.db')
        df.to_sql('project', connection, if_exists='replace', index=False)
        cursor = connection.cursor()
        cursor.execute("""SELECT strftime('%Y', `formatted_date`) AS year, COUNT(formatted_date) AS year_count 
                       FROM project 
                       GROUP BY strftime('%Y', `formatted_date`)
                       """)
        results = cursor.fetchall()
        """for row in results:
            print(row)"""
        return results
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

#data analysis with pandas
def data_analysis_pd(df):

    try:
        if df is not None:
            timestamp = datetime.now()
            to_datetime(df)
            file_path = "data_analysis.txt"
            
            df_turkey = df[df["origin"] == "Türkiye"]
            df_poland = df[df["origin"] == "Poland"]

            analysis_results = {
                "Shape": str(df.shape),
                "NaN Check": df[['risk_decision', 'origin', 'distribution', 'date', 'notifying_country', 'category', 'classification']].isna().sum().to_string(),
                "Describe": df.describe().to_string(),
                "Origin": df["origin"].value_counts().head(10).to_string(),
                "Notifying": df["notifying_country"].value_counts().head(10).to_string(),
                "Percentage Counts Origin": (df["origin"].value_counts(normalize=True)*100).head(10).to_string(),
                "Percentage Counts Notifying Country": (df["notifying_country"].value_counts(normalize=True)*100).head(10).to_string(),
                "Category": df["category"].value_counts().head(10).to_string(),
                "Percentage Counts Category": (df["category"].value_counts(normalize=True)*100).head(10).to_string(),
                "Category & Classification": df.value_counts(subset=["category","classification"]).head(10).to_string(),
                "Subject & Risk & Hazards": df.value_counts(subset=["subject", "risk_decision", "hazards"]).head(10).to_string(),
                "Hazards": df["hazards"].value_counts().head(10).to_string(),
                "Origin & Hazards": df.value_counts(subset=["origin", "hazards"]).head(5).to_string(),
                "Poland's Category": df_poland["category"].value_counts().head(10).to_string(),
                "Turkey's Category": df_turkey["category"].value_counts().head(10).to_string(),
                "Most Violations Reported on": str(df["formatted_date"].value_counts().idxmax()),
            }

            try:
                with open(file_path, "a+", encoding='utf-8') as file:
                    file.write(f"Analysis started at {timestamp}\n")
                    for key, value  in analysis_results.items():
                        file.write(f"**- {key} -**\n")
                        file.write(value + "\n\n")
                    file.write("*"*80 + "\n")
                    print("Analysis is successful")
            except Exception as E:
                print(f"Error: {E}")

    except Exception as e:
        print("Error: ", e)