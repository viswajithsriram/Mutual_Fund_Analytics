import pandas as pd

# Load original folio dataset
df = pd.read_csv(
    "data/raw/1788499985036-da4a0c4a-06_industry_folio_count.csv"
)

print("Original Shape:", df.shape)

# Convert month to datetime
df["month"] = pd.to_datetime(
    df["month"], format="%Y-%m", errors="coerce"
)

# Convert folio columns to numeric
numeric_cols = [
    "total_folios_crore",
    "equity_folios_crore",
    "debt_folios_crore",
    "hybrid_folios_crore",
    "others_folios_crore"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove missing and duplicate rows
df = df.dropna()
df = df.drop_duplicates(subset=["month"])

# Validate positive values
for col in numeric_cols:
    df = df[df[col] >= 0]

# Sort by month
df = df.sort_values("month")

# Save cleaned dataset
df.to_csv(
    "data/processed/industry_folio_count_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Missing Values:")
print(df.isnull().sum())
print("Folio Cleaning Completed!")