
import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

columns = {
    "scheme_name": "TEXT",
    "fund_house": "TEXT",
    "category": "TEXT",
    "plan": "TEXT",
    "risk_grade": "TEXT"
}

existing_columns = [
    row[1] for row in conn.execute("PRAGMA table_info(fact_performance)")
]

for column, data_type in columns.items():
    if column not in existing_columns:
        conn.execute(
            f"ALTER TABLE fact_performance ADD COLUMN {column} {data_type}"
        )

conn.commit()
conn.close()

print("fact_performance table updated successfully!")
