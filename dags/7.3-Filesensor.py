from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

with DAG(
    dag_id="7.3-Filesensor",
    description="File Sensor DAG",
    schedule_interval="@daily",
    start_date=datetime(2024, 8, 10),
    end_date=datetime(2024, 8, 15),
) as dag:

    t1 = BashOperator(
        task_id="creating_file",
        bash_command="sleep 10 && touch /tmp/file.txt",
    )

    t2 = FileSensor(
        task_id="waiting_for_file",
        filepath="/tmp/file.txt",
        poke_interval=10,
    )

    t3 = BashOperator(
        task_id="end_task",
        bash_command="echo 'File was created!'",
    )

    t1 >> t2 >> t3
