from scripts.load_data import load_all_data
import pandas as pd
import os

# Load data using your custom loader
bank1, bank2, customer_risk, inflation, inflation_effectors = load_all_data()

# Merge Bank Stability 1 & 2
merged_bank = pd.merge(bank1, bank2, on=["Year", "Month"], how="outer")
merged_bank["Bank_Stability_Score"] = merged_bank[["Factors Affecting Bank Stability", "MONTHS PER YEAR"]].mean(axis=1)

# Aggregate Customer Risk (Kenya-wide average per month/year)
customer_summary = customer_risk.groupby(["Year", "Month"]).agg({
    "Risk_Score": "mean"
}).reset_index()

customer_summary["Risk_Category"] = pd.cut(customer_summary["Risk_Score"],
                                           bins=[0, 0.3, 0.7, 1.0],
                                           labels=["Low", "Medium", "High"])

# Merge Inflation Data with Effectors
inflation_full = pd.merge(inflation, inflation_effectors, on=["Year"], how="left")

# Merge all data together
step1 = pd.merge(merged_bank, customer_summary, on=["Year", "Month"], how="left")
final_data = pd.merge(step1, inflation_full, on=["Year", "Month"], how="left")

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