import streamlit as st
import requests

# Title of the app
st.title("🌤️ Real-Time Weather App (Weatherstack API)")

# User input: city name
city = st.text_input("Enter city name:")

# Your Weatherstack API key
api_key = "a4e89c9f9eb30c8ecd11c546fdfe18f3"

# Run when button is clicked
if st.button("Get Weather"):
    if city:
        # Build the request URL
        url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
        
        # Send GET request
        response = requests.get(url)
        data = response.json()

        # Check if the response contains valid data
        if "current" in data:
            current = data["current"]
            location = data["location"]["name"]
            country = data["location"]["country"]
            st.subheader(f"🌍 Weather in {location}, {country}")
            st.write(f"**Temperature:** {current['temperature']}°C")
            st.write(f"**Weather Description:** {current['weather_descriptions'][0]}")
            st.write(f"**Humidity:** {current['humidity']}%")
            st.write(f"**Wind Speed:** {current['wind_speed']} km/h")
        else:
            st.error("City not found or API error.")
    else:
        st.warning("Please enter a city name.")
