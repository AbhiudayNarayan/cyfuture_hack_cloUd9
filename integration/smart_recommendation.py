import pandas as pd

df = pd.read_csv("data/energy_readings.csv")
latest = df.iloc[-1]

if latest['power_kW'] > 1.2:
    print(f"🔴 High usage detected at {latest['timestamp']}")
    print("💡 Suggestion: Turn off non-essential devices to save ₹20/hour.")
