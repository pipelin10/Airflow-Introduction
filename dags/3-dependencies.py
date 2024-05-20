from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def hello_world():
    print("Hello World from Airflow!")

with DAG(dag_id="dependencies",
         description="Using dependencies",
         schedule_interval="@once",
         start_date=datetime(2024, 5, 20)) as dag:
    t1 = PythonOperator(task_id="hello_with_python_dependencies",
                        python_callable=hello_world)
    t2 = BashOperator(task_id="task2",
                      bash_command="echo 'Task 2'")
    t3 = BashOperator(task_id="task3",
                        bash_command="echo 'Task 3'")
    t4 = BashOperator(task_id="task4",
                        bash_command="echo 'Task 4'")
    t1 >> [t2, t3] >> t4
    