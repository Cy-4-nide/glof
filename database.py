import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect("glof_data.db")
cursor = conn.cursor()

# Create a table for storing real-time data
cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    water_level_m REAL,
    temperature_c REAL,
    humidity REAL,
    rainfall_mm REAL
)
""")

conn.commit()
conn.close()

print("✅ Database and table created successfully!")
