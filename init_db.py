from db import get_db

conn = get_db()
cur = conn.cursor()

# Users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    role TEXT,
    is_active BOOLEAN
)
""")

# Records table
cur.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    type TEXT,
    category TEXT,
    date TEXT,
    note TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")