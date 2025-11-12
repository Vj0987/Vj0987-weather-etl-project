import pandas as pd

# 1. Load raw JSON data
df = pd.read_json("weather_raw.json")

# 2. Standardize column names
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# 3. Convert data types
df["temperature"] = df["temperature"].astype(float)
df["humidity"] = df["humidity"].astype(int)
df["pressure"] = df["pressure"].astype(int)
df["wind_speed"] = df["wind_speed"].astype(float)
df["date"] = pd.to_datetime(df["date"])  # Updated from date_time to date

# 4. Add derived columns
df["temperature_f"] = df["temperature"] * 9/5 + 32          # Celsius to Fahrenheit
df["day_of_week"] = df["date"].dt.day_name()                # Day of the week
df["month"] = df["date"].dt.month                            # Month
df["year"] = df["date"].dt.year                              # Year

# 5. Handle missing data (for numeric columns or city)
df["city"] = df["city"].fillna("Unknown")
numeric_cols = ["temperature", "humidity", "pressure", "wind_speed"]
df[numeric_cols] = df[numeric_cols].fillna(0)

# 6. Save transformed data to CSV and JSON
df.to_csv("weather_transformed.csv", index=False)
df.to_json("weather_transformed.json", orient="records", indent=4)

print("Weather data transformed and saved to weather_transformed.json and CSV")
