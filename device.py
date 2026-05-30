import random
import time
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:

    data = {
        "device_id": random.choice([
            "patient_1",
            "patient_2",
            "patient_3",
            "patient_4",
            "patient_5"
        ]),
        "heart_rate": random.randint(60, 120),
        "temperature": round(random.uniform(36.0, 39.5), 1),
        "spo2": random.randint(90, 100)
    }

    client.publish("health/sensors", json.dumps(data))

    print("Sent:", data)

    time.sleep(2)
