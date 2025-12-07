MQTT Home Assistant Assignment
Student: BHAVENTHAN R
Register No: 42130081
## Overview

This project demonstrates MQTT communication using a Python publisher and subscriber, integrated with Home Assistant.
Three sensor values are published every second:

Temperature

Humidity

Vibration

Data is published as JSON to this topic:

home/bhaventhanr-2025/sensor

## Project Contents
publish.py      → Publishes temperature, humidity, vibration  
subscribe.py    → Receives MQTT JSON sensor data  
requirements.txt→ Python dependencies  
screenshots/    → Screenshots for assignment submission  

▶️ How to Run (Windows)
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run subscriber (Terminal 1)
python subscribe.py

3️⃣ Run publisher (Terminal 2)
python publish.py


Subscriber output example:

home/bhaventhanr-2025/sensor → {"temp":30.1,"hum":72.3,"vib":2.4}

🏠 Home Assistant

Three MQTT sensors were created in Home Assistant:

BHAVENTHAN Temperature

BHAVENTHAN Humidity

BHAVENTHAN Vibration

All values update in real-time on the dashboard.

🎥 Demo Video Includes

Face verification

Timestamp

Publisher running

Subscriber receiving

Home Assistant dashboard updates