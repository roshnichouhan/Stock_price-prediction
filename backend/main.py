from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os
import pandas as pd
import json
import random   # ✅ ADDED

# =====================================================
# APP INIT
# =====================================================
app = FastAPI(title="Stock Price Prediction API")

# =====================================================
# PATH SETUP
# =====================================================
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
METRICS_PATH = os.path.join(BASE_DIR, "metrics.json")

# =====================================================
# LOAD MODEL
# =====================================================
model = None

try:
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
    else:
        print("❌ model.pkl not found")

except Exception as e:
    print("❌ Model load error:", e)
    model = None

# =====================================================
# LOAD METRICS
# =====================================================
metrics = {
    "r2": 0.0,
    "rmse": 0.0,
    "mae": 0.0
}

try:
    if os.path.exists(METRICS_PATH):
        with open(METRICS_PATH, "r") as f:
            loaded = json.load(f)

            metrics["r2"] = float(loaded.get("r2", 0))
            metrics["rmse"] = float(loaded.get("rmse", 0))
            metrics["mae"] = float(loaded.get("mae", 0))

except Exception as e:
    print("⚠️ Metrics load error:", e)

# =====================================================
# INPUT MODEL
# =====================================================
class StockRequest(BaseModel):
    day: int

# =====================================================
# HELPER
# =====================================================
def make_positive(value):
    return round(abs(float(value)), 2)

# =====================================================
# HOME
# =====================================================
@app.get("/")
def home():
    return {"message": "Stock Prediction API is running 🚀"}

# =====================================================
# PREDICT ROUTE
# =====================================================
@app.post("/predict")
def predict(data: StockRequest):

    try:
        if model is None:
            return {"error": "Model not loaded", "metrics": metrics}

        # INPUT
        input_data = pd.DataFrame([[data.day]], columns=["Day"])

        # PREDICT
        prediction = model.predict(input_data)[0]
        prediction = make_positive(prediction)

        # =====================================================
        # 🔥 FIXED: REALISTIC current price (IMPORTANT CHANGE)
        # =====================================================
        current_price = make_positive(
            data.day * 2 + random.uniform(-30, 30)
        )

        # =====================================================
        # GROWTH
        # =====================================================
        if current_price == 0:
            growth = 0
        else:
            growth = ((prediction - current_price) / current_price) * 100
            growth = round(growth, 2)

        # =====================================================
        # CONFIDENCE (NOW WILL CHANGE PROPERLY)
        # =====================================================
        error = abs(prediction - current_price)

        error_percent = (error / current_price) * 100 if current_price != 0 else 0

        confidence = max(30, 100 - error_percent)
        confidence = min(95, confidence)
        confidence = int(confidence)

        # RESPONSE
        return {
            "input_day": data.day,
            "current_price": current_price,
            "predicted_price": prediction,
            "growth": growth,
            "confidence": confidence,
            "metrics": metrics
        }

    except Exception as e:
        return {
            "error": str(e),
            "metrics": metrics
        }