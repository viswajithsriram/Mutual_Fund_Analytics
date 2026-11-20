import pandas as pd

# Load original fund master dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("Original Shape:", df.shape)

# Remove accidental invalid rows
df["amfi_code"] = pd.to_numeric(df["amfi_code"], errors="coerce")
df = df.dropna(subset=["amfi_code"])

# Convert AMFI code to integer
df["amfi_code"] = df["amfi_code"].astype(int)

# Remove duplicate AMFI codes
df = df.drop_duplicates(subset=["amfi_code"])

# Clean text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Convert launch date
df["launch_date"] = pd.to_datetime(
    df["launch_date"], errors="coerce"
)

# Save cleaned dataset
df.to_csv(
    "data/processed/fund_master_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Missing Values:")
print(df.isnull().sum())
print("Fund Master Cleaning Completed!")