import pandas as pd
import mysql.connector
from mysql.connector import Error

# 1. Load transformed CSV
df = pd.read_csv("weather_transformed.csv")

# 2. Standardize column names (just to be safe)
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# 3. Connect to MySQL
try:
    connection = mysql.connector.connect(
        host='localhost',          # your MySQL host
        user='root',               # your MySQL username
        password='password',  # your MySQL password
        database='weather_db'      # your MySQL database name
    )

    if connection.is_connected():
        print("Connected to MySQL")
        cursor = connection.cursor()

        # 4. Create table if not exists
        create_table_query = """
        CREATE TABLE IF NOT EXISTS weather (
            id INT AUTO_INCREMENT PRIMARY KEY,
            city VARCHAR(100),
            temperature FLOAT,
            humidity INT,
            pressure INT,
            wind_speed FLOAT,
            date_time DATETIME,
            temperature_f FLOAT,
            day_of_week VARCHAR(20)
        );
        """
        cursor.execute(create_table_query)
        connection.commit()

        # 5. Insert rows
        insert_query = """
        INSERT INTO weather 
        (city, temperature, humidity, pressure, wind_speed, date_time, temperature_f, day_of_week)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        for _, row in df.iterrows():
            values = (
                row["city"],
                row["temperature"],
                row["humidity"],
                row["pressure"],
                row["wind_speed"],
                row["date"],          # corrected column name
                row["temperature_f"],
                row["day_of_week"]
            )
            cursor.execute(insert_query, values)

        connection.commit()
        print("Data inserted successfully!")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
