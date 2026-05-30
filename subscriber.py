import json
import paho.mqtt.client as mqtt
from db import Session, HealthData

session = Session()

def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe("health/sensors")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Received:", data)

    if data["heart_rate"] > 100:
        print("ALERT: High heart rate!")

    if data["temperature"] > 38.0:
        print("ALERT: High body temperature!")

    if data["spo2"] < 95:
        print("ALERT: Low oxygen level!")

    record = HealthData(
        device_id=data["device_id"],
        heart_rate=data["heart_rate"],
        temperature=data["temperature"],
        spo2=data["spo2"]
    )

    session.add(record)
    session.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
