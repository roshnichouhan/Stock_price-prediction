import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(BASE_DIR, "data", "stock.csv")

df = pd.read_csv(file_path)

# Reset index
df = df.reset_index()

# Create feature (Day number)
df["Day"] = np.arange(len(df))

# Features & Target
X = df[["Day"]]
y = df["Close"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
os.makedirs("backend", exist_ok=True)

with open("backend/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully")