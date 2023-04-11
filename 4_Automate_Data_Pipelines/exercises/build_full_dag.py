import pendulum

from airflow.decorators import dag,task

from custom_operators.facts_calculator import FactsCalculatorOperator
from custom_operators.has_rows import HasRowsOperator
from custom_operators.s3_to_redshift import S3ToRedshiftOperator
from airflow.operators.empty import EmptyOperator

#
# The following DAG performs the following functions:
#
#       1. Loads Trip data from S3 to RedShift
#       2. Performs a data quality check on the Trips table in RedShift
#       3. Uses the FactsCalculatorOperator to create a Facts table in Redshift
#           a. **NOTE**: to complete this step you must complete the FactsCalcuatorOperator
#              skeleton defined in plugins/operators/facts_calculator.py
#
@dag(start_date=pendulum.now())
def full_pipeline():
#
# The following code will load trips data from S3 to RedShift. Use the s3_key
#       "data-pipelines/divvy/unpartitioned/divvy_trips_2018.csv"
#       and the s3_bucket "sean-murdock"
#
    copy_trips_task = S3ToRedshiftOperator(
        task_id="load_trips_from_s3_to_redshift",
        table="trips",
        redshift_conn_id="redshift",
        aws_credentials_id="aws_credentials",
        s3_bucket="sean-murdock",
        s3_key="data-pipelines/divvy/unpartitioned/divvy_trips_2018.csv"
    )

#
#  Data quality check on the Trips table
#
    check_trips = HasRowsOperator(
        task_id="check_trips_data",
        redshift_conn_id="redshift",
        table="trips"
    )

#
# We use the FactsCalculatorOperator to create a Facts table in RedShift. The fact column is
#  `tripduration` and the groupby_column is `bikeid`
#
    calculate_facts = FactsCalculatorOperator(
        task_id="calculate_facts_trips",
        redshift_conn_id="redshift",
        origin_table="trips",
        destination_table="trips_facts",
        fact_column="tripduration",
        groupby_column="bikeid"
    )

#
# Task ordering for the DAG tasks 
#
    copy_trips_task >> check_trips
    check_trips >> calculate_facts

full_pipeline_dag = full_pipeline()
    