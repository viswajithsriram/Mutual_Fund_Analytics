
import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///bluestock_mf.db")

# Read cleaned CSV files
fund = pd.read_csv("data/processed/fund_master_cleaned.csv")
nav = pd.read_csv("data/processed/nav_history_cleaned.csv")
transactions = pd.read_csv("data/processed/investor_transactions_cleaned.csv")
performance = pd.read_csv("data/processed/scheme_performance_cleaned.csv")
aum = pd.read_csv("data/processed/aum_by_fund_house_cleaned.csv")
sip = pd.read_csv("data/processed/monthly_sip_inflows_cleaned.csv")
category = pd.read_csv("data/processed/category_inflows_cleaned.csv")
folio = pd.read_csv("data/processed/industry_folio_count_cleaned.csv")
portfolio = pd.read_csv("data/processed/portfolio_holdings_cleaned.csv")
benchmark = pd.read_csv("data/processed/benchmark_indices_cleaned.csv")

# Match fund master column with database
fund = fund.rename(columns={"risk_category": "risk_grade"})

# Check whether database already contains data
with engine.connect() as conn:
    count = conn.execute(
        text("SELECT COUNT(*) FROM dim_fund")
    ).scalar()

if count > 0:
    print("Database already contains data. Loading stopped to avoid duplicates.")
    raise SystemExit

# Prepare fund dimension
dim_fund = fund.copy()
dim_fund["amfi_code"] = dim_fund["amfi_code"].astype(int)

# Prepare date dimension
date_series = pd.concat([
    pd.to_datetime(nav["date"]),
    pd.to_datetime(transactions["transaction_date"]),
    pd.to_datetime(aum["date"]),
    pd.to_datetime(benchmark["date"])
]).dropna().dt.normalize().drop_duplicates().sort_values()

dim_date = pd.DataFrame({
    "date_value": date_series.dt.strftime("%Y-%m-%d").values,
    "date_id": date_series.dt.strftime("%Y%m%d").astype(int).values,
    "year": date_series.dt.year.values,
    "month": date_series.dt.month.values,
    "month_name": date_series.dt.month_name().values,
    "quarter": date_series.dt.quarter.values
})

date_lookup = dict(zip(dim_date["date_value"], dim_date["date_id"]))

def add_date_id(df, column):
    df = df.copy()
    dates = pd.to_datetime(df[column]).dt.strftime("%Y-%m-%d")
    df["date_id"] = dates.map(date_lookup)
    return df

# Prepare NAV
fact_nav = add_date_id(nav, "date")
fact_nav = fact_nav[["amfi_code", "date_id", "nav"]]

# Prepare transactions
fact_transactions = add_date_id(transactions, "transaction_date")
fact_transactions = fact_transactions[
    [
        "investor_id", "amfi_code", "date_id",
        "transaction_type", "amount_inr", "state",
        "city", "city_tier", "age_group", "gender",
        "annual_income_lakh", "payment_mode", "kyc_status"
    ]
]

# Prepare performance
fact_performance = performance.copy()

# Prepare AUM
fact_aum = add_date_id(aum, "date")
fact_aum = fact_aum[
    ["date_id", "fund_house", "aum_lakh_crore",
     "aum_crore", "num_schemes"]
]

# Prepare portfolio holdings
fact_portfolio_holdings = portfolio.copy()

# Prepare benchmark indices
fact_benchmark_indices = add_date_id(benchmark, "date")
fact_benchmark_indices = fact_benchmark_indices[
    ["date_id", "index_name", "close_value"]
]

# Load all datasets
tables = {
    "dim_fund": dim_fund,
    "dim_date": dim_date,
    "fact_nav": fact_nav,
    "fact_transactions": fact_transactions,
    "fact_performance": fact_performance,
    "fact_aum": fact_aum,
    "fact_sip": sip,
    "fact_category_inflows": category,
    "fact_folio_count": folio,
    "fact_portfolio_holdings": fact_portfolio_holdings,
    "fact_benchmark_indices": fact_benchmark_indices
}

with engine.begin() as conn:
    for table_name, dataframe in tables.items():
        dataframe.to_sql(
            table_name,
            con=conn,
            if_exists="append",
            index=False
        )
        print(table_name, "loaded:", len(dataframe), "rows")

print("\nAll datasets loaded successfully!")
