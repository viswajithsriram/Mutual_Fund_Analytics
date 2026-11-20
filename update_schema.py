
import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

conn.execute("PRAGMA foreign_keys = OFF")

conn.execute("ALTER TABLE fact_transactions RENAME TO old_fact_transactions")

conn.execute("""
CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id TEXT,
    amfi_code INTEGER,
    date_id INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
)
""")

conn.execute("DROP TABLE old_fact_transactions")

conn.commit()
conn.close()

print("fact_transactions table updated successfully!")
