import os

def safe_delete(path):
    try:
        if os.path.exists(path):
            os.remove(path)
            print(f"🗑️ Deleted: {path}")
        else:
            print(f"⚠️ Not found: {path}")
    except Exception as e:
        print(f"❌ Error deleting {path}: {e}")

# Clean up data, database, model, and dashboard output
FILES_TO_DELETE = [
    "data/energy_readings.csv",
    "database/energy_data.db",
    "models/saved_models/linear_model.pkl",
    "models/forecast_arima.csv",
    "dashboard/templates/plot.html"
]

print("🔁 Resetting project state...")
for file in FILES_TO_DELETE:
    safe_delete(file)

print("\n✅ Project reset complete. You can now re-run from step 1.")
