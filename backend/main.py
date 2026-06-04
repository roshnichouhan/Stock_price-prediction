from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI(title="Stock Price Prediction API")

# -----------------------------
# Load model safely
# -----------------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("model.pkl not found")

model = pickle.load(open(MODEL_PATH, "rb"))

# -----------------------------
# Input schema
# -----------------------------
class StockRequest(BaseModel):
    day: int

# -----------------------------
# Home route
# -----------------------------
@app.get("/")
def home():
    return {"message": "Stock Price API Running 🚀"}

# -----------------------------
# Prediction route
# -----------------------------
@app.post("/predict")
def predict(data: StockRequest):

    try:
        input_data = np.array([[data.day]])

        prediction = model.predict(input_data)[0]

        return {
            "input_day": data.day,
            "predicted_price": float(prediction)
        }

    except Exception as e:
        return {
            "error": str(e)
        }