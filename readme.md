# AI Energy Monitoring System for Indian Homes

An affordable, end-to-end Python-based AI solution to **monitor, predict, and optimize** energy usage in Indian households and classrooms.

## 🔥 Features

- Real-time data simulation and hardware logging
- SQLite-based local storage
- AI-based power prediction (Linear Regression, ARIMA)
- Flask web dashboard with Plotly
- Smart recommendations and simulated appliance control
- Daily/Weekly cost-savings reports (₹4–8/kWh tariffs)

## 📁 Project Structure

- `data/`: Simulated/sensor data
- `database/`: SQLite scripts
- `models/`: ML training and forecasting
- `dashboard/`: Flask dashboard
- `integration/`: Main pipeline + smart control
- `reports/`: Cost-saving and optimization reports

## 🚀 Run the Pipeline

```bash
# Step-by-step
python data/synthetic_data_gen.py
python database/setup_db.py
python database/insert_data.py
python models/train_linear_model.py
python dashboard/app.py
```
