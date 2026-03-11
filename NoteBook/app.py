import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st
from sklearn.ensemble import RandomForestRegressor

# Load trained models
lr_model = pk.load(open('model.pkl','rb'))        # Linear Regression
rf_model = pk.load(open('rf_model.pkl','rb'))    # Random Forest

st.title('🚗 Car Price Prediction Model')

# Load dataset
cars_data = pd.read_csv('Cardetails.csv')

# Extract brand name
def brandname(car_name):
    return car_name.split(' ')[0]

cars_data['name'] = cars_data['name'].apply(brandname)

# Streamlit input widgets
name = st.sidebar.selectbox('Car Brand', cars_data['name'].unique())
year = st.sidebar.slider('Year of Manufacture', 1994, 2024)
km_driven = st.sidebar.slider('KM Driven', 10, 2000000)
fuel = st.sidebar.selectbox('Fuel Type', cars_data['fuel'].unique())
seller_type = st.sidebar.selectbox('Seller Type', cars_data['seller_type'].unique())
transmission = st.sidebar.selectbox('Transmission', cars_data['transmission'].unique())
owner = st.sidebar.selectbox('Owner Type', cars_data['owner'].unique())
mileage = st.sidebar.slider('Mileage (kmpl)', 10.0, 40.0)
engine = st.sidebar.slider('Engine Capacity (CC)', 700, 5000)
max_power = st.sidebar.slider('Max Power (bhp)', 11.0, 200.0)
seats = st.sidebar.slider('Seats', 1, 10)

# Add some vertical space at the bottom of sidebar
st.sidebar.write("\n" * 5)

# Predict button
predict_button = st.sidebar.button("Predict")

if predict_button:
    # Mapping categorical inputs to numeric codes
    name_code = {brand: i for i, brand in enumerate(cars_data['name'].unique(), 1)}[name]
    fuel_code = {fuel: i for i, fuel in enumerate(cars_data['fuel'].unique(), 1)}[fuel]
    seller_code = {seller: i for i, seller in enumerate(cars_data['seller_type'].unique(), 1)}[seller_type]
    transmission_code = {t: i for i, t in enumerate(cars_data['transmission'].unique(), 1)}[transmission]
    owner_code = {o: i for i, o in enumerate(cars_data['owner'].unique(), 1)}[owner]

    # Prepare input
    user_input = [[
        name_code, year, km_driven, fuel_code, seller_code,
        transmission_code, owner_code, mileage, engine, max_power, seats
    ]]

    # Predict prices
    lr_price = lr_model.predict(user_input)[0]
    rf_price = rf_model.predict(user_input)[0]

    # --- Summary Table (Vertical) ---
    summary_dict = {
        "Feature": [
            "Car Brand", "Year", "KM Driven", "Fuel Type", "Seller Type",
            "Transmission", "Owner Type", "Mileage (kmpl)", "Engine (CC)",
            "Max Power (bhp)", "Seats"
        ],
        "Value": [
            name, year, km_driven, fuel, seller_type,
            transmission, owner, mileage, engine, max_power, seats
        ]
    }

    summary_df = pd.DataFrame(summary_dict)
    summary_df = summary_df.set_index('Feature')

    # Apply gradient only to numeric columns
    def highlight_numeric(s):
        if pd.api.types.is_numeric_dtype(s):
            return ['background: linear-gradient(90deg, #e0f7fa 0%, #00acc1 100%)']*len(s)
        else:
            return ['']*len(s)

    summary_styled = summary_df.style.apply(highlight_numeric, axis=0)\
        .set_table_styles([
            {'selector': 'tr:hover',
             'props': [('background-color', '#f2f2f2')]},
            {'selector': 'th',
             'props': [('background-color', '#4CAF50'), ('color', 'white')]}
        ])

    st.dataframe(summary_styled, height=400)

    # --- Prediction Table ---
    price_df = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "Predicted Price": [lr_price, rf_price]  # numeric only
})

# Format prices with ₹
    price_df["Predicted Price"] = price_df["Predicted Price"].apply(lambda x: f"₹{x:,.2f}")

# Set index to Model
    price_df = price_df.set_index("Model")

    st.subheader("💰 Predicted Prices")
    st.table(price_df)  # Use st.table instead of st.dataframe

