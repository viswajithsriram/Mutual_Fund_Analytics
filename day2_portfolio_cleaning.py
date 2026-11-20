
import pandas as pd

df = pd.read_csv("data/raw/1788499982117-e3d6ab98-09_portfolio_holdings.csv")

print("Original Shape:", df.shape)

# Clean text columns
for col in ["stock_symbol", "stock_name", "sector"]:
    df[col] = df[col].astype("string").str.strip()

# Convert columns to correct data types
df["amfi_code"] = pd.to_numeric(df["amfi_code"], errors="coerce")

for col in ["weight_pct", "market_value_cr", "current_price_inr"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["portfolio_date"] = pd.to_datetime(
    df["portfolio_date"], errors="coerce"
)

# Remove invalid and duplicate rows
df = df.dropna()

df = df.drop_duplicates(
    subset=["amfi_code", "stock_symbol", "portfolio_date"]
)

# Validate values
df = df[
    (df["amfi_code"] > 0) &
    (df["weight_pct"] >= 0) &
    (df["weight_pct"] <= 100) &
    (df["market_value_cr"] >= 0) &
    (df["current_price_inr"] > 0)
]

df["amfi_code"] = df["amfi_code"].astype(int)

# Sort and save
df = df.sort_values(
    ["amfi_code", "portfolio_date", "stock_symbol"]
)

df.to_csv(
    "data/processed/portfolio_holdings_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Missing Values:")
print(df.isnull().sum())

print("Portfolio Holdings Cleaning Completed!")
