from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="5.1-orchestration",
         description="Orchestration example",
         schedule_interval="@daily",
         start_date=datetime(2024, 4, 20),
         end_date=datetime(2024,5,20),
         default_args={
             "depends_on_past": True},
         max_active_runs=1) as dag:
    
    t1 = BashOperator(task_id="task1_orchestator",
                      bash_command="sleep 2 && echo 'Task 1'")
    
    t2 = BashOperator(task_id="task2_orchestator",
                        bash_command="sleep 2 && echo 'Task 2'")
    
    t3 = BashOperator(task_id="task3_orchestator",
                        bash_command="sleep 2 && echo 'Task 3'")
    
    t4 = BashOperator(task_id="task4_orchestator",
                        bash_command="sleep 2 && echo 'Task 4'")
    
    t1 >> t2 >> [t3, t4]
    