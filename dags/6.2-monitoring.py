from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.utils.trigger_rule import TriggerRule


def func_with_error():
    raise ValueError("This is an error")


_default_args = {}

with DAG(
    dag_id="6.2-monitoring",
    description="Monitoring DAG",
    schedule_interval="@daily",
    start_date=datetime(2024, 8, 11),
    end_date=datetime(2024, 8, 15),
    default_args=_default_args,
    max_active_runs=1,
) as dag:

    t1 = BashOperator(
        task_id="task1",
        bash_command="sleep 2 && echo 'Task 1'",
        trigger_rule=TriggerRule.ALL_SUCCESS,
    )

    t2 = BashOperator(
        task_id="task2",
        bash_command="sleep 2 && echo 'Task 2'",
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALL_SUCCESS,
        depends_on_past=True,
    )

    t3 = BashOperator(
        task_id="task3",
        bash_command="sleep 2 && echo 'Task 3'",
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALWAYS,
        depends_on_past=True,
    )

    t4 = PythonOperator(
        task_id="task4",
        python_callable=func_with_error,
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALL_SUCCESS,
        depends_on_past=True,
    )

    t5 = BashOperator(
        task_id="task5",
        bash_command="sleep 2 && echo 'Task 5'",
        retries=2,
        retry_delay=5,
        depends_on_past=True,
    )

    t1 >> t2 >> t3 >> t4 >> t5
