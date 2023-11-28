# from datetime import timedelta
# from time import sleep
from datetime import timedelta 
from airflow import DAG 
from airflow.operators.bash_operator import BashOperator 
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

target_time = 14
hour=target_time - 7 # 7 is the time zone of VietNam 

# define DAG arguments 
default_args={
    'owner': 'vanhuan',
    'start_date': days_ago(1),
    'email': ['huannguyen.09.pt@gmail.com'], 
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
    # 'is_paused_upon_creation': False,
}

# define the DAG 
dag=DAG(
    dag_id="Ingest_Extract_Transform_Load_Binance_Market_Data",
    default_args=default_args,
    description=" Auto Ingest Data from Binance into DataLake, ETL into Datawarehouse",
    schedule_interval=f"13 {hour} * * *",
)

# define the ingestion data from Binance task 
ingestion= BashOperator(
    task_id='ingestion', 
    bash_command="python3 /code/getdata.py", 
    dag=dag,
)

# define the etl task 
etl= BashOperator(
    task_id='etl',
    bash_command="python3 /code/ETL.py",
    dag=dag,
)


# define the start_hive_hiveserver2
build_report= BashOperator(
    task_id='build_report', 
    bash_command="python3 /code/build_report.py",
    dag=dag,
)

# task pipeline 
ingestion >> etl >> build_report