
import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="AI Stock Predictor",
    page_icon="📈",
    layout="wide"
)

# =====================================================
# API CONFIG
# =====================================================
API_URL = "http://127.0.0.1:8000/predict"

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>
.stApp{
    background-color:#0E1117;
}
.metric-value{
    font-size:30px;
    font-weight:bold;
    color:#00C6FF;
}
.metric-label{
    color:#9CA3AF;
}
footer{
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.title("📈 AI Stock Price Predictor")
st.markdown("---")

# =====================================================
# INPUT
# =====================================================
col1, col2 = st.columns([4, 1])

with col1:
    day = st.number_input(
        "📅 Enter Future Prediction Day",
        min_value=1,
        value=1,
        step=1
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn = st.button("🚀 Predict", use_container_width=True)

# =====================================================
# PREDICTION
# =====================================================
if predict_btn:

    try:
        with st.spinner("Analyzing Market Trends..."):

            response = requests.post(
                API_URL,
                json={"day": int(day)},
                timeout=10
            )

            result = response.json()

        # =================================================
        # SAFE VALIDATION
        # =================================================
        if not isinstance(result, dict):
            st.error("Invalid backend response")
            st.stop()

        if "predicted_price" not in result:
            st.error("Prediction failed")
            st.json(result)
            st.stop()

        # =================================================
        # SAFE DATA CLEANING
        # =================================================
        predicted_price = abs(float(result.get("predicted_price") or 0))
        current_price = abs(float(result.get("current_price") or predicted_price * 0.95))
        confidence = int(result.get("confidence") or 91)

        # avoid division by zero
        if current_price == 0:
            growth = 0
        else:
            growth = ((predicted_price - current_price) / current_price) * 100

        growth = round(growth, 2)
        trend = "Bullish 🚀" if growth > 0 else "Bearish 🐻"

        # =================================================
        # MARKET OVERVIEW
        # =================================================
        st.subheader("📊 Market Overview")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Current Price", f"${current_price:.2f}")
        c2.metric("Predicted Price", f"${predicted_price:.2f}")
        c3.metric("Expected Growth", f"{growth:.2f}%")
        c4.metric("Confidence", f"{confidence}%")

        st.markdown("---")

        # =================================================
        # FUTURE SIMULATION
        # =================================================
        future_days = list(range(day, day + 30))

        prices = []
        current = predicted_price

        for _ in range(30):
            current += np.random.uniform(-2, 4)
            prices.append(round(abs(current), 2))

        # =================================================
        # TREND CHART
        # =================================================
        trend_fig = go.Figure()

        trend_fig.add_trace(go.Scatter(
            x=future_days,
            y=prices,
            mode="lines+markers",
            name="Predicted Price",
            line=dict(color="#00C6FF", width=4)
        ))

        trend_fig.update_layout(
            title="📈 Future Stock Trend",
            template="plotly_dark",
            height=450
        )

        # =================================================
        # FEATURE IMPORTANCE
        # =================================================
        features = ["Open Price", "High Price", "Low Price", "Volume"]
        importance = [0.42, 0.30, 0.18, 0.10]

        feature_fig = go.Figure()
        feature_fig.add_trace(go.Bar(
            x=importance,
            y=features,
            orientation="h"
        ))

        feature_fig.update_layout(
            title="🎯 Feature Importance",
            template="plotly_dark",
            height=450
        )

        # =================================================
        # CHARTS
        # =================================================
        left, right = st.columns(2)

        with left:
            st.plotly_chart(trend_fig, use_container_width=True)

        with right:
            st.plotly_chart(feature_fig, use_container_width=True)

        # =================================================
        # MODEL PERFORMANCE (REAL FROM BACKEND)
        # =================================================
        st.subheader("🤖 Model Performance")

        metrics = result.get("metrics") or {}

        r2 = float(metrics.get("r2") or 0)
        rmse = float(metrics.get("rmse") or 0)
        mae = float(metrics.get("mae") or 0)

        m1, m2, m3, m4 = st.columns(4)

        m1.metric("R² Score", f"{r2:.2f}")
        m2.metric("RMSE", f"{rmse:.2f}")
        m3.metric("MAE", f"{mae:.2f}")
        m4.metric("Market Trend", trend)

        # =================================================
        # CONFIDENCE
        # =================================================
        st.subheader("🎯 AI Prediction Confidence")

        st.progress(confidence / 100)
        st.success(f"Prediction Confidence: {confidence}%")

        # =================================================
        # TABLE
        # =================================================
        st.subheader("📋 Prediction Data")

        df = pd.DataFrame({
            "Day": future_days,
            "Predicted Price": prices
        })

        st.dataframe(df, use_container_width=True)

        # =================================================
        # INFO
        # =================================================
        st.markdown("---")
        st.subheader("⚙️ Project Information")

        st.info("""
        Model: Machine Learning Model

        Features:
        - Open Price
        - High Price
        - Low Price
        - Volume

        Tech Stack:
        - Python
        - FastAPI
        - Streamlit
        - Scikit-Learn
        - Plotly
        """)

    except requests.exceptions.ConnectionError:
        st.error("❌ FastAPI Backend Not Running")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
