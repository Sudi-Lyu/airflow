from __future__ import annotations

from datetime import datetime

from airflow.decorators import dag, task


@dag(
    dag_id='log_generator',
    description='Generate 40K log lines',
    schedule=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
)
def log_generator_dag():
    @task
    def generate_40k_logs():
        """Generate 40K log lines"""
        for i in range(40000):
            print(f"Log line {i + 1}: This is a test log entry for performance testing")

    generate_40k_logs()


log_generator_dag()
