from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
        print("Hello World from Airflow!")

with DAG(dag_id="python_operator",
         description="Using python operator",
         schedule_interval="@once",
         start_date=datetime(2024, 5, 10)) as dag:
    
    t1 = PythonOperator(task_id="hello_with_python",
                        python_callable=hello_world)