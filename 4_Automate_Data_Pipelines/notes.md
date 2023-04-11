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

**Exercise**: [Airflow DAGs](exercises/airflow_dags.py)

**Operators**:

- Define the atomic steps of work that make upa DAG
- common operators:
  - PythonOperator
  - PostgresOperator
  - RedshiftToS3Operator
  - S3ToRedshiftOperator
  - BashOperator
  - SimpleHttpOperator
  - Sensor

**DAG Decorator**:

- Annotation used to mark a function as the definition of a DAG.

```python
import pendulum
import logging
from airflow.decorators import dag

@dag(description='Analyzes test Data',
    start_date=pendulum.now(),
    schedule_interval='@daily')
def divvy_dag():
```

**Operators and Tasks**:

- Operators: Define atomic steps of work that make up a DAG.
- Tasks: Instantiated operators

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def hello_world():
    print(“Hello World”)

divvy_dag = DAG(...)
task = PythonOperator(
    task_id=’hello_world’,
    python_callable=hello_world,
    dag=divvy_dag)
```

Tasks can be defined using ```@task```decorators

```python
@task()
    def hello_world_task():
      logging.info("Hello World")
```

**Schedules**:

Define with cron strings or Airflow presets.

```@once```, ```@hourly```, ```@daily```, ```@weekly```, ```@monthly```, ```@yearly```, ```None```

**Start Date**: if start date is in the past, DAG will run as many times as there are schedule intervals between that start date and the current date.

**End Date**: Unless an optional end date is specified, DAGs will continue run until it get disabled or deleted.

**Exercise**: [Run the schedules](exercises/run_the_schedules.py)

<hr style="border:2px solid gray">

#### Task Dependencies

In DAGs:

- Nodes = Tasks
- Edges = Ordering and dependencies between tasks.
- ```a >> b``` means a comes before b. Similarly```a << b``` means a comes after b.
- Can also use ```set_downstream``` and ```set_upstream```
eg:

```python
hello_world_task = PythonOperator(task_id=’hello_world’, ...)
goodbye_world_task = PythonOperator(task_id=’goodbye_world’, ...)
...
# Use >> to denote that goodbye_world_task depends on hello_world_task
hello_world_task >> goodbye_world_task

# With set_downstream or set_upstream
hello_world_task.set_downstream(goodbye_world_task)
```

**Exercise**: [Task Dependencies](exercises/task_dependencies.py)

#### Airflow Hooks

- Connections can be access in code via hooks.
- Hooks provide a reusable interface to external systems and databases.
- Common hooks:
  - ```HttpHook```
  - ```PostgresHook```
  - ```MySqlHook```
  - ```SlackHook```
  - ```PrestoHook```

eg:

```python
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator

def load():
# Create a PostgresHook option using the `demo` connection
    db_hook = PostgresHook(‘demo’)
    df = db_hook.get_pandas_df('SELECT * FROM rides')
    print(f'Successfully used PostgresHook to return {len(df)} records')

load_task = PythonOperator(task_id=’load’, python_callable=hello_world, ...)
```

#### Context Variables

**kwargs parameter to accept the runtime variables in task.

```python
from airflow.decorators import dag, task

@dag(
  schedule_interval="@daily";
)
def template_dag(**kwargs):

  @task
  def hello_date():
    print(f"Hello {kwargs['ds']}}")
```

**Exercise**: [Context Templating](exercises/context_templating.py)

<hr style="border:2px solid gray">

## Airflow and AWS

### Create an IAM User in AWS

Permissions:

- AdministratorAccess
- AmazonRedshiftFullAccess
- AmazonS3FullAccess

Set and download Download access keys

### Airflow connections

Create connection in Airflow:

- **Connection Id**: Enter ```aws_credentials```.
- **Connection Type**: Enter ```Amazon Web Services```.
- **AWS Access Key ID**: Enter your **Access key ID** from the IAM User credentials you downloaded earlier.
- **AWS Secret Access Key**: Enter your **Secret access key** from the IAM User credentials you downloaded earlier. Once you've entered these values, select **Save**.
- Click the **Test** button to pre-test your connection information.

Command to create aws connection:

```bash
airflow connections add aws_credentials --conn-uri 'aws://<aws_access_key_id>:<aws_access_key_secret>'
```

**S3 Hook**

```python


from airflow.hooks.S3_hook import S3Hook
. . .
hook = S3Hook(aws_conn_id='aws_credentials')
        bucket = Variable.get('s3_bucket')
        prefix = Variable.get('s3_prefix')
        logging.info(f"Listing Keys from {bucket}/{prefix}")
        keys = hook.list_keys(bucket, prefix=prefix)
        for key in keys:
            logging.info(f"- s3://{bucket}/{key}")
    list_keys()

list_keys_dag = list_keys()
```

### Copy S3 Data

1. Create S3 bucket
```aws s3 mb s3:/`udacity-airflow-bkt/```
2. Copy data from udacity bucket to cloudshell directory:
```aws s3 cp s3://udacity-dend/data-pipelines/ ~/data-pipelines/ --recursive```
3. Copy the data from the home cloudshell directory to our own bucket:
```aws s3 cp ~/data-pipelines/ s3://udacity-airflow-bkt/data-pipelines/ --recursive```
4. List the data to be sure it copied over:
```aws s3 ls s3://udacity-airflow-bkt/data-pipelines/```
5. Update bucket name on copy statements on **Exercise**: [SQL Statments](exercises/sql_statements.py)

### Configure Variable

Open the Airflow UI and open Admin->Variables.

Click "Create".

Set ```Key``` equal to ```s3_bucket``` and set ```Value``` equal to bucket name.

Set ```Key``` equal to ```s3_prefix``` and set ```Value``` equal to ```data-pipelines```.

Click save.

Or through command line:

```bash
airflow variables set s3_bucket udacity-airflow-bkt
```

```bash
airflow variables set s3_prefix data-pipelines
```

Now, we can refer variable like this:

```python
from airflow.models import Variable
. . .
bucket = Variable.get('s3_bucket')
prefix = Variable.get('s3_prefix')
```

**Exercise**: [Connections and Hooks](exercises/connections_hooks.py)

### Configure AWS Redshift Serverless

**AWS Redshift Serverless** gives all the benefits of a Redshift cluster without paying for compute when your servers are idle.

**Grant Redshift access to S3 so it can copy data from CSV files**:

Create a Redshift Role called my-redshift-service-role from the AWS Cloudshell.

```bash
aws iam create-role --role-name my-redshift-service-role --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "redshift.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}'
```

Grant the role S3 Full Access:

```bash
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --role-name my-redshift-service-role
```

1. Go to Amazon Redshift > Redshift Serverless
2. Click Customize settings
3. Go with the default namespace name
4. Check the box Customize admin user credentials
5. Enter awsuser for the Admin user name
6. Enter a password (save this for later)
7. Associate the ```my-redshift-service-role``` created with Redshift. This will enable Redshift Serverless to connect with S3
8. Accept the defaults for Security and encryption
9. Accept the default Workgroup settings
10. Select Turn on enhanced VPC routing and click Save
11. Click Continue and wait for Redshift Serverless setup to finish
12. After status showing as *Available*, click the default workgroup
13. To make this cluster publicly accessible in order to connect to this cluster via Airflow:
    - Click Edit
    - Select Turn on Publicly accessible > Save
    - Click on **VPC security group** link to open EC2 console.
    - Go to Inbound Rules > *Edit inbound rules*.
    - Add an inbound rule, as shown in the image below.
      - Type = *Custom TCP*
      - Port range = *0 - 5500*
      - Source = *Anywhere-iPv4*
    - Now the Redshift Serverless should be accessible from Airflow.
14. Go back to Redshift workgroup and copy the end point.  

### Airflow Connections to AWS Redshift

Create connection by going to to Admin > Connections with following info:

- **Connection Id**: Enter redshift.
- **Connection Type**: Choose Amazon Redshift.
- **Host**: Enter the endpoint of your Redshift Serverless workgroup, excluding the port and schema name at the end
- **Schema**: Enter dev. This is the Redshift database you want to connect to.
- **Login**: Enter awsuser.
- **Password**: Enter the password created when launching Redshift serverless.
- **Port**: Enter 5439. Once you've entered these values, select Save.

or with command, eg:

```bash
airflow connections add redshift --conn-uri 'redshift://awsuser:R3dsh1ft@default.859321506295.us-east-1.redshift-serverless.amazonaws.com:`439/dev'
```

### PostgresHook and Postgres Operator

Python class ```MetastoreBackend```connects to the Airflow Metastore Backend to retrieve credentials and other data required to connect to outside systems.

Usage:

```python
from airflow.decorators import dag
from airflow.secrets.metastore import MetastoreBackend


@dag(
    start_date=pendulum.now()
)
def load_data_to_redshift_dag():

    @task
    def copy_task():    
        metastoreBackend = MetastoreBackend()
        aws_connection=metastoreBackend.get_connection("aws_credentials")
        # aws_connection.login contains Access key ID
        # aws_connection.password contains secret access key
        logging.info(vars(aws_connection))
```

```PostgresHook```: superclass of the Airflow ```DbApiHook```. It can be used to get all the connection details for the postgres database using connection id.

```python
from airflow.providers.postgres.operators.postgres import PostgresOperator
. . .
redshift_hook = PostgresHook("redshift")

redhisft_hook.run("SELECT * FROM trips")
```

**PostgresOperator**:

```python
from airflow.hooks.postgres_hook import PostgresHook
from airflow.decorators import dag

@dag(
    start_date=pendulum.now()
)
def load_data_to_redshift_dag():


. . .
    create_table_task=PostgresOperator(
        task_id="create_table",
        postgres_conn_id="redshift",
        sql=sql_statements.CREATE_TRIPS_TABLE_SQL
    )
. . .
    create_table_task >> copy_data
```

### Build the S3 to Redshift DAG

**Exercise**: [S3 to Redshift](exercises/s3_to_redshift.py)

### Putting all together

<figure>
  <img src="images/airflow_aws_all_together.png" alt="Airflow and AWS Putting all together" width=60% height=60%>
</figure>

<hr style="border:2px solid gray">

## Data Quality

### Data Lineage

The data lineage of a dataset describes the discrete steps involved in the creation, movement, and calculation of that dataset.

Why data lineage is important:

- **Build Confidence**: being able to describe the data lineage of a particular dataset or analysis will build confidence in data consumers.
- **Defining Metrics**: it allows everyone in the organization to agree on the definition of how a particular metric is calculated.
- **Debugging**: helps data engineers track down the root of errors when they occur.

**Visualizing Data Lineage**:

<figure>
  <img src="images/bikeshare_data_lineage.jpeg" alt="Bikeshare Data Lineage" width=60% height=60%>
</figure>

Airflow DAGs are a natural representation for the movement & transformation of data.

<figure>
  <img src="images/airflow_data_lineage.jpeg" alt="Airflow Data Lineage" width=60% height=60%>
</figure>

- Airflow keeps a record of historical DAG and task executions.
- It does not store the code from those historical runs.
- Whatever the latest code is in your DAG definition is what Airflow will render for you in the browser.

**Exercise**: [Data Lineage](exercises/data_lineage.py)

### Data Pipeline Schedules

**Data in Time Ranges**:

When a data pipeline is designed with a schedule in mind, we can use the execution time of the pipeline run to only analyze data from the time period since this data pipeline last ran.

**Analyzing an Entire Dataset**:

In a naive analysis, with no scope, we would analyze all of the data at all times.

**Schedules**:

Pipelines are often driven by schedules which determine what data should be analyzed and when.

- Pipeline schedules can reduce the amount of data that needs to be processed in a given run.
- Using schedules to select only data relevant to the time period of the given pipeline execution can help improve the quality and accuracy of the analyses performed by our pipeline.
- Running pipelines on a schedule will decrease the time it takes the pipeline to run.

**Selecting the time period**:

Factors to be considered in determining the appropriate time period for a schedule:

- What is the size of data, on average, for a time period?
- How frequently is data arriving, and how often does the analysis need to be performed?
- What's the frequency on related datasets? 

<hr style="border:2px solid gray">

### Scheduling in Airflow

Airflow will **catchup** by creating a DAG run for every period defined by the *schedule_interval* between the *start_date* and *now*.

<figure>
  <img src="images/scheduling_in_airflow.jpeg" alt="Scheduling in airflow" width=60% height=60%>
</figure>

**catchup**:

- Airflow uses the schedule interval to create historical DAG runs and catchup data.
- Whenever the start date of a DAG is in the past, and the time difference between the start date and now includes more than one schedule intervals, Airflow will automatically schedule and execute a DAG run to satisfy each one of those intervals.
- Catchup is enabled by default.

**Start Date**:

- Airflow will begin running pipelines on the date in the ```start_date``` parameter.
- This is the date when a scheduled DAG will start executing on its own.

```python
@dag(
    # schedule to run daily
    # once it is enabled in Airflow
    schedule_interval='@daily',
    start_date=pendulum.now(),
    catchup=False
)
```

**End Date**:

- Can use an end_date parameter to let Airflow know the date it should stop running a scheduled pipeline.
- End_dates can also be useful when you want to perform an overhaul or redesign of an existing pipeline. Update the old pipeline with an ``end_date``` and then have the new pipeline start on the end date of the old pipeline.

```python
@dag(
    start_date=pendulum.datetime(2022, 8, 1, 0, 0, 0, 0),
    end_date=pendulum.datetime(2022, 9, 1, 0, 0, 0, 0),
    schedule_interval='@daily',
    max_active_runs=1    
)
```

**Exercise**: [Schedules and Catchups in Airflow](exercises/data_lineage.py)

### Data Partitioning

- **Schedule partitioning**: Apart from reducing the amount of data our pipelines have to process, schedules also help us guarantee that we can meet timing guarantees that our data consumers required.
- **Logical partitioning**: Conceptually related data can be partitioned into discrete segments and processed separately.
- **Size Partitioning**: separates data for processing based on desired or required storage limits.

**Goals of Data Partitioning**:

- Pipelines designed to work with partitioned data fail more gracefully.
  - Smaller datasets, smaller time periods, and related concepts are easier to debug than big datasets, large time periods, and unrelated concepts.
  - Partitioning makes debugging and rerunning failed tasks much simpler.
  - Enables easier redos of work, reducing cost and time.
- If data is partitioned appropriately, there will be fewer dependencies on each other. Because of this, Airflow will be able to parallelize execution of your DAGs to produce your results even faster.

**Exercise**: [Data Partitioning](exercises/data_partitioning.py)

### Data Quality Requirements

**Data Quality** is the measure of how well a dataset satisfies its intended use.

- Adherence to a set of requirements is a good starting point for measuring data quality.

**Examples of Data Quality Requirements**:

- Data must be a certain size
- Data must be accurate to some margin of error
- Data must arrive within a given timeframe from the start of execution. Use SLA in Airflow
- Pipelines must run on a particular schedule
- Data must not contain any sensitive information

**Exercise**: [Data Quality](exercises/data_quality.py)

## Production Data Pipelines

### Extending Airflow Plugins & Contrib

Custom **Hooks** allow Airflow to integrate with non-standard datastores and systems.

[Airflow Contrib](https://github.com/apache/airflow/tree/main/airflow/contrib): to check existing Airflow plugins and contribute.

Custom Operators are typically used to capture frequently used operations into a reusable form.

The most common types of user-created plugins for Airflow are Operators and Hooks.

To create custom operator, follow the steps:

1. Identify Operators that perform similar functions and can be consolidated
2. Define a new Operator in the plugins folder
3. Replace the original Operators with your new custom one, re-parameterize, and instantiate them.

Official doc: [Creating a custom operator](https://airflow.apache.org/docs/apache-airflow/stable/howto/custom-operator.html)

**Exercise**: [Custom Operators](exercises/custom_operators.py)

### Best Practices for Data Pipeline Steps - Task Boundaries

DAG tasks should be designed such that they are:

- Atomic and have a single purpose
- Maximize parallelism
- Make failure states obvious

Every task in the dag should perform only one job.

Helps to understand the flow easily. Also, can be easily parallelized to improve execution speed.

**Exercise**: [Refactor DAG](exercises/refactor_dag.py)

### Converting an Airflow 1 DAG

The main difference between Airflow 1 and Airflow 2 syntax is the functional paradigm, and the use of Decorators for Tasks and DAGs.

Key Differences:

- Airflow1 instantiates the DAG directly with dag= DAG (...) whereas, with Airflow2, you'll use a decorator.
- Airflow1 uses explicitly stated DAG names, but Airflow2 can infer DAG names from functions.
- Airflow1 uses PythonOperator() in tasks, but in Airflow2, you'll use a regular Python function with the task decorator.
- In Airflow2, you don't instantiate the DAG, so you don't have to pass the DAG.

**Airflow 1**:

```python
dag = DAG(
    'data_quality_legacy',
    start_date=pendulum.datetime(2018, 1, 1, 0, 0, 0, 0),
    end_date=pendulum.datetime(2018, 12, 1, 0, 0, 0, 0),
    schedule_interval='@monthly',
    max_active_runs=1
)

def load_trip_data_to_redshift(*args,* *kwargs):
    metastoreBackend = MetastoreBackend()
    aws_connection=metastoreBackend.get_connection("aws_credentials")
    redshift_hook = PostgresHook("redshift")
    execution_date = kwargs["execution_date"]
    sql_stmt = sql_statements.COPY_MONTHLY_TRIPS_SQL.format(
        aws_connection.login,
        aws_connection.password,
        year=execution_date.year,
        month=execution_date.month
    )
    redshift_hook.run(sql_stmt)

load_trips_task = PythonOperator(
    task_id='load_trips_from_s3_to_redshift',
    dag=dag,
    python_callable=load_trip_data_to_redshift,
    provide_context=True,
    sla=datetime.timedelta(hours=1)
)

. . .

create_trips_table >> load_trips_task
```

**Airflow 2**:

```python
@dag(
    start_date=pendulum.datetime(2018, 1, 1, 0, 0, 0, 0),
    end_date=pendulum.datetime(2018, 12, 1, 0, 0, 0, 0),
    schedule_interval='@monthly',
    max_active_runs=1    
)
def data_quality():

    @task(sla=datetime.timedelta(hours=1))
    def load_trip_data_to_redshift(*args,* *kwargs):
        metastoreBackend = MetastoreBackend()
        aws_connection=metastoreBackend.get_connection("aws_credentials")
        redshift_hook = PostgresHook("redshift")
        execution_date = kwargs["execution_date"]
        sql_stmt = sql_statements.COPY_MONTHLY_TRIPS_SQL.format(
            aws_connection.login,
            aws_connection.password,
            year=execution_date.year,
            month=execution_date.month
        )
        redshift_hook.run(sql_stmt)

    load_trips_task = load_trip_data_to_redshift()
    
. . .

create_trips_table >> load_trips_task
```

**Exercise**: [Convert Airflow 1 to 2](exercises/convert_airflow1.py)

### Monitoring

**Service Level Agreements**:

DAGs can be configured to have an SLA which is defined as a time by which a DAG must com.

**Emails and Alerts**:

Airflow can be configured to send emails on DAG and task state changes.

**Metrics**:

- Airflow can be configured to publish metrics to *Statsd* and *Prometheus*.
- *Statsd* and *Prometheus* can be used together to view Airflow system metrics as well as trigger alerts for outages and failures.


**Logging**:

- By default, Airflow logs to the local file system.
- Logs can be forwarded using standard logging tools like *fluentd*.

### Building a full pipeline

**Exercise**: [Bulding full DAG](exercises/build_full_dag.py)

### Putting all together

Airflow has robbest ecosystem for logging, monitoring, and metrics.

<figure>
  <img src="images/airflow_instrumentation.png" alt="Airflow Instrumentation" width=60% height=60%>
</figure>

### Data Pipeline Orchestrators

Other Pipeline Orchestrators: [Pipeline frameworks & libraries](https://github.com/pditommaso/awesome-pipeline)

[Luigi vs Airflow](https://medium.com/@cyrusv/luigi-vs-airflow-vs-zope-wfmc-comparison-of-open-source-workflow-engines-de5209e6dac1)

<hr style="border:2px solid gray">

## Project: Data Pipelines with Airflow

A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

They have decided to bring you into the project and expect you to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

[Data Pipelines with Airflow](4_Automate_Data_Pipelines/project/README.md)