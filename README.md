# Build Hadoop distributed data storage system for Binance Trading Market Data using Binance API, Spark, Hive, Superset and Airflow. Deploy on docker. 
## Version
 - Hadoop: 3.3.6
 - Hive: 3.1.3

## Quick Start

To deploy the cluster, run:
```
make
docker compose up
```
To shut down the cluster, run:
```
docker compose down -v
```

## Access interfaces with the following URL

### Hadoop
NameNode: http://localhost:9871

### Airflow
Web UI: http://localhost:8081

### Hive 
URI: jdbc:hive2://172.20.1.2:10000

### Superset
Web UI: http://localhost:8089
