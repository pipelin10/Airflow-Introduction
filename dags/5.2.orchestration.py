from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(dag_id="5.2-orchestration",
         description="Orchestration example",
         schedule_interval="0 7 * * 1",
         start_date=datetime(2024, 3, 20),
            end_date=datetime(2024,5,20)) as dag:
    
    t1 = EmptyOperator(task_id="task1")
    t2 = EmptyOperator(task_id="task2")
    t3 = EmptyOperator(task_id="task3")
    t4 = EmptyOperator(task_id="task4")
    
    t1 >> t2 >> t3 >> t4