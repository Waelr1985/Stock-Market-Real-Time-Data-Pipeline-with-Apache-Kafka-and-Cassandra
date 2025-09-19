# 📈 Stock Market Real-Time Data Pipeline with Apache Kafka & Cassandra  

This project implements a **real-time stock market data pipeline**, streaming live market data using Python and Apache Kafka, and storing it in a **Cassandra time-series database**. The pipeline is deployed on **AWS EC2** for Kafka brokers and connected to a local Cassandra cluster for persistence.  

The goal is to demonstrate how **financial data engineering pipelines** can be built to support real-time analytics, trading strategies, and AI/ML models.  

---

## 🚀 Key Features  

- **Streaming Data Ingestion** → Fetches real-time stock data via API and streams it into Kafka topics.  
- **Scalable Data Pipeline** → Uses Apache Kafka for distributed, fault-tolerant event streaming.  
- **NoSQL Storage** → Persists data in Cassandra, optimized for time-series queries.  
- **Cloud Deployment** → Kafka broker hosted on AWS EC2.  
- **Error Handling** → Built-in error logging and recovery mechanisms.  
- **Extensibility** → Future-ready for data visualization, ML-driven predictions, and real-time alerts.  

---

## 🛠️ Tech Stack  

- **Languages**: Python (with `kafka-python`, `cassandra-driver`)  
- **Streaming**: Apache Kafka  
- **Database**: CassandraDB  
- **Cloud**: AWS EC2, AWS CLI  
- **System**: Ubuntu 22.04 (local), Amazon Linux 2 (EC2)  
- **Other Tools**: Java (Kafka runtime), Git  

---

## 📐 Architecture  

![Pipeline Architecture](https://imgur.com/1DBe05W.png)  

1. Python script fetches **real-time stock data**.  
2. Data is published to a **Kafka topic**.  
3. Kafka consumer subscribes and writes data into **CassandraDB**.  
4. Data becomes queryable for **analysis / ML pipelines**.  

---

## ⚙️ Environment Setup  

### Local Machine  
```bash
Ubuntu 22.04.1 LTS  
4 vCPU, 4 GiB RAM, 32 GiB Storage  
```

### AWS EC2  
```bash
Amazon Linux 2 (Kernel 5.10)  
t2.micro – 1 vCPU, 1 GiB RAM  
```

### Prerequisites  

- Python 3.x  
- Apache Kafka  
- Cassandra  
- Java Runtime (for Kafka)  
- AWS CLI configured  

Install Python packages:  

```bash
pip install kafka-python cassandra-driver
```

---

## 🔧 Project Implementation  

1. **Provision EC2** instance and set up Apache Kafka.  
2. **Create Python producer** → fetch real-time stock market data.  
3. **Publish messages** → send data to Kafka topic.  
4. **Create Python consumer** → subscribe to topic and write data into Cassandra.  
5. **Query stored data** with CQL (Cassandra Query Language).  

---

## ▶️ Execution Steps  

1. Launch EC2 and start Kafka broker.  
2. Run producer script to publish real-time stock data.  
3. Run consumer script to consume and write data to Cassandra.  
4. Verify storage with Cassandra `cqlsh` queries.  

---

## 🐞 Error Handling & Troubleshooting  

- **Kafka Connection Error** → Check EC2 instance, Kafka service, and security group (ports 9092/2181).  
- **Cassandra Connection Error** → Ensure Cassandra is running; verify firewall rules.  
- **Data Retrieval Errors** → Validate API credentials and connectivity.  
- **Data Storage Issues** → Confirm Cassandra tables exist and schema matches data.  
- **Query Errors** → Use correct CQL syntax (`SELECT * FROM stocks;`).  

---

## 🔮 Future Enhancements  

- Add **data visualization dashboards** (Grafana, Plotly, or Matplotlib).  
- Integrate **PySpark** for large-scale processing.  
- Implement **Airflow DAGs** for automated workflows.  
- Build **ML models** for stock price prediction / anomaly detection.  
- Develop **real-time alerts** (Slack/Email) for market signals.  
- Deploy Cassandra cluster on **AWS (EKS/EC2) for scaling**.  

---

## ✅ Conclusion  

This project demonstrates how to build a **real-time financial data engineering pipeline** using Python, Apache Kafka, and Cassandra. While currently focused on stock market equities, the architecture is **adaptable to any real-time data stream** (IoT, crypto, financial tick data, etc.).  

 
