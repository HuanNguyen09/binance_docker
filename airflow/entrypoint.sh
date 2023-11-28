#!/bin/bash
# airflow db init
airflow db migrate
airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org \
    --password admin
airflow webserver --port 8080 &
airflow db upgrade
airflow dags unpause Ingest_Extract_Transform_Load_Binance_Market_Data
airflow scheduler &
# exec /bin/bash
tail -f /dev/null
