import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def simulate_energy_readings(start_date, days):
    data = []
    curr_time = datetime.strptime(start_date, "%Y-%m-%d")
    end_time = curr_time + timedelta(days=days)

    while curr_time < end_time:
        hour = curr_time.hour
        # Usage pattern (kW)
        if 6 <= hour <= 9:
            power = np.random.uniform(0.8, 1.2)
        elif 10 <= hour <= 16:
            power = np.random.uniform(0.3, 0.6)
        elif 18 <= hour <= 22:
            power = np.random.uniform(1.0, 1.5)
        else:
            power = np.random.uniform(0.2, 0.4)

        voltage = np.random.uniform(180, 260)
        current = (power * 1000) / voltage
        temperature = np.random.uniform(25, 35)  # Simulate hot summer

        data.append([curr_time, round(current, 2), round(voltage, 2),
                     round(power, 2), round(temperature, 2)])
        curr_time += timedelta(minutes=60)

    df = pd.DataFrame(data, columns=["timestamp", "current_A", "voltage_V", "power_kW", "temperature_C"])
    df.to_csv("data/energy_readings.csv", index=False)
    print("✅ Data simulated and saved!")

simulate_energy_readings("2025-05-01", 30)
