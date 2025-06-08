import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import os

# Load the energy usage data
df = pd.read_csv("data/energy_readings.csv")

# Use power_kW as the time series
ts = df["power_kW"]

# Build and fit ARIMA model (simple configuration)
model = ARIMA(ts, order=(2, 1, 2))  # ARIMA(p=2, d=1, q=2) is a good starting point
fitted_model = model.fit()

# Forecast for next 24 hours
forecast = fitted_model.forecast(steps=24)

# Save forecast to CSV
os.makedirs("models", exist_ok=True)
forecast_df = pd.DataFrame({"hour": range(24), "forecast_kW": forecast})
forecast_df.to_csv("models/forecast_arima.csv", index=False)

print("✅ ARIMA forecast saved to models/forecast_arima.csv")
