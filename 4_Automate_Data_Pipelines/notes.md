# Automate Data Pipelines

## Introdcution to Automating Data Pipelines

Focus on applying the data pipeline using an open-source tool from Airbnb called Apache Airflow.

Environment and Tools:

- Python 3
- Apache Airflow
- Amazon Web Services (AWS)
  - AWS Redshift
  - AWS S3

### Data Pipeline

- A data pipeline is a series of sequential data processing steps.
- Depending on the data requirements for each step, some steps may occur in parallel.
- Typically occur on a schedule.

<figure>
  <img src="images/example_pipeline.png" alt="Example Pipeline" width=60% height=60%>
</figure>

<hr style="border:2px solid gray">

## Data Pipelines

### DAGs and Data Pipelines

<figure>
  <img src="images/directed_acyclic_graph.png" alt="Diagram of a Directed Acyclic Graph" width=60% height=60%>
</figure>

**Bikeshare DAG Example**:

<figure>
  <img src="images/bikeshare_dag_example.png" alt="Bikeshare DAG example" width=60% height=60%>
</figure>

### Data Validation

- Data Validation is the process of ensuring that data is present, correct & meaningful.
- Ensuring the quality of the data through automated validation checks is a critical step in building data pipelines at any organization.
- Example: Bike sharing data, following validation steps are possible:
  - After loading from S3 to Redshift:
    - Validate the number of rows in Redshift match the number of records in S3
  - Once location business analysis is complete:
    - Validate that all locations have a daily visit average greater than 0
    - Validate that the number of locations in our output table match the number of tables in the input table

### Apache Airflow

- Platform to programmatically author, schedule and monitor workflows as DAGs of tasks.
- The airflow scheduler executes your tasks on an array of workers while following the specified dependencies.
- Simple to maintain
- Can run data analysis itself or trigger external tools during execution.
- Provides a web-based UI for users to visualize and interact with their data pipelines.
- Official Doc: [Apache Airflow](https://airflow.apache.org/)

<figure>
  <img src="images/airflow_component_diagram.jpeg" alt="Airflow component diagram" width=60% height=60%>
</figure>

- **Scheduler**: orchestrates the execution of jobs on a trigger or schedule.
- **Work Queue** is used by the scheduler to deliver tasks that need to be run to the Workers.
- **Worker**: processes execute the operations defined in each DAG.
- **Metastore Database**: saves credentials, connections, history, and configuration.
- **Web Interface** provides a control dashboard for users and maintainers.

<figure>
  <img src="images/how-airflow-works.png" alt="How Airflow works" width=60% height=60%>
</figure>


1. The Airflow Scheduler starts DAGs based on time or external triggers.
2. Once a DAG is started, the Scheduler looks at the steps within the DAG and determines which steps can run by looking at their dependencies.
3. The Scheduler places runnable steps in the queue.
4. Workers pick up those tasks and run them.
5. Once the worker has finished running the step, the final status of the task is recorded and additional tasks are placed by the scheduler until all tasks are complete.
6. Once all tasks have been completed, the DAG is complete.


<hr style="border:2px solid gray">

## Airflow and AWS

<hr style="border:2px solid gray">

## Data Quality

<hr style="border:2px solid gray">

## Production Data Pipelines

<hr style="border:2px solid gray">

## Project: Data Pipelines
