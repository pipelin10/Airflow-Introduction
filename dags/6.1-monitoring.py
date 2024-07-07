from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def func_with_error():
    raise ValueError("This is an error")

with DAG(dag_id="6.1-monitoring",
         description="Monitoring DAG",
            schedule_interval="@daily",
            start_date=datetime(2024, 5, 10)) as dag:
    
    t1 = BashOperator(task_id="task1",
                      bash_command="sleep 2 && echo 'Task 1'")
    
    t2 = BashOperator(task_id="task2",
                        bash_command="sleep 2 && echo 'Task 2'")
    
    t3 = BashOperator(task_id="task3",
                        bash_command="sleep 2 && echo 'Task 3'")
    
    t4 = PythonOperator(task_id="task4",
                        python_callable=func_with_error)
    
    t5 = BashOperator(task_id="task5",
                        bash_command="sleep 2 && echo 'Task 5'")
    
    t1 >> t2 >> t3 >> t4 >> t5