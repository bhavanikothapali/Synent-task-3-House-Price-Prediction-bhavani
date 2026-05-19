import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.title("🏠 House Price Prediction App")

st.write("Enter house details to predict price")

# Inputs
longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.number_input("Housing Median Age", value=20)
total_rooms = st.number_input("Total Rooms", value=1000)
total_bedrooms = st.number_input("Total Bedrooms", value=200)
population = st.number_input("Population", value=500)
households = st.number_input("Households", value=150)
median_income = st.number_input("Median Income", value=3.5)

# Prediction button
if st.button("Predict House Price"):

    features = np.array([[longitude, latitude, housing_median_age,
                          total_rooms, total_bedrooms,
                          population, households, median_income]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")
