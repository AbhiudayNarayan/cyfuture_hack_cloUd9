import sqlite3

conn = sqlite3.connect("database/energy_data.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    current_A REAL,
    voltage_V REAL,
    power_kW REAL,
    temperature_C REAL
)
""")
conn.commit()
conn.close()
