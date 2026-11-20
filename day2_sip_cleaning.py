import pandas as pd

# Load original SIP dataset
df = pd.read_csv(
    "data/raw/1788499984405-d702a6c6-04_monthly_sip_inflows.csv"
)

print("Original Shape:", df.shape)

# Convert month column
df["month"] = pd.to_datetime(
    df["month"], format="%Y-%m", errors="coerce"
)

# Convert numeric columns
numeric_cols = [
    "sip_inflow_crore",
    "active_sip_accounts_crore",
    "new_sip_accounts_lakh",
    "sip_aum_lakh_crore",
    "yoy_growth_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove duplicate months
df = df.drop_duplicates(subset=["month"])

# Sort by month
df = df.sort_values("month")

# Validate positive values
df = df[
    (df["sip_inflow_crore"] > 0) &
    (df["active_sip_accounts_crore"] > 0) &
    (df["new_sip_accounts_lakh"] > 0) &
    (df["sip_aum_lakh_crore"] > 0)
]

# Save cleaned dataset
df.to_csv(
    "data/processed/monthly_sip_inflows_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Missing Values:")
print(df.isnull().sum())
print("SIP Cleaning Completed!")