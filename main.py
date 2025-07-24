import os
from scripts.load_data import load_excel, load_csv
from scripts.clean_data import clean_column_names, convert_dates
from scripts.save_data import save_to_csv

# Define paths
raw_dir = os.path.join("data", "raw")
processed_dir = os.path.join("data", "processed")

# -------- Bank Stability --------
bank_file = "357447032_Depository Corporation Survey.csv"
df_bank = load_csv(os.path.join(raw_dir, bank_file))
df_bank = clean_column_names(df_bank)
df_bank = df_bank.dropna() #Removes rows with any missing values
#OR
#fillna(value=0)-filling missing values with zero
df_bank = df_bank.fillna(value= 0)
df_bank = convert_dates(df_bank, "date")  # change column if needed
save_to_csv(df_bank, os.path.join(processed_dir, "clean_bank_data.csv"))

# -------- Customer Risk Mapping --------
finaccess_file = "2024_Finaccess_Publicdata.xlsx"
df_fin = load_excel(os.path.join(raw_dir, finaccess_file))
df_fin = df_fin = clean_column_names(df_fin)
df_fin = df_fin.dropna() 
df_fin = df_fin.fillna ( method= "ffill" )# Removes rows with any missing values
    # OR
    # Example: Forward fill missing values
save_to_csv(df_fin, os.path.join(processed_dir, "clean_finaccess_data.csv"))

# -------- Economic Indicators --------
econ_file = "Monthly Economic Indicators.xlsx"
df_econ = load_excel(os.path.join(raw_dir, econ_file))
df_econ = clean_column_names(df_econ)
df_econ = convert_dates(df_econ, "date")
df_econ = df_econ.fillna(df_econ.mean())# filling issing values with column mean
#OR
df_econ = df_econ.dropna (subset=["specific_column"])#Drops rows with missing values in a specific column
save_to_csv(df_econ, os.path.join(processed_dir, "clean_economic_indicators.csv"))

import pandas as pd
df1 = pd.read_csv ("file1.csv")
df2 = pd.read_csv ("file2.csv")
df3 = pd.read_csv ("file3.csv")
combined_df = pd.concat ([df1, df2, df3])
combined_df.to_csv("C:/Users/USER/OneDrive/Desktop/Kenyan_Bank_Analysis/data/processed/combined_data.csv", index=False)