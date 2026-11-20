
import pandas as pd
import os

# Load original Scheme Performance dataset
input_file = "data/raw/1788499985420-bb134abf-07_scheme_performance.csv"

df = pd.read_csv(input_file)

print("Original Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

# Check missing values and duplicates
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Validate return columns are numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nNon-numeric Return Values:")
print(df[return_columns].isnull().sum())

# Check expense ratio range
print("\nExpense Ratio Outside 0.1% to 2.5%:")
print(df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
][["scheme_name", "expense_ratio_pct"]])

# Check return value ranges for anomaly review
print("\nReturn Value Ranges:")
print(df[return_columns].agg(["min", "max"]))

# Save cleaned dataset
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("\nCleaned Scheme Performance saved successfully!")
print("Final Shape:", df.shape)
