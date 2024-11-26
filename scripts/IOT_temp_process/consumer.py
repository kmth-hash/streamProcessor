from kafka import KafkaConsumer 
import csv 
import os 
import json 
import sys 


KAFKA_BROKER = 'localhost:9092'  
KAFKA_TOPIC = 'test1' 

consumer = KafkaConsumer(KAFKA_TOPIC, 
                         bootstrap_servers=KAFKA_BROKER, 
                        #  auto_offset_reset='earliest',  
                         enable_auto_commit=True,
                         value_deserializer=lambda x: x.decode('utf-8')
                         ) 


def store_into_csv(filename , data) : 

    temp = [data[key] for key in ['sensor_id', 'location', 'timestamp', 'temperature', 'humidity', 'aqi']]
    
    script_path = os.path.abspath(__file__)

    script_directory = os.path.dirname(script_path)

    file_path = f'{script_directory}/{filename}'

    file_exists = os.path.exists(file_path)

    with open(file_path , mode='a' , newline='') as f : 
        writer = csv.writer(f) 
        if not file_exists : 
            writer.writerow(['sensor_id', 'location', 'timestamp', 'temperature', 'humidity', 'aqi'])
        
        writer.writerow(temp)
    print(f' Data loaded into {filename}: ',temp)

def process_data(message) : 
    # message = json.loads(message)

    filename = message.get('location') + '.csv'

    store_into_csv(filename , message) 



if __name__ == "__main__" : 
    for message in consumer : 
        data = message.value
        process_data(json.loads(data))
