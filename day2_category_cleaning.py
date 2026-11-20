import pandas as pd

# Load original category inflows dataset
df = pd.read_csv(
    "data/raw/1788499984721-4b860901-05_category_inflows.csv"
)

print("Original Shape:", df.shape)

# Clean category names
df["category"] = df["category"].str.strip()

# Convert month to datetime
df["month"] = pd.to_datetime(
    df["month"], format="%Y-%m", errors="coerce"
)

# Convert inflow to numeric
df["net_inflow_crore"] = pd.to_numeric(
    df["net_inflow_crore"], errors="coerce"
)

# Remove missing and duplicate rows
df = df.dropna()
df = df.drop_duplicates(subset=["month", "category"])

# Sort data
df = df.sort_values(["month", "category"])

# Save cleaned dataset
df.to_csv(
    "data/processed/category_inflows_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Missing Values:")
print(df.isnull().sum())
print("Category Inflows Cleaning Completed!")