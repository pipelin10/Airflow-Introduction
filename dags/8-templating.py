from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

template_command = """
{% for file in params.filenames %}
    echo "{{ ds }}"
    echo "{{ file }}"
{% endfor %}
"""

with DAG(
    dag_id="8.templating",
    description="Templating DAG",
    schedule_interval="@daily",
    start_date=datetime(2024, 9, 30),
    end_date=datetime(2024, 10, 5),
    max_active_runs=1,
) as dag:

    t1 = BashOperator(
        task_id="t1",
        bash_command=template_command,
        params={"filenames": ["/tmp/file1.txt", "/tmp/file2.txt"]},
        depends_on_past=True,
    )

    t1
