"""
weather_engine.py
Fetches current weather data for a city using OpenWeather API.
"""

import requests

# Get a free API key from https://openweathermap.org/api
API_KEY = "dc64448db46081fe2c5fa3ea0c0e3270"


def get_weather(city: str):
    """
    Fetches current weather for a given city.
    Returns a dict with temperature, condition, and humidity.
    If the API call fails, returns None.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city},IN",
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        return {
            "city": data.get("name"),
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "condition": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }
    except Exception as e:
        print(f"Weather API error: {e}")
        return None
