
import pandas as pd

df = pd.read_csv(
    "data/raw/1788499982615-f9647ab2-10_benchmark_indices.csv"
)

print("Original Shape:", df.shape)

# Clean index name
df["index_name"] = df["index_name"].astype("string").str.strip()

# Convert date and close value
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["close_value"] = pd.to_numeric(df["close_value"], errors="coerce")

# Remove missing and invalid rows
df = df.dropna()
df = df[df["close_value"] > 0]

# Remove duplicates
df = df.drop_duplicates(subset=["date", "index_name"])

# Sort data
df = df.sort_values(["index_name", "date"])

# Save cleaned dataset
df.to_csv(
    "data/processed/benchmark_indices_cleaned.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Missing Values:")
print(df.isnull().sum())

print("Benchmark Indices Cleaning Completed!")
