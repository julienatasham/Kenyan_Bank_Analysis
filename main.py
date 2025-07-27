from scripts.load_data import load_all_data
import pandas as pd
import os
import pandas as pd

# Step 1: Load Data
bank1 = pd.read_csv("Bank_Stability_1.csv")
bank2 = pd.read_csv("Bank_Stability_2.csv")
monthly_factors = pd.read_csv("Factors_Bank_Monthly.csv")
inflation = pd.read_csv("Inflation_Rates.csv")
annual_factors = pd.read_csv("Inflation_Annual_Factors.csv")

# Step 2: Combine Bank Stability (assume same columns)
bank_combined = pd.concat([bank1, bank2], ignore_index=True)

# Step 3: Merge Bank Stability with Monthly Factors
bank_with_factors = pd.merge(
    bank_combined,
    monthly_factors,
    on=["Year", "Month"],
    how="left"
)

# Step 4: Merge with Monthly Inflation
bank_with_inflation = pd.merge(
    bank_with_factors,
    inflation,
    on=["Year", "Month"],
    how="left"
)

# Step 5: Merge with Annual Inflation Factors
final_merged = pd.merge(
    bank_with_inflation,
    annual_factors,
    on="Year",
    how="left"
)

# Step 6: Save the processed dataset
final_merged.to_csv("Processed_Bank_Stability_Data.csv", index=False)

# Optional: Show a quick summary
print("Final dataset shape:", final_merged.shape)
print(final_merged.head())

# Optional: Add calculated insights
final_data["Risk_to_Stability_Ratio"] = final_data["Risk_Score"] / final_data["Bank_Stability_Score"]

#  Make sure the 'processed' folder exists
os.makedirs("processed", exist_ok=True)

#  Save the processed data
final_data.to_csv("processed/ProcessedBankAnalysis.csv", index=False)

# Print confirmation and data preview
print(" File saved successfully at: processed/ProcessedBankAnalysis.csv")
print("Shape:", final_data.shape)
print(final_data.head(10))

print("Processing complete! Data saved to 'processed/Processed_Bank_Analysis.csv'")