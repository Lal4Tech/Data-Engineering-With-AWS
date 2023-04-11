#Instructions
#In this exercise, we’ll consolidate repeated code into Operator Plugins
#1 - Replace both uses of the check_greater_than_zero function with calls to the HasRowsOperator
#2 - Execute the DAG

# Remember to run "/opt/airflow/start.sh" command to start the web server. Once the Airflow web server is ready,  open the Airflow UI using the "Access Airflow" button. Turn your DAG “On”, and then Run your DAG. If you get stuck, you can take a look at the solution file in the workspace/airflow/dags folder in the workspace and the video walkthrough on the next page.

import pendulum
import logging

from airflow.decorators import dag, task
from airflow.hooks.postgres_hook import PostgresHook

from airflow.operators.postgres_operator import PostgresOperator
from custom_operators.s3_to_redshift import S3ToRedshiftOperator
from custom_operators.has_rows import HasRowsOperator


from udacity.common import sql_statements

@dag(    
    start_date=pendulum.now(),
    max_active_runs=1
)

def demonstrate_custom_operators():

    @task()
    def check_greater_than_zero(*args, **kwargs):
        table = kwargs["params"]["table"]
        redshift_hook = PostgresHook("redshift")
        records = redshift_hook.get_records(f"SELECT COUNT(*) FROM {table}")
        if len(records) < 1 or len(records[0]) < 1:
            raise ValueError(f"Data quality check failed. {table} returned no results")
        num_records = records[0][0]
        if num_records < 1:
            raise ValueError(f"Data quality check failed. {table} contained 0 rows")
        logging.info(f"Data quality on table {table} check passed with {records[0][0]} records")



    create_trips_table = PostgresOperator(
        task_id="create_trips_table",
        postgres_conn_id="redshift",
        sql=sql_statements.CREATE_TRIPS_TABLE_SQL
    )

    copy_trips_task = S3ToRedshiftOperator(
        task_id="load_trips_from_s3_to_redshift",
        table="trips",
        redshift_conn_id="redshift",
        aws_credentials_id="aws_credentials",
        s3_bucket="sean-murdock",
        s3_key="data-pipelines/divvy/unpartitioned/divvy_trips_2018.csv"
    )

    #
    # TODO: Replace this data quality check with the HasRowsOperator
    #
    check_trips_task = HasRowsOperator(
        task_id="count_trips",
        table="trips",
        redshift_conn_id="redshift",
    )



    create_stations_table = PostgresOperator(
        task_id="create_stations_table",
        postgres_conn_id="redshift",
        sql=sql_statements.CREATE_STATIONS_TABLE_SQL,
    )

    copy_stations_task = S3ToRedshiftOperator(
        task_id="load_stations_from_s3_to_redshift",
        redshift_conn_id="redshift",
        aws_credentials_id="aws_credentials",
        s3_bucket="sean-murdock",
        s3_key="data-pipelines/divvy/unpartitioned/divvy_stations_2017.csv",
        table="stations"
    )

#
# TODO: Replace this data quality check with the HasRowsOperator
#
    check_stations_task = HasRowsOperator(
        task_id="count_stations",
        table="stations",
        redshift_conn_id="redshift",        
    )

    create_trips_table >> copy_trips_task
    create_stations_table >> copy_stations_task
    copy_stations_task >> check_stations_task
    copy_trips_task >> check_trips_task

custom_operators_dag = demonstrate_custom_operators()