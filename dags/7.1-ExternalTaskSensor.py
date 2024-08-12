from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="7.1-ExternalTaskSensor",
    description="External Task Sensor DAG",
    schedule_interval="@daily",
    start_date=datetime(2024, 8, 10),
    end_date=datetime(2024, 8, 15),
) as dag:

    t1 = BashOperator(
        task_id="task1", bash_command="sleep 10 && echo 'Task 1 Finished'"
    )

    t1
