import pandas as pd
import os

directory_path = r"C:\Users\USER\OneDrive\Desktop\Kenyan_Bank_Analysis\data\raw"
file_names = ["2024_Finaccess_Publicdata.xlsx", "357447032 Depository Corporation Survey - CSV.csv", "Monthly Economic Indicators.xlsx"]
dataframes = {}

for file_name in file_names:
    file_path = os.path.join(directory_path, file_name)
    try:
        if file_name.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        elif file_name.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            print(f"Error: Unsupported file type for {file_name}")
            continue # Skip to the next file
        
        dataframes[file_name] = df
        print(f"Loaded {file_name}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")