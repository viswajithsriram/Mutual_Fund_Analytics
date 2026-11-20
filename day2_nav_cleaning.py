
import pandas as pd
import os

# Load original NAV history
input_file = "data/raw/02_nav_history.csv"

df = pd.read_csv(input_file)

print("Original Shape:", df.shape)
print("\nOriginal Columns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nInvalid NAV Values (NAV <= 0):")
print((df["nav"] <= 0).sum())

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by AMFI code and date
df = df.sort_values(
    by=["amfi_code", "date"]
).reset_index(drop=True)

print("\nDate Data Type:")
print(df["date"].dtype)

print("\nSorted Data:")
print(df.head())

# Forward-fill missing NAV values within each scheme
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Validate NAV values
print("\nMissing NAV after forward-fill:", df["nav"].isnull().sum())
print("Invalid NAV after cleaning:", (df["nav"] <= 0).sum())

# Save cleaned dataset
os.makedirs("data/processed", exist_ok=True)

df.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("\nCleaned NAV dataset saved successfully!")
print("Final Shape:", df.shape)
