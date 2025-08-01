from scripts.load_data import load_all_data
import pandas as pd
import os
import pandas as pd

# Step 1: Load Data
bank1 = pd.read_csv(r"C:\\Users\USER\\OneDrive\\Desktop\Kenyan_Bank_Analysis\\data\\raw\\Bank_Stability_Analysis.csv" ,encoding='ISO-8859-1')
bank2 = pd.read_csv(r"C:\\Users\\USER\OneDrive\\Desktop\\Kenyan_Bank_Analysis\\data\raw\\Bank_Stability_Analysis2.csv" ,encoding='ISO-8859-1')
inflation_rates = pd.read_csv(r"C:\\Users\USER\\OneDrive\\Desktop\\Kenyan_Bank_Analysis\\data\\raw\\Inflation Rates.csv", encoding='ISO-8859-1')
inflation_affectors = pd.read_csv(r"C:\\Users\\USER\\OneDrive\\Desktop\\Kenyan_Bank_Analysis\\data\\raw\\Factor_affecting_Inflation.csv" ,encoding='ISO-8859-1')

# Step 2: Combine Bank Stability (assume same columns)
bank_combined = pd.concat([bank1, bank2], ignore_index=True)
bank_combined = bank_combined.drop_duplicates (subset=['Year','Factors_affecting_bank_stability'] , keep='first', inplace=True)

#Step 3
bank_with_inflation = pd.merge(
    bank_combined,
    inflation_rates,
    on=["Year","annual_average_inflation"],
    how="left"
)

# Step 4: Merge with Annual Inflation Factors
final_merged = pd.merge(
    bank_with_inflation,
    inflation_affectors,
    on="Factors_affecting_inflation",
    how="left"
)

# Step 5: Save the processed dataset
final_merged.to_csv("Processed_Bank_Stability_Data.csv", index=False)

# Optional: Show a quick summary
print("Final dataset shape:", final_merged.shape)
print(final_merged.head())
# Step 5: Save the processed dataset
final_merged.to_csv("Processed_Bank_Stability_Data.csv", index=False)

# Optional: Show a quick summary
print("Final dataset shape:", final_merged.shape)
print(final_merged.head())

# Optional: Add calculated insights
final_merged["Risk_to_Stability_Ratio"] = final_merged["Risk_Score"] / final_merged["Bank_Stability_Score"]

#  Make sure the 'processed' folder exists
os.makedirs("processed", exist_ok=True)

#  Save the processed data
final_merged.to_csv("processed/ProcessedBankAnalysis.csv", index=False)

# Print confirmation and data preview
print(" File saved successfully at: processed/ProcessedBankAnalysis.csv")
print("Shape:", final_merged.shape)
print(final_merged.head(10))

print("Processing complete! Data saved to 'processed/Processed_Bank_Analysis.csv'")