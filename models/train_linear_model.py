import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("data/energy_readings.csv")
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
X = df[['hour', 'temperature_C']]
y = df['power_kW']

model = LinearRegression().fit(X, y)
with open('models/saved_models/linear_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("✅ Linear model trained and saved")
