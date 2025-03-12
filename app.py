import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np

# Load your CSV file with station names and coordinates
df = pd.read_csv("data/EVChargingStationUsage.csv", low_memory=False)

# Extract the relevant columns
new_df = df[['Station Name', 'Latitude', 'Longitude']].drop_duplicates()

# Title of the app
st.title("EV Charging Demand Prediction")

# Introduction text
st.write("This tool allows you to select parameters and predict the demand for EV charging stations.")

# Form to collect user inputs
with st.form("ev_charging_form"):
    # Station Name selection
    station_name = st.selectbox("Select Station Name", new_df['Station Name'].tolist())
    
    # Get latitude and longitude for the selected station name
    station_data = new_df[new_df['Station Name'] == station_name].iloc[0]
    latitude = station_data['Latitude']
    longitude = station_data['Longitude']
    
    # Display the latitude and longitude based on station selection
    st.write(f"Selected Station Latitude: {latitude}, Longitude: {longitude}")
    
    start_date = st.date_input("Start Date", value=datetime(2011, 7, 29))
    end_date = st.date_input("End Date", value=datetime(2020, 12, 31))

    # Manual entry inputs
    gasoline_savings = st.number_input("Gasoline Savings (gallons)", min_value=0.0, max_value=10.0, step=0.1)
    fee = st.number_input("Fee (USD)", min_value=0.0, step=0.01)

    # Latitude and Longitude will now be auto-filled based on the station name
    # You can still allow the user to modify if needed
    st.write("### Latitude and Longitude (auto-filled from selected station):")
    st.write(f"Latitude: {latitude}, Longitude: {longitude}")

    # Other inputs
    port_number = st.selectbox("Port Number", [1, 2])
    ended_by_customer = st.selectbox("Ended By Customer", [True, False])
    ended_by_door = st.selectbox("Ended By Door", [True, False])
    start_hour = st.selectbox("Start Hour", list(range(24)))
    start_dayofweek = st.selectbox("Start Day of Week", [0, 1, 2, 3, 4, 5, 6])
    start_month = st.selectbox("Start Month", list(range(1, 13)))
    start_year = st.selectbox("Start Year", list(range(2011, 2021)))

    # Submit button
    submit_button = st.form_submit_button("Predict")

if submit_button:
    # Collecting data for prediction
    data = {
        'Station Name': station_name,
        'Start Date': start_date,
        'End Date': end_date,
        'Gasoline Savings (gallons)': gasoline_savings,
        'Fee (USD)': fee,
        'Latitude': latitude,
        'Longitude': longitude,
        'Port Number': port_number,
        'Ended By Customer': ended_by_customer,
        'Ended By Door': ended_by_door,
        'Start Hour': start_hour,
        'Start Day of Week': start_dayofweek,
        'Start Month': start_month,
        'Start Year': start_year
    }

    # Display the collected data
    st.write("### Collected Data")
    st.write(data)

    # Predicting using a pre-trained model (assuming you have a model saved, such as a .pkl file)
    # For the sake of this example, let's assume we use a simple linear regression model.
    
    # Importing a dummy model (you can replace this with your actual trained model)
    # For example:
    # from sklearn.externals import joblib
    # model = joblib.load("your_trained_model.pkl")
    
    # Simulate prediction (replace this with actual model prediction)
    prediction = np.random.rand() * 100  # Random prediction value
    
    st.write("### Prediction Result")
    st.write(f"Predicted EV Charging Demand: {prediction:.2f} kWh")
