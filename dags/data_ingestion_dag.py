from datetime import datetime #type: ignore
from airflow import DAG #type: ignore
from airflow.operators.bash import BashOperator #type: ignore
from airflow.operators.python import PythonOperator #type: ignore
import pandas as pd #type: ignore
from sqlalchemy import create_engine #type: ignore
import os 

URL_PREFIX = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
URL_TEMPLATE = URL_PREFIX + 'yellow_tripdata_{{ execution_date.strftime("%Y-%m") }}.csv.gz'
OUTPUT_DIR = '/opt/airflow/data'
OUTPUT_FILE_TEMPLATE = OUTPUT_DIR + '/output_{{ execution_date.strftime("%Y-%m") }}.csv.gz'
TABLE_NAME = 'yellow_taxi_data'

def ensure_data_dir_exists():
    """Ensures /opt/airflow/data exists inside the container."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def ingest_to_postgres(file_path):
    """Reads CSV and loads it into Postgres."""
    engine = create_engine('postgresql://airflow:airflow@postgres:5432/ny_taxi')
    df = pd.read_csv(file_path, compression='gzip')
    df.to_sql(TABLE_NAME, con=engine, if_exists='append', index=False)

with DAG(
    dag_id="data_ingestion_local",
    schedule_interval="@monthly",
    start_date=datetime(2021, 1, 1),
    end_date=datetime(2021, 3, 1),
    catchup=True,
    max_active_runs=1,
    tags=['zoomcamp']
) as dag:

    create_data_dir = PythonOperator(
        task_id="create_data_dir",
        python_callable=ensure_data_dir_exists
    )

    download_dataset = BashOperator(
        task_id='download_dataset',
        bash_command=f'curl -sSL {URL_TEMPLATE} > {OUTPUT_FILE_TEMPLATE}'
    )

    ingest_task = PythonOperator(
        task_id='ingest_to_postgres',
        python_callable=ingest_to_postgres,
        op_kwargs={'file_path': OUTPUT_FILE_TEMPLATE}
    )

    create_data_dir >> download_dataset >> ingest_task
