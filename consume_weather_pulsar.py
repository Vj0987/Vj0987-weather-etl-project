import json
import pulsar
import mysql.connector

# 1️⃣ Connect to Pulsar
client = pulsar.Client('pulsar://localhost:6650')

# 2️⃣ Create consumer on same topic
consumer = client.subscribe('weather-topic', subscription_name='weather-sub', consumer_type=pulsar.ConsumerType.Shared)

# 3️⃣ Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",          # change if your MySQL username differs
    password="password",  # enter your MySQL password
    database="weather_db"
)
cursor = connection.cursor()
print("Connected to MySQL ✅")

# 4️⃣ Consume and insert into MySQL
try:
    while True:
        msg = consumer.receive(timeout_millis=5000)  # waits up to 5 s for message
        data = json.loads(msg.data().decode('utf-8'))

        sql = """
            INSERT INTO weather_data (city, temperature, humidity, pressure, wind_speed, date, temperature_f, day_of_week)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            data.get("city"),
            data.get("temperature"),
            data.get("humidity"),
            data.get("pressure"),
            data.get("wind_speed"),
            data.get("date"),
            data.get("temperature_f"),
            data.get("day_of_week")
        )

        cursor.execute(sql, values)
        connection.commit()
        print(f"Inserted into MySQL: {data}")
        consumer.acknowledge(msg)

except pulsar.Timeout:
    print("No more messages. Closing connection...")

finally:
    cursor.close()
    connection.close()
    consumer.close()
    client.close()
    print("✅ Consumer and database connections closed.")

