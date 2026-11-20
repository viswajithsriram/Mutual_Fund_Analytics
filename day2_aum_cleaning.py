import pandas as pd

# Load original AUM dataset
df = pd.read_csv(
    "data/raw/1788499984134-b0cbf625-03_aum_by_fund_house.csv"
)

print("Original Shape:", df.shape)

# Clean text columns
df["fund_house"] = df["fund_house"].str.strip()

# Convert date column
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Convert numeric columns
numeric_cols = [
    "aum_lakh_crore",
    "aum_crore",
    "num_schemes"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove missing and duplicate rows
df = df.dropna()
df = df.drop_duplicates()

# Validate positive values
df = df[
    (df["aum_lakh_crore"] > 0) &
    (df["aum_crore"] > 0) &
    (df["num_schemes"] > 0)
]

# Sort data
df = df.sort_values(["fund_house", "date"])

# Save cleaned dataset
df.to_csv(
    "data/processed/aum_by_fund_house_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Missing Values:")
print(df.isnull().sum())
print("AUM Cleaning Completed!")