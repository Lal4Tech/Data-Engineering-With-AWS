# Spark and Data Lakes

## Introduction to Spark and Data Lakes

This course contains hands-on exercises and a project to develop skills in the following areas:

- Big Data Engineering and Ecosystem
- Apache Spark
- Using Spark with Amazon Web Services (AWS)
- Building a data lake house on AWS

<hr style="border:2px solid gray">

## Big Data Ecosystem, Data Lakes and Spark

- The modern big data ecosystem is an evolution of data processing on distributed architecture necessary to handle the sheer volume of data.
- The job of data engineer is to skillfully use modern tools and techniques to create the big data ecosystem.

### Evolution of Big Data Ecosystem

<figure>
  <img src="images/evolution_of_bigdata_ecosystem.png" alt="Evolution of Big Data Ecosystem" width=60% height=60%>
</figure>

- Early efforts at processing large amounts of structured, semi-structured, and unstructured data led to the development of Hadoop. Hadoop incorporates two key components:
  - **The Hadoop Distributed File System (or HDFS)** provides distributed storage with high-throughput access to data.
  - **MapReduce** provides a way to conduct massive parallel processing for large amounts of data.
- Next evolution was **Apache Spark**
  - Built on ideas of Hadoop
  - Provides multiple APIs for processing data
  - Provides interactive interface for iteratively developing data engineering/science solutions.
- Hadoop + Spark led to the development of **Data lakes**
  - To process large amounts of both structured and unstructured data.
- Last step in the evolution is the **Lake house architecture**
  - Combine the strengths of both data lakes and data warehouses.

### From Hadoop to Data Lakehouse

<figure>
  <img src="images/hadoop_to_data_lakehouse.png" alt="Haoop to Data Lakehouse" width=60% height=60%>
</figure>

- Data warehouses are based on specific and explicit data structures that allow for highly performant business intelligence and analytics but they do not perform well with unstructured data.
- Data lakes are capable of ingesting massive amounts of both structured and unstructured data with Hadoop and Spark providing processing on top of these datasets.
- Data lakes have several shortcomings
  - They are unable to support transactions and perform poorly with changing datasets.
  - Data governance became difficult due to the unstructured nature of these systems.
- Modern lakehouse architectures seek to combine the strengths of data warehouses and data lakes into a single, powerful architecture.

### The Hadoop Ecosystem

- **Hadoop**: an ecosystem of tools for big data storage and data analysis.
- **Hadoop MapReduce**: a system for processing and analyzing large data sets in parallel.
- **Hadoop YARN**: a resource manager that schedules jobs across a cluster.
- **Hadoop Distributed File System (HDFS)**: a big data storage system that splits data into chunks and stores the chunks across a cluster of computers.
- **Apache Pig**: a SQL-like language that runs on top of Hadoop MapReduce
- **Apache Hive**: another SQL-like interface that runs on top of Hadoop MapReduce.

#### Spark vs Hadoop

- Spark is another big data framework.
- Spark contains libraries for data analysis, machine learning, graph analysis, and streaming live data.
- Spark is generally faster than Hadoop. This is because Hadoop writes intermediate results to disk whereas Spark tries to keep intermediate results in memory whenever possible.
- Hadoop ecosystem includes a distributed file storage system called HDFS. Spark, on the other hand, does not include a file storage system. Spark can read in data from other sources as well.

#### Streaming Data

- **Use case**: when we want to store and analyze data in real-time.
- Popular streaming libraries:
  - [Spark Streaming](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
  - [Storm](https://storm.apache.org/)
  - [Flink](https://flink.apache.org/)
- Storm and Flink are designed for fast streaming. Better than Spark streaming.

### MapReduce

- **MapReduce**: a programming technique for manipulating large data sets.
- **Hadoop MapReduce**: an implementation of MapReduce.
- Steps:
  1. Divide the large dataset and distributing the data across a cluster.
  2. *Map*: data is analyzed and converted into a (key, value) pair.
  3. *Shuffle*:These key-value pairs are shuffled across the cluster so that all keys are on the same machine.
  4. *Reduce*: the values with the same keys are combined together.

**Exercise**: [Map Reduce](exercises/1_mapreduce_practice.ipynb)

### Spark

Spark is currently one of the most popular tools for big data analytics. It's a

- Data engineering tool
- Data analytics tool
- Data science tool

Apache Spark can be used to perform data engineering tasks for building both data lakes and lakehouse architectures.

#### Spark Cluster

Most computational frameworks are organized into a **master-worker** hierarchy:

- The master node is responsible for orchestrating the tasks across the cluster
- Workers are performing the actual computations

<figure>
  <img src="images/spark_modes.png" alt="Spark Modes" width=60% height=60%>
</figure>

There are four different modes to setup Spark:

1. **Local Mode**:
   - Everything happens on a single machine. So, while we use spark's APIs, we don't really do any distributed computing.
   - Useful to learn syntax and to prototype your project.
2. **Cluster Modes**:
   - Distributed and declare a cluster manager.
   - The cluster manager is a separate process that monitors available resources and makes sure that all machines are responsive during the job.
   - There are three different options of cluster managers.
     a. *Standalone*
        - Spark's own cluster manager.
        - There is a Driver process which act as the master and is responsible for scheduling tasks.
     b. *YARN*
        - From Hadoop project
     c. *Mesos*
        - Open-source manager from UC Berkeley's AMPLab Coordinators.

#### Spark Use Cases

Resources about Spark use cases:

- [Data Analytics](https://spark.apache.org/sql/)
- [Machine Learning](https://spark.apache.org/mllib/)
- [Streaming](https://spark.apache.org/streaming/)
- [Graph Analytics](https://spark.apache.org/graphx/)

**When to Use Spark**:

Spark is meant for big data sets that cannot fit on one computer. If data sets fit on local computer, following methods can be used:

- AWK - a command line tool for manipulating text files
- Python or R libraries
- Even if data is little bigger than memory, Pandas can read data in chunks.

Other possible methods:

- If data is stored in relational databases, can leverage SQL to extract, filter and aggregate the data.
- [SQLAlchemy](https://www.sqlalchemy.org/) provides an abstraction layer to manipulate SQL tables with generative Python expressions. It enables to leverage pandas and SQL simultaneously.

#### Spark's Limitations

- Spark Streaming’s latency is at least 500 milliseconds since it operates on micro-batches of records, instead of processing one record at a time.
- Streaming tools such as **Storm, Apex or Flink** are sutiable for low latency applications.
- Spark only supports ML algorithms that scale linearly with the input data size.

### Data Lakes

- In data warehouses data has to be structured going in and out of it.
- A data lake on the other hand, pours all of the data into a single repository, ready to be consumed by whoever and wherever they need.
- Data warehouses consist of only highly structured data that is suitable for business intelligence and reporting needs.
- Data lakes provide the ability to serve up both structured and un-structured data from a single data store.
- Key features of data lakes include:
  - Lower costs associated with using big data tools for ETL / ELT operations.
  - Data lakes provide schema-on-read rather than schema-on-write which lowers the cost and work of ingesting large amounts of data.
  - Data lakes provide support for structured, semi-structured, and unstructured data.

### Data Lakehouse

Though data lakes provide huge improvement in handling both structured and un-structured data, With the need to ingest a large amount of unstructured data, we lost:

- Atomic transactions: failed production jobs left data in a corrupted state.
- Quality enforcement: inconsistent and therefore unusable data.
- Consistency in data structures: impossible to stream and batch process data while ingesting.

Lake house architecture overcome these limitations with the creation of a **metadata** and **data governance layer** on top of the data lake.

One of the important features of a lakehouse architecture is the ability to quickly ingest large amounts of data and then incrementally improve the quality of the data.

The key difference between data lakes and data lakehouse architectures is the inclusion of the metadata and governance layer which provides atomicity, data quality, and consistency for the underlying data lake.

<hr style="border:2px solid gray">

## Spark Essential

### The Spark DAG

- In distributed systems, a program should not rely on resources created by previous executions.
- An **idempotent program** can run multiple times without any effect on the result.
- Non-idempotent programs depend on prior state in order to start executing.
- Example of relying on prior state:

```java
ledgerBalance = getLedgerBalanceFromLastRun()
ledgerBalance = ledgerBalance + getLedgerBalanceSinceLastRun()
```

- Example of avoiding prior state

```java
ledgerBalance = addAllTransactions()
```

- One goal of idempotent code is that data can be processed in parallel. This is achieved by calling the same code repeatedly in different threads and on different nodes/servers for each chunk or block of data. If each program has no reliance on prior execution, there should be no problem splitting up processing.
- Using Spark, large data can be handled using special datasets called **Resilient Distributed Datasets (RDDs)** and **DataFrames**.
- Instead of holding the data in memory, these datasets the Spark job access to the shared resources of the cluster in a very controlled way, that is managed outside of your Spark job.

```java
# Instead of doing something like this 

textFile = open("invoices.txt", "r")

# invoiceList could occupy Gigabytes of Memory
invoiceList = textFile.readlines()

print(invoiceList)

# Do something like this instead

invoiceDataFrame = spark.read.text("invoices.txt")

# Leverage Spark DataFrames to handle large datasets
invoiceDataFrame.show(n=10)
```

<figure>
  <img src="images/spark_dag.png" alt="Spark DAG" width=60% height=60%>
</figure>

- Every Spark program makes a copy of its input data and never changes the original parent data.
- Because Spark doesn't change or mutate the input data, it's known as **immutable**.
- When multiple functions calls in program, Spark chaining these together so that each accomplish small chunk of work.
- Then Spark finds a more optimal execution plan.
- **Lazy evaluation**: Spark uses this programming concept. Before Spark does anything with the data in your program, it first builds step-by-step directions of what functions and data it will need. It's called **Directed Acyclic Graph (DAG).**. The reference is made to the fact that no explicit repetition is inherent in the process.
- For example, if a specific file is read more than once in your code, Spark will only read it one time.
- Spark builds the DAG from your code, and checks if it can be delayed, waiting until the last possible moment to get the data.
- Output of spark execution shows something like this: 

```bash
[Stage 20:> ======>                                         (0 + 1) / 1]
```

- This means your code is on stage 20 of its physical execution plan.
- Data is processed in parallel tasks at each stage, separated by data partitions, so data in the same partition can be processed more efficiently.

### Resilient Distributed Datasets

Spark processes data using a cluster of distributed computing resources.

1. Source data is loaded from a different sources like database.
2. Spark converts this data into an immutable collection of objects for distributed processing called a Resilent Distributed Dataset or RDD.

The features of the RDD are designed for efficient data processing; it is fault-tolerant (recomputed in case of failure), cacheable, and partitioned.

<figure>
  <img src="images/spark_catalyst.png" alt="Spark Catalyst" width=60% height=60%>
</figure>

Sparks's query optimizer(Catalyst) convert code written in high level language like python/sql to DAG:

The code generated based on the execution plan operates on a lower level data abstraction called Resilient Distributed Dataset(RDD).

<figure>
  <img src="images/spark_version_rdd_mapping.png" alt="Spark Version RDD" width=60% height=60%>
</figure>

In Spark version 2.0 DataFrame and Datset API were unified.

**Resources**:

- [RDDs vs DataFrames and Datasets](https://www.databricks.com/blog/2016/07/14/a-tale-of-three-apache-spark-apis-rdds-dataframes-and-datasets.html)
- [RDD prgramming guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html)

### PySpark and SparkSession

**PySpark**:

- Python library used to write Spark Jobs.
- Give access to Spark Data constructs like RDDs, DataFrames, Spark SQL.

**SparkContext**:

- First component of a Spark Program.
- The main entry point for Spark functionality.
- Connects the cluster with the application.
- If using lower level abstractions, will create objects with SparkContext.
- To create a SparkContext: create *SparkConf* object by specifying information about the application(eg: name) and the Master node's IP address(*local* if run in local mode).

```python
from pyspark import SparkContext, SparkConf

configure = SparkConf().setAppName("app name").setMaster("IP Address")

sc = SparkContext(conf = configure)
```

**SparkSession**:

- Spark SQL equivalent which is used to read data frames.
- To create a SparkSession, use parameters/functions like *getOrCreate* which is used to retrieve the SparkSession if already existing or create new one.

```python
from pyspark import SparkSession

spark = SparkSession.builder.appName("app name").config("config option", "config value").getOrCreate()
```

### Maps and Lambda Functions

**Map**:

- Makes copy of the original input data and transforms according to the function passed to *map*.

eg:

```python
names = ["john", "bob", "martin", "Jannet", "Silvia"]

# Convert python list to distributed dataset for processing using Spark
distributed_names_rdd = spark.SparkContext.parallelize(names)

# function for converting to lower
def convert_to_lower(name):
  return name.lower

# Use Spark function map to apply convert_to_lower function to each item in the distributed dataset
step_to_lower = distributed_names_rdd.map(convert_to_lower)

# Spark commands are using lazy evaluation. So, the actual conversion is not happened yet. To force Spark to take some action on the data use collect function.
step_to_lower.collect()
```

**lambda**:

- Keyword for anonymous functions in python which is used to writing functional style programs.

eg:

```python
distributed_names_rdd.map(lambda name: name.lower())
```

**Exercise**: [Maps and Lambda functions](exercises/2_rdd_song_lower_case.py)

### Data Formats

Common data formats: CSV, JSON, HTML, and XML

### Distributed Data stores

- Store data in a fault-tolerant way.
- Hadoop's Distributed file system, HDFS splits file into 64/128 megabyte blocks and replicates these blocks across the cluster.
- Examples of distributed data services on cloud providers:
  - Amazon Simple Storages Sevice(S3)
  - Azure Blob Storage
  - Google Cloud Storage

### Imperative vs Declarative programming

#### Imperative programming using DataFrames and python

- Concerned with how
- Focus on exact steps, how to get to the result
- Data transformations with DataFrames

#### Declarative programming using SQL

- Concerned with what(result)
- Provides an abstraction layer for an imperative system

**Exercise**: [Reading and writing data to and fro of DataFrames](exercises/3_data_inputs_and_outputs.py)

<hr style="border:2px solid gray">

## Using Spark in AWS

<hr style="border:2px solid gray">

## Ingesting and Organizing Data in a Lakehouse

<hr style="border:2px solid gray">

## Project: STEDI Human Balance Analytics