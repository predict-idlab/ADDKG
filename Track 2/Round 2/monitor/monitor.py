from kafka import KafkaConsumer, KafkaProducer
import json
import os
import pandas as pd

# Kafka broker configuration
bootstrap_servers = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
input_topic = 'result'

found_true_positive = set()
found_false_positive = set()
true_regions_frame = pd.read_csv('train_labels.csv')[['started_at','finished_at', 'fault_name']]

true_positives = 0
false_positives = 0
average_detection_time = 0

def calculate_score(graph_timestamp, false_pos_region_delta=300):
    global average_detection_time, true_positives, false_positives
    true_regions = true_regions_frame.values
    timestamp_found = False
    # Iterate over each true window
    for true_start, true_end, _ in true_regions:
        # Check if the predicted timestamp falls within the current true window
        if int(pd.Timestamp(true_start).timestamp()) <= graph_timestamp <= int(pd.Timestamp(true_end).timestamp()):
            # If it falls within the window and a true positive within the window was already found ,
            # just continue, this are predictions related and close to eachother
            if (true_start, true_end) in found_true_positive:
                timestamp_found = True
                break
            # If it falls within the window and a true positive within the window is not found yet,
            # count it as a true positive and set the flag to True
            true_positives += 1
            found_true_positive.add((true_start, true_end))
            timestamp_found=True
            break
    # If the predicted timestamp falls outside the window, count it as a false positive
    if not timestamp_found:
        # but check if a previous false positive was within the range of an already detected false positive
        in_region = False
        for region in found_false_positive:
            if region[0] <= graph_timestamp <= region[1]:
                #if so, we just neglect it
                in_region = True
                break
        if not in_region:
            # otherwise, we add it, together with its range
            false_positives += 1
            if false_pos_region_delta is not None:
                found_false_positive.add((graph_timestamp, graph_timestamp+false_pos_region_delta))

# Function to consume files from input topic, process them, and produce result to output topic
def process_files(consumer):
    global average_detection_time, true_positives, false_positives
    print("Ready, start listening:")
    for message in consumer:
        event_timestamp = message.timestamp
        data = json.loads(message.value.decode('utf-8'))
        if average_detection_time == 0:
            average_detection_time = event_timestamp-data['event_ts']
        else:
            average_detection_time = (average_detection_time+event_timestamp-data['event_ts'])/2
        
        calculate_score(data['graph_ts'])
        
        print(true_positives, false_positives, average_detection_time)


if __name__ == '__main__':
    consumer = KafkaConsumer(input_topic, bootstrap_servers=bootstrap_servers)
    process_files(consumer)