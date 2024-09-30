from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {"depends_on_past": True}


def my_function(**context):
    print(int(context["ti"].xcom_pull(task_ids="t2")) * 2)


with DAG(
    dag_id="9-xcom",
    description="Testing XCom",
    schedule_interval="@once",
    start_date=datetime(2024, 9, 30),
    default_args=default_args,
    max_active_runs=1,
) as dag:
    t1 = BashOperator(
        task_id="t1",
        bash_command="sleep 5 && echo $((3*8))",
    )

    t2 = BashOperator(
        task_id="t2",
        bash_command="sleep 5 && echo {{ ti.xcom_pull(task_ids='t1') }}",
    )

    t3 = PythonOperator(
        task_id="t3",
        python_callable=my_function,
    )

    t1 >> t2 >> t3
