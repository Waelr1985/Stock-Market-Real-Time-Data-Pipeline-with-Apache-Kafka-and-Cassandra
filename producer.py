from kafka import KafkaProducer
from time import sleep
from json import dumps
import pandas as pd
import os

try:
    # Connect to Kafka
    producer = KafkaProducer(
        bootstrap_servers=['192.168.1.182:9092'],  # Replace with your Kafka broker IP
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )
    print("✅ Connected to Kafka")
except Exception as e:
    print("❌ Producer connection error:", e)
    producer = None

# Load dataset
df = None
if os.path.exists("stockData.csv"):
    try:
        df = pd.read_csv("stockData.csv")
        print(f"✅ Loaded stockData.csv with {len(df)} rows")
    except Exception as e:
        print("❌ Error reading stockData.csv:", e)

# Send messages
if producer and df is not None:
    try:
        for i in range(100):  # send 100 messages for testing
            sample_data = df.sample(1).to_dict(orient="records")[0]
            producer.send("demo_test", value=sample_data)
            print(f"📤 Sent: {sample_data}")
            sleep(0.5)  # wait half a second between messages
        producer.flush()
        print("✅ Finished sending messages")
    except Exception as e:
        print("❌ Error while sending data:", e)
