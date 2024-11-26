from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

KAFKA_BROKER = 'localhost:9092'  
KAFKA_TOPIC = 'test1' 

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def producer_main(currLoc):
    print('Main method call : ')
    generate_sensor_data(currLoc)

def get_values(sensor_id,currloc):
    temperature = random.uniform(18.0, 35.0)  
    humidity = random.uniform(30.0, 80.0)     
    aqi = random.randint(30, 150)             
    timestamp = datetime.utcnow().isoformat()
    
    return {
        "sensor_id": sensor_id,
        "location" : currloc ,
        "timestamp": timestamp,
        "temperature": temperature,
        "humidity": humidity,
        "aqi": aqi
    }

def generate_sensor_data(currLoc): 

    while True:
        sensor_data = get_values("S1",currLoc)
        producer.send(KAFKA_TOPIC, value=sensor_data)  
        print(f"Sent data: {sensor_data}")
        time.sleep(0.15) 
    
    # producer.flush()
    # producer.close()

