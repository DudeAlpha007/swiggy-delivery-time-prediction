import streamlit as st
import pandas as pd
import pickle
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Swiggy ETA Predictor", layout="wide")

# ---------------- IMAGE ----------------
st.image("Swiggy ETA Predictor.png", use_container_width=True)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

.section {
    padding: 20px;
    border-radius: 15px;
    background: #111827;
    margin-bottom: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}

h1 {
    text-align: center;
    color: #fc8019;
}

.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 25px;
}

.stButton>button {
    background-color: #fc8019;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    height: 50px;
    width: 100%;
}

.result-box {
    background: linear-gradient(135deg,#fc8019,#ff9f43);
    padding:40px;
    border-radius:20px;
    text-align:center;
    color:white;
}

.result-title {
    font-size:18px;
    opacity:0.8;
}

.result-value {
    font-size:42px;
    font-weight:bold;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1>🍔 Swiggy ETA Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>AI-powered Delivery Time Prediction System</p>", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
with open("Swiggy Delivery Time Prediction Project.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------- MAIN SECTIONS ----------------
col1, col2, col3 = st.columns(3)

# -------- ORDER DETAILS --------
with col1:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("🍽️ Order Details")

    type_of_order = st.selectbox("Type of Order", ["snack","meal","drinks","buffet"])
    distance = st.slider("Distance (km)", 0.1, 30.0, 5.0)
    multiple_deliveries = st.selectbox("Multiple Deliveries", [0,1,2,3])
    festival = st.selectbox("Festival", ["no","yes"])
    city_name = st.text_input("City Name", "Hyderabad")

    st.markdown('</div>', unsafe_allow_html=True)

# -------- DELIVERY CONDITIONS --------
with col2:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("🚦 Delivery Conditions")

    weather = st.selectbox("Weather", ["sunny","stormy","cloudy","fog","windy"])
    traffic = st.selectbox("Traffic", ["low","medium","high","jam"])
    city_type = st.selectbox("City Type", ["urban","semi-urban","metropolitian"])
    order_day = st.slider("Day", 1, 31, 15)
    order_month = st.slider("Month", 1, 12, 6)
    order_day_of_week = st.selectbox("Day of Week",
        ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"])

    weekend_label = st.selectbox("Weekend", ["No", "Yes"])
    is_weekend = {"No": 0, "Yes": 1}[weekend_label]

    st.markdown('</div>', unsafe_allow_html=True)

# -------- RIDER INFO --------
with col3:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("🛵 Rider Info")

    age = st.slider("Rider Age", 18, 60, 25)
    ratings = st.slider("Rating", 1.0, 5.0, 4.2)

    vehicle_condition_label = st.selectbox(
        "Vehicle Condition",
        ["Poor", "Average", "Good", "Excellent"]
    )
    vehicle_condition = {
        "Poor": 0,
        "Average": 1,
        "Good": 2,
        "Excellent": 3
    }[vehicle_condition_label]

    type_of_vehicle = st.selectbox("Vehicle Type", ["motorcycle","scooter","electric_scooter","bicycle"])
    pickup_time_minutes = st.slider("Pickup Time (min)", 0, 60, 15)
    order_time_hour = st.slider("Order Hour", 0, 23, 12)
    order_time_of_day = st.selectbox("Time of Day", ["morning","afternoon","evening","night"])

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 Predict ETA"):
    
    input_data = pd.DataFrame({
        'age':[age],
        'ratings':[ratings],
        'weather':[weather],
        'traffic':[traffic],
        'vehicle_condition':[vehicle_condition],
        'type_of_order':[type_of_order],
        'type_of_vehicle':[type_of_vehicle],
        'multiple_deliveries':[multiple_deliveries],
        'festival':[festival],
        'city_type':[city_type],
        'distance':[distance],
        'order_day':[order_day],
        'order_month':[order_month],
        'is_weekend':[is_weekend],
        'order_time_hour':[order_time_hour],
        'pickup_time_minutes':[pickup_time_minutes],
        'order_day_of_week':[order_day_of_week],
        'order_time_of_day':[order_time_of_day],
        'city_name':[city_name]
    })

    with st.spinner("Calculating optimal delivery time..."):
        time.sleep(2)
        prediction = model.predict(input_data)[0]

    st.markdown("---")

    st.markdown(f"""
    <div class="result-box">
        <div class="result-title">Estimated Delivery Time</div>
        <div class="result-value">{prediction:.2f} Minutes</div>
    </div>
    """, unsafe_allow_html=True)