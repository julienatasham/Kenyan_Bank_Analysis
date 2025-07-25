import pandas as pd
import os

# Define function to load all datasets
def load_all_data(raw_data_folder="data/raw"):
    """
    Loads all cleaned CSV datasets from the specified raw data folder.

    Parameters:
        raw_data_folder (str): Path to the folder where CSV files are stored.

    Returns:
        dict: A dictionary containing all loaded DataFrames.
    """
    # Build full paths to each file
    file_bank1 = os.path.join(raw_data_folder, "Bank_Stability_Analysis.csv")
    file_bank2 = os.path.join(raw_data_folder, "Bank_Stability_Analysis2.csv")
    file_customer_risk = os.path.join(raw_data_folder, "Customer_Risk_Mapping_Statistics.csv")
    file_inflation_rates = os.path.join(raw_data_folder, "Inflation_Rates.csv")
    file_inflation_affectors = os.path.join(raw_data_folder, "Inflation_Affectors_Statistics.csv")

    # Load CSV files into pandas DataFrames
    df_bank1 = pd.read_csv(file_bank1)
    df_bank2 = pd.read_csv(file_bank2)
    df_customer_risk = pd.read_csv(file_customer_risk)
    df_inflation_rates = pd.read_csv(file_inflation_rates)
    df_inflation_affectors = pd.read_csv(file_inflation_affectors)

    # Return as a dictionary for organized access
    return {
        "bank1": df_bank1,
        "bank2": df_bank2,
        "customer_risk": df_customer_risk,
        "inflation_rates": df_inflation_rates,
        "inflation_affectors": df_inflation_affectors
    }
