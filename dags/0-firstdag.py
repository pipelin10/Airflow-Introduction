from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(dag_id="first_dag",
         description="This is the first example",
         start_date=datetime(2023, 5, 15),
         schedule_interval="@once") as dag:
    t1 = EmptyOperator(task_id="dummy")