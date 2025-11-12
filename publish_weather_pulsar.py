import json
import pulsar

# 1. Connect to Pulsar broker
client = pulsar.Client('pulsar://localhost:6650')

# 2. Create a producer for a topic
producer = client.create_producer('weather-topic')

# 3. Read transformed JSON data
with open('weather_transformed.json', 'r') as file:
    data = json.load(file)

# 4. Publish each record as a message
for record in data:
    message = json.dumps(record)
    producer.send(message.encode('utf-8'))
    print(f"Sent: {message}")

# 5. Close connection
producer.close()
client.close()

print("✅ All weather data published to Pulsar topic 'weather-topic'")

