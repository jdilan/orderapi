from confluent_kafka import Producer #, Consumer
from django.conf import settings

# Initialize Kafka Producer
producer = Producer({'bootstrap.servers': settings.KAFKA_CONFIG['bootstrap.servers']})

def delivery_report(err, msg):
    """Callback function for Kafka Producer to check delivery status."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def send_data(topic, data_json):
    """Function to send data to Kafka."""
    producer.produce(topic, data_json, callback=delivery_report)
    producer.flush()  # Ensure all messages are sent