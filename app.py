import streamlit as st
import requests

st.set_page_config(page_title="Weather App", page_icon="🌦️")
st.title("🌦️ Real-Time Weather Fetcher")

# User input
city = st.text_input("Enter city name", "Hyderabad")

# Add your OpenWeatherMap API key here
api_key = "b309fbbc5e66e0b67f60f6acda3d7c24"  # Replace with your actual API key

if st.button("Get Weather"):
    if not api_key or api_key == "b309fbbc5e66e0b67f60f6acda3d7c24":
        st.error("Please add your OpenWeatherMap API key in the script.")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            st.subheader(f"Weather in {city.title()}")
            st.write(f"**Temperature:** {temp}°C")
            st.write(f"**Condition:** {weather}")
            st.write(f"**Humidity:** {humidity}%")
            st.write(f"**Wind Speed:** {wind_speed} m/s")
        else:
            st.error("City not found or API error.")
