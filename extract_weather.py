import requests
import json
from datetime import datetime

# 1. API Key from OpenWeatherMap
API_KEY = "27b81b557a41a9f1f24e2eb70a311c65"  # Replace with your API Key

# 2. List of cities to fetch
CITIES = ["London", "New York", "Mumbai"]

def fetch_weather(city):
    """
    Fetch weather for a single city using OpenWeatherMap API
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Create dictionary of required info
    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    weather_data = []
    for city in CITIES:
        weather_data.append(fetch_weather(city))
    
    # Save as JSON file
    with open("weather_raw.json", "w") as f:
        json.dump(weather_data, f, indent=4)

    print("Weather data extracted and saved to weather_raw.json")

if __name__ == "__main__":
    main()
