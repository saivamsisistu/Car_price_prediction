import streamlit as st
import pandas as pd
import numpy as np
import pickle
with open('LinearRegressionModel.pkl','rb') as f:
    model=pickle.load(f)

car=pd.read_csv("cleaned_car.csv")

# Title and header for the application
st.title("🚗 Car Price Prediction")
st.header("Predict the Resale Price of Your Car")

# Collecting user inputs with enhanced layout
st.subheader("Select Car Details")

# Adding car company selection with icons
company = st.selectbox(
    "Select the Car Company",
    options=car['company'].unique().tolist(),
)

# Adding car model selection based on example options

name = st.selectbox(
    "Select the Car Model",
    options=car[car['company']==company]['name'].unique().tolist(),  # Replace with real car models as needed
)

# Year of purchase
year = st.slider(
    "Select Year of Purchase",
    min_value=1995, max_value=2019, step=1,
)

# Fuel type with enhanced display
fuel = st.radio(
    "Select Fuel Type",
    options=['Petrol', 'Diesel', 'LPG'],
    horizontal=True,
)

# Kilometers driven
km = st.number_input(
    "Enter Kilometers Driven",
    min_value=0, max_value=500000, step=1000,
)

# Displaying a prediction button
if st.button("Predict Price"):
    # Placeholder for prediction logic
    prediction=model.predict(pd.DataFrame([[name,company,year,km,fuel]],columns=['name','company','year','kms_driven','fuel_type']))
    st.markdown(f"<h2 style='text-align: center; color: green;'>Estimated Price: ₹{prediction}</h2>", unsafe_allow_html=True)
