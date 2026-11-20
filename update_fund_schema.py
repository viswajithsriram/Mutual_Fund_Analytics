
import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

columns = {
    "launch_date": "TEXT",
    "benchmark": "TEXT",
    "expense_ratio_pct": "REAL",
    "exit_load_pct": "REAL",
    "min_sip_amount": "REAL",
    "min_lumpsum_amount": "REAL",
    "fund_manager": "TEXT",
    "sebi_category_code": "TEXT"
}

existing_columns = [
    row[1] for row in conn.execute("PRAGMA table_info(dim_fund)")
]

for column, data_type in columns.items():
    if column not in existing_columns:
        conn.execute(
            f"ALTER TABLE dim_fund ADD COLUMN {column} {data_type}"
        )

conn.commit()
conn.close()

print("dim_fund table updated successfully!")
