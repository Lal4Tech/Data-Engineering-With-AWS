import pendulum
import logging

from airflow.decorators import dag, task

@dag(
    # schedule to run daily
    # once it is enabled in Airflow
    schedule_interval='@daily',
    start_date=pendulum.now()
)
def greet_flow():
    
    @task
    def hello_world():
        logging.info("Hello World!")

    # hello_world represents the invocation of the only task in this DAG
    # it will run by itself, without any sequence before or after another task
    hello_world_task=hello_world()

greet_flow_dag=greet_flow()