import logging
import pendulum

from airflow.decorators import dag, task
from airflow.models import Variable

@dag(
    start_date=pendulum.now(),
    schedule_interval="@daily"
)
def log_details():

    @task
    def log_execution_date(**kwargs):
        logging.info(f"Execution date is {kwargs['ds']}")

    @task
    def log_run_id(**kwargs):
        logging.info(f"My run id is {kwargs['run_id']}")
    
    @task
    def log_previous_run(**kwargs):
        logging.info(f"My previous run was on {kwargs['prev_start_date_success']}")
    
    @task
    def log_next_run(**kwargs):
        logging.info(f"My next run will be {kwargs['next_execution_date']}")


    log_execution_date_task=log_execution_date()
    log_run_id_task=log_run_id()
    log_previous_run_task=log_previous_run()
    log_next_run_task=log_next_run()

log_details_dag = log_details()