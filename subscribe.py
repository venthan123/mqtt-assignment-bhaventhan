import paho.mqtt.client as mqtt

student_name = "BHAVENTHAN R"
unique_id = "42130081"
topic = "home/bhaventhanr-2025/sensor"

def on_message(client, userdata, msg):
    print(f"{msg.topic} → {msg.payload.decode()}")

client = mqtt.Client(client_id="subscriber_42130081", protocol=mqtt.MQTTv311)
client.connect("broker.hivemq.com", 1883, 60)

client.subscribe(topic)
client.on_message = on_message

client.loop_forever()

