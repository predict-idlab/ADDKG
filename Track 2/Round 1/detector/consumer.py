from kafka import KafkaConsumer, KafkaProducer
from anomaly_detector import determine_anomaly
import os
import json

# Kafka broker configuration
bootstrap_servers = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
input_topic = 'kg'
output_topic = 'result'

# Function to consume files from input topic, process them, and produce result to output topic
def process_files(consumer, producer):
    print("Ready, start listening:")
    for message in consumer:
        event_timestamp = message.timestamp
        data = json.loads(message.value.decode('utf-8'))
        anomaly, graph_timestamp = determine_anomaly(data['timestamp'], data['content'])
        if anomaly:
            anomaly_message = {'event_ts':event_timestamp, 'graph_ts':graph_timestamp}
            producer.send(output_topic, value=json.dumps(anomaly_message).encode('utf-8'))
            producer.flush()


if __name__ == '__main__':
    consumer = KafkaConsumer(input_topic, bootstrap_servers=bootstrap_servers)
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    process_files(consumer, producer)