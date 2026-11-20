
import pandas as pd
import os

# Load original Investor Transactions dataset
input_file = "data/raw/1788499980509-304c1255-08_investor_transactions.csv"

df = pd.read_csv(input_file)

print("Original Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nTransaction Types:")
print(df["transaction_type"].value_counts())

print("\nKYC Status Values:")
print(df["kyc_status"].value_counts())

print("\nInvalid Amounts (Amount <= 0):")
print((df["amount_inr"] <= 0).sum())

# Standardise transaction type values
df["transaction_type"] = (
    df["transaction_type"].str.strip().str.title()
)

df["transaction_type"] = df["transaction_type"].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

# Standardise KYC status
df["kyc_status"] = df["kyc_status"].str.strip().str.title()

# Check standardised values
print("\nStandardised Transaction Types:")
print(df["transaction_type"].value_counts())

print("\nStandardised KYC Status:")
print(df["kyc_status"].value_counts())

# Convert transaction date to datetime
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

print("\nTransaction Date Data Type:")
print(df["transaction_date"].dtype)

print("\nInvalid Dates:")
print(df["transaction_date"].isnull().sum())

# Save cleaned dataset
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("\nCleaned Investor Transactions saved successfully!")
print("Final Shape:", df.shape)
