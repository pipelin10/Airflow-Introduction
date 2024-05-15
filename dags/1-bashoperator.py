from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="bashoperator",
         description="Using bash operator",
         start_date=datetime(2024, 5, 10)) as dag:
    t1 = BashOperator(task_id="hello_with_bash",
                      bash_command="echo 'Hello World from Airflow!'")
    t1