import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("bluestock_mf.db")

# Enable foreign keys
conn.execute("PRAGMA foreign_keys = ON")

# Read schema.sql file
with open("schema.sql", "r") as file:
    schema = file.read()

# Create all tables
conn.executescript(schema)

conn.commit()
conn.close()

print("Database created successfully!")
print("All 6 tables created.")