import time
import random
import json
import paho.mqtt.client as mqtt

student_name = "BHAVENTHAN R"
unique_id = "42130081"
topic = "home/bhaventhanr-2025/sensor"

client = mqtt.Client(client_id="publisher_42130081", protocol=mqtt.MQTTv311)
client.connect("broker.hivemq.com", 1883, 60)

while True:
    temp = round(random.uniform(26, 34), 2)
    hum = round(random.uniform(60, 90), 2)
    vib = round(random.uniform(0.5, 5.0), 2)

    payload = {
        "student": student_name,
        "regno": unique_id,
        "temperature": temp,
        "humidity": hum,
        "vibration": vib
    }

    client.publish(topic, json.dumps(payload))
print(time.strftime("%Y-%m-%d %H:%M:%S"), f"Published → Temp:{temp}, Hum:{hum}, Vib:{vib}")

       time.sleep(1)
