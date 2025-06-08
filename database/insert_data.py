import pandas as pd
import sqlite3

df = pd.read_csv("data/energy_readings.csv")
conn = sqlite3.connect("database/energy_data.db")
df.to_sql("readings", conn, if_exists="append", index=False)
conn.close()
print("✅ Data inserted into SQLite database")
