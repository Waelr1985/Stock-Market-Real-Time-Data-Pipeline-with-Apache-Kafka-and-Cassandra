from cassandra.cluster import Cluster
from kafka import KafkaConsumer
from json import loads, dumps
import uuid

try:
    # Connect to Kafka
    consumer = KafkaConsumer(
        'demo_test',
        bootstrap_servers=['192.168.1.182:9092'],  # Replace with your broker IP
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
    print("✅ Connected to Kafka")
except Exception as e:
    print("❌ Kafka consumer error:", e)
    consumer = None

try:
    # Connect to Cassandra
    cluster = Cluster(['192.168.1.182'])  # Replace with your Cassandra node IP
    session = cluster.connect()
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS stockmarket 
        WITH replication = {'class':'SimpleStrategy', 'replication_factor':1};
    """)
    session.set_keyspace("stockmarket")

    session.execute('''
        CREATE TABLE IF NOT EXISTS stock_market_data (
            id UUID PRIMARY KEY,
            "index" text,
            date text,
            open float,
            high float,
            low float,
            close float,
            "adj close" float,
            volume bigint,
            closeUSD float
        );
    ''')
    print("✅ Cassandra keyspace and table ready")
except Exception as e:
    print("❌ Cassandra error:", e)
    session = None

if consumer and session:
    for message in consumer:
        if message.value:
            try:
                new_data = {'id': str(uuid.uuid4())}  # unique ID
                new_data.update(message.value)
                final_data = dumps(new_data)

                query = f"INSERT INTO stock_market_data JSON '{final_data}';"
                session.execute(query)

                print("✅ Inserted:", new_data)
            except Exception as e:
                print("❌ Insert error:", e)
