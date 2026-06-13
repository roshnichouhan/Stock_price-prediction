import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import pickle
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "stock.csv")

df = pd.read_csv(file_path)

# Feature
df["Day"] = np.arange(len(df))

X = df[["Day"]]
y = df["Close"]

# -----------------------------
# SPLIT DATA (IMPORTANT)
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# TRAIN MODEL
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# PREDICTION
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# REAL METRICS
# -----------------------------
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

metrics = {
    "r2": float(r2),
    "rmse": float(rmse),
    "mae": float(mae)
}

# -----------------------------
# SAVE MODEL
# -----------------------------
os.makedirs("backend", exist_ok=True)

with open("backend/model.pkl", "wb") as f:
    pickle.dump(model, f)

# -----------------------------
# SAVE METRICS
# -----------------------------
with open("backend/metrics.json", "w") as f:
    json.dump(metrics, f)

print("Model trained successfully with real metrics!")
print(metrics)
