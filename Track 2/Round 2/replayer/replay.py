import time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from glob import glob
import json
import os

# Kafka broker configuration
bootstrap_servers = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
topic = 'kg'

# Function to read files and publish their content to Kafka topic
def publish_files(producer):
    file_list = sorted(sorted(glob('data/*/*/*.ttl')))
    for file_name in file_list:
        timestamp = int(file_name.split('/')[-1].split('.')[0])
        with open(file_name, 'r') as file:
            content = file.read()
            data = {'timestamp': timestamp, 'content': content}
            producer.send(topic, value=json.dumps(data).encode('utf-8'))
            producer.flush()
            print(f"Published file {file_name} to Kafka topic")
            time.sleep(15)  # 15-second interval between replays

if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    publish_files(producer)
