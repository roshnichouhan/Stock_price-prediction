# 📈 Stock Price Prediction System

A Machine Learning based Stock Price Prediction application that predicts future stock trends using historical stock market data.

## 🚀 Project Overview

This project uses Machine Learning algorithms to analyze historical stock prices and predict future stock movements. The application consists of:

- Backend API for model prediction
- Frontend interface for user interaction
- Historical stock dataset
- Machine Learning prediction model

---

## 📂 Project Structure

```bash
Stock_price-prediction/
│
├── backend/
│   ├── train_model.py
│   ├── predict.py
│   ├── model.pkl
│   └── utils.py
│
├── data/
│   └── stock_data.csv
│
├── frontend/
│   └── app.py
│
├── venv/
│
├── requirements.txt
│
└── README.md
```

---

## 🛠️ Technologies Used

### Frontend
- Streamlit

### Backend
- Python
- Flask / FastAPI

### Machine Learning
- Scikit-Learn
- Pandas
- NumPy

### Visualization
- Plotly
- Matplotlib

---

## 📊 Features

✅ Stock Price Prediction

✅ Interactive Dashboard

✅ Historical Data Analysis

✅ Data Visualization

✅ Machine Learning Model Integration

✅ User Friendly Interface

---

## ⚙️ Installation

### 1 Clone Repository

```bash
git clone https://github.com/yourusername/Stock_price-prediction.git

cd Stock_price-prediction
```

### 2 Create Virtual Environment

```bash
python -m venv venv
```

### 3 Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 4 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Start Backend Server

```bash
cd backend

python app.py
```

or

```bash
uvicorn main:app --reload
```

---

### Start Frontend

Open a new terminal:

```bash
cd frontend

streamlit run app.py
```

---

## 📈 Machine Learning Workflow

### Data Collection

Historical stock market data is collected and stored in:

```bash
data/stock_data.csv
```

### Data Preprocessing

- Handle Missing Values
- Feature Engineering
- Data Normalization

### Model Training

Algorithms that can be used:

- Linear Regression
- Random Forest Regressor
- XGBoost
- LSTM (Advanced)

### Model Evaluation

Metrics:

- MAE
- MSE
- RMSE
- R² Score

---

## 🔥 Sample Prediction Workflow

1. User enters stock symbol.
2. Frontend sends request to backend.
3. Backend loads trained model.
4. Model predicts future stock price.
5. Result displayed on dashboard.

---

## 📦 Requirements

```txt
streamlit
pandas
numpy
plotly
matplotlib
scikit-learn
flask
requests
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 📸 Application Screens

### Dashboard

- Historical Price Graph
- Predicted Price Graph
- Market Trend Analysis

---

## 🎯 Future Improvements

- Real-Time Stock Data Integration
- Deep Learning (LSTM/GRU)
- Multiple Stock Comparison
- Portfolio Analysis
- Buy/Sell Recommendations
- Sentiment Analysis from News

---

## 👨‍💻 Author

**Roshni Chauhan**

Frontend Developer | Data Science Enthusiast

Skills:
- Python
- Machine Learning
- Streamlit
- React
- Node.js
- MongoDB

---

## ⭐ Contribute

Contributions are welcome.

1. Fork Repository
2. Create New Branch
3. Commit Changes
4. Push Changes
5. Create Pull Request

---

## 📄 License

This project is licensed under the MIT License.
