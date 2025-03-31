import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import sqlite3
from datetime import datetime
import re

# Change date's type
def to_datetime(df):

    try:
        df['formatted_date'] = pd.to_datetime(df['date'], format='%d-%m-%Y %H:%M:%S', errors='coerce')
        df['formatted_date'] = df['formatted_date'].dt.strftime('%Y-%m-%d')
        return df
    except Exception as e:
        print(f"Error in converting date: {e}")
        return df

# Data analysis with SQL
def data_analysis_sql(df):
    
    try:
        to_datetime(df)

        # Running SQL query on the connected database to fetch data.
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

# Data analysis with pandas
def data_analysis_pd(df):

    try:
        if df is not None:

            timestamp = datetime.now()
            to_datetime(df)
        
            file_path = "data_analysis.txt"
            
            df_turkey = df[df["origin"] == "Türkiye"]
            df_poland = df[df["origin"] == "Poland"]

            df["category"] = df["category"].str.strip().str.lower()
            # Mapping data to ensure consistency in visualization.
            category_mapping = {"poultry meat and poultry meat products": "poultry meat prod.",
                                "dietetic foods, food supplements and fortified foods": "food supplements",
                                "meat and meat products (other than poultry)": "other than poultry",
                                "cereals and bakery products": "cereals and bakery",
                                "nuts, nut products and seeds": "nut and seeds",
                                "fish and fish products": "fish prod.",
                                "milk and milk products": "milk prod.",
                                "other food product / mixed": "other food prod."
                                }
            df["category"] = df["category"].replace(category_mapping)

            # Standardizing the "hazards" column for consistency.
            df["hazards"] = df["hazards"].str.replace(r"(?i)salmonella[\s\S]*", "Salmonella", regex=True)

            df["hazards"] = df["hazards"].str.strip().str.lower()
            # Mapping data to ensure consistency in visualization.
            hazards_mapping = {"listeria monocytogenes": "Listeria",
                               "aflatoxin b1  ,aflatoxin total": "Aflatoxin",
                               "escherichia coli shigatoxin-producing": "E. coli ST",
                               "pyrrolizidine alkaloids": "P. alkaloids",
                               "ragweed (ambrosia spp.) seeds  too high content": "Ambrosia spp."
                               }
            df["hazards"] = df["hazards"].replace(hazards_mapping)

            # Beginning the data analysis process.
            # I changed the to_string() function to to_dict() later because
            # it was more appropriate for writing data correctly, not for visualizing data.
            analysis_results = {
                "Shape": str(df.shape),
                "NaN_Check": df[['risk_decision', 'origin', 'distribution', 'date', 'notifying_country', 'category', 'classification']].isna().sum().to_dict(),
                "Describe": df.describe().to_dict(),
                "Origin": df["origin"].value_counts().head(10).to_dict(),
                "Notifying": df["notifying_country"].value_counts().head(10).to_dict(),
                "Percentage_Counts_Origin": (df["origin"].value_counts(normalize=True)*100).head(10).to_dict(),
                "Percentage_Counts_Notifying_Country": (df["notifying_country"].value_counts(normalize=True)*100).head(10).to_dict(),
                "Category": df["category"].value_counts().head(10).to_dict(),
                "Percentage_Counts_Category": (df["category"].value_counts(normalize=True)*100).head(10).to_dict(),
                "Category&Classification": df.value_counts(subset=["category","classification"]).head(10).to_dict(),
                "Subject&Risk&Hazards": df.value_counts(subset=["subject", "risk_decision", "hazards"]).head(10).to_dict(),
                "Hazards": df["hazards"].value_counts().head(10).to_dict(),
                "Origin&Hazards": df.value_counts(subset=["origin", "hazards"]).head(10).to_dict(),
                "Poland's_Category": df_poland["category"].value_counts().head(10).to_dict(),
                "Turkey's_Category": df_turkey["category"].value_counts().head(10).to_dict(),
                "Most_Violations_Reported_on": df["formatted_date"].value_counts().idxmax()
            }

            # Writing the extracted data to a .txt file in a structured format.
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

            return analysis_results

    except Exception as e:
        print("Error: ", e)