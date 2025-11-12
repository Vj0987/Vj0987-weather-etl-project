import requests
import json
import pulsar
import time
from datetime import datetime

# Pulsar producer setup
client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('weather-topic')

# Coordinates for multiple cities
cities = {
    "Nagpur": (21.1458, 79.0882),
    "Mumbai": (19.0760, 72.8777),
    "Delhi":  (28.6139, 77.2090)
}

while True:
    for city, (lat, lon) in cities.items():
        # Fetch live weather
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        r = requests.get(url)
        data = r.json()

        weather = data["current_weather"]
        record = {
            "city": city,
            "temperature": weather["temperature"],
            "humidity": 70,          # Open-Meteo doesn’t always give humidity
            "pressure": 1013,
            "wind_speed": weather["windspeed"],
            "date": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "temperature_f": weather["temperature"] * 9/5 + 32,
            "day_of_week": datetime.utcnow().strftime("%A")
        }

        producer.send(json.dumps(record).encode('utf-8'))
        print(f"Sent to Pulsar → {record}")

    # Sleep 5 minutes
    time.sleep(300)

client.close()
