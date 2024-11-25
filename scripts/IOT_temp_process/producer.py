# from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

# producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def producer_main():
    print('Main method call : ')
    generate_sensor_data()

def get_values(sensor_id):
    temperature = random.uniform(18.0, 35.0)  
    humidity = random.uniform(30.0, 80.0)     
    aqi = random.randint(30, 150)             
    timestamp = datetime.utcnow().isoformat()
    
    return {
        "sensor_id": sensor_id,
        "timestamp": timestamp,
        "temperature": temperature,
        "humidity": humidity,
        "aqi": aqi
    }

def generate_sensor_data(): 

    while True:
        sensor_data = get_values("S1")
        # producer.send('iot-sensor-data', value=sensor_data)  
        print(f"Sent data: {sensor_data}")
        time.sleep(0.15) 

