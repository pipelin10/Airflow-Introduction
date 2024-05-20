from airflow import DAG
from datetime import datetime
from hello_operator import HelloOperator

with DAG(dag_id="custom_operator",
         description="Using custom operator",
         schedule_interval="@once",
         start_date=datetime(2024, 5, 20)) as dag:
    t1 = HelloOperator(task_id="custom_hello",
                        name="Felipe")