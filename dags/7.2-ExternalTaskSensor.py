from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.sensors.external_task import ExternalTaskSensor

with DAG(
    dag_id="7.2-ExternalTaskSensor",
    description="External Task Sensor DAG",
    schedule_interval="@daily",
    start_date=datetime(2024, 8, 10),
    end_date=datetime(2024, 8, 15),
) as dag:

    t1 = ExternalTaskSensor(
        task_id="waiting_dag",
        external_dag_id="7.1-ExternalTaskSensor",
        external_task_id="task1",
        poke_interval=10,
    )

    t2 = BashOperator(
        task_id="task2", bash_command="echo 'Task 2 Finished'", depends_on_past=True
    )

    t1 >> t2
