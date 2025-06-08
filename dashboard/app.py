from flask import Flask, render_template_string
import pandas as pd
import plotly.graph_objects as go
import os

app = Flask(__name__)

@app.route("/")
def dashboard():
    # Load usage data
    data_file = "data/energy_readings.csv"
    forecast_file = "models/forecast_arima.csv"
    if not os.path.exists(data_file):
        return "⚠️ No data available. Run synthetic_data_gen.py first."

    df = pd.read_csv(data_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Load forecast
    if os.path.exists(forecast_file):
        forecast_df = pd.read_csv(forecast_file)
    else:
        forecast_df = pd.DataFrame({"hour": [], "forecast_kW": []})

    # --- PLOT: Actual vs Forecast ---
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['timestamp'][-24:], y=df['power_kW'][-24:], mode='lines+markers', name='Actual Power'))
    if not forecast_df.empty:
        fig.add_trace(go.Scatter(x=pd.date_range(start=df['timestamp'].iloc[-1], periods=24, freq='H'),
                                 y=forecast_df['forecast_kW'], mode='lines+markers', name='Forecast'))
    fig.update_layout(title="Power Usage vs Forecast", xaxis_title="Time", yaxis_title="kW")
    plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    # --- Calculate cost ---
    tariff = 6.0  # ₹/kWh
    today = df[df['timestamp'].dt.date == df['timestamp'].max().date()]
    total_kWh = today['power_kW'].sum()
    cost_today = total_kWh * tariff

    # --- Smart Tip ---
    peak_hours = today[today['power_kW'] > 1.2]
    if not peak_hours.empty:
        tip = "💡 Tip: Consider shifting heavy appliance use to non-peak hours (before 6 PM or after 10 PM)."
    else:
        tip = "✅ You're using energy efficiently today!"

    # --- HTML Output ---
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Energy Dashboard</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="refresh" content="60"> <!-- Auto refresh every 60s -->
    </head>
    <body class="container mt-4">
        <h1 class="mb-4">📊 AI Energy Usage Dashboard</h1>
        <div class="row mb-3">
            <div class="col-md-4">
                <div class="card text-white bg-primary mb-3">
                    <div class="card-body">
                        <h5 class="card-title">Today's Usage</h5>
                        <p class="card-text">{{ total_kWh | round(2) }} kWh</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card text-white bg-success mb-3">
                    <div class="card-body">
                        <h5 class="card-title">Estimated Cost</h5>
                        <p class="card-text">₹ {{ cost_today | round(2) }}</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card text-white bg-warning mb-3">
                    <div class="card-body">
                        <h5 class="card-title">Smart Tip</h5>
                        <p class="card-text">{{ tip }}</p>
                    </div>
                </div>
            </div>
        </div>

        <h4>Usage Chart (Actual vs Forecast)</h4>
        <div class="card p-2">
            {{ plot_html | safe }}
        </div>
    </body>
    </html>
    """, plot_html=plot_html, total_kWh=total_kWh, cost_today=cost_today, tip=tip)


if __name__ == "__main__":
    app.run(debug=True)
