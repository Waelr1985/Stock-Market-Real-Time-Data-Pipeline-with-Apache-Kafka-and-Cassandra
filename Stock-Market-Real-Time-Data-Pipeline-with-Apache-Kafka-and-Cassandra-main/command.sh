# Download and extract Apache Kafka
wget https://downloads.apache.org/kafka/3.3.2/kafka_2.12-3.3.2.tgz
tar -xvf kafka_2.12-3.3.2.tgz
cd kafka_2.12-3.3.2

# Install Java (Kafka 3.3.2 requires Java 11+)
sudo yum install java-11-openjdk -y
java -version

# Configure Kafka to use EC2 Public IP
nano config/server.properties
# listeners=PLAINTEXT://0.0.0.0:9092
# advertised.listeners=PLAINTEXT://<EC2_PUBLIC_IP>:9092

# Start ZooKeeper (run in background)
nohup bin/zookeeper-server-start.sh config/zookeeper.properties > zookeeper.log 2>&1 &

# Start Kafka broker (run in background)
nohup bin/kafka-server-start.sh config/server.properties > kafka.log 2>&1 &

# Create a topic
bin/kafka-topics.sh --create --topic demo_test \
--bootstrap-server localhost:9092 \
--replication-factor 1 --partitions 1

# Start a Kafka producer (new terminal)
bin/kafka-console-producer.sh --topic demo_test --bootstrap-server localhost:9092

# Start a Kafka consumer (new terminal)
bin/kafka-console-consumer.sh --topic demo_test --bootstrap-server localhost:9092
