# Cloud Data Warehouses

## Introduction To Data Warehouses

By the end of the lesson, you’ll be able to:

- Describe the business need for data warehouses
- Describe the architecture of data warehouses
- Run ETL processes to support dimensional modeling
- Create an OLAP cube from facts and dimensions

<figure>
  <img src="images/1-introduction-to-cloud-data-warehouses.jpg" alt="Data warehouse representation" width=60% height=60%>
</figure>

### Data Warehouse for Business Analytics

#### Operational vs Analytical Business Processes

**Operational processes**: Make it work.
    - Find goods & make orders (for customers)
    - Stock and find goods (for inventory staff)
    - Pick up & deliver goods (for delivery staff)

**Analytical processes**s: What is going on?
    - Assess the performance of sales staff (for HR)
    - See the effect of different sales channels (for marketing)
    - Monitor sales growth (for management)

![OLTP and OLAP](images/2-introduction-to-datawarehousing.png)

- OLTP databases have to scale and maintain a level of performance to accommodate customer transactions and will have a different level of complexity(because they integrate with multiple systems). But in case of OLAP, requirements may not be very clear and should have a flexibility.
- OLTP data need to be recent, updated and available in real-time for customers. While OLAP data needs to be historical, accurate and aggregated.
- OLTP data is often stored in normalized relational databases. While, data analysts want to work with dimensional data. 

These differences between OLTP and OLAP resulted in the invention of data warehouses.

**Data Warehouse** is a system(including processes, technologies and data representations) that enable us to support analytical processes.

Data from OLTP is moved to data warehouse to support OLAP.

<figure>
  <img src="images/2-introduction-to-datawarehousing.png" alt="OLTP and OLAP" width=60% height=60%>
</figure>

A data warehouse is designed to optimize data analysis processes and gathers data from multiple sources.

### Data Warehouse Architecture

#### Data Warehouse Design(ETL)

**Extracting**:
    - Extract data from source periodically and transfer to data warehouse.

**Transforming**:
    - Integrates many sources together
    - Possibly cleansing: inconsistencies, duplication, missing values, etc..
    - Possibly producing diagnostic metadata

**Loading**:
    - Structuring and loading the data into the dimensional data model

<figure>
  <img src="images/3-DW_ETL_Design.png" alt="DW Design" width=60% height=60%>
</figure>

#### Technical Perspective

Extract the data from the source systems used for operations, transform the data, and load it into a dimensional model.

<figure>
  <img src="images/4-Kimballs_Bus_Architecture.png" alt="Kimball's Bus Architecture" width=60% height=60%>
</figure>

##### Characteristics of Kimball Bus Architecture

- Results in a common dimension data model shared by different departments.
- Data is not kept at the aggregated level, but rather at the atomic level.
- Organized by business processes, and used by different departments.

<figure>
  <img src="images/5-DWH_Tech_Perspective.png" alt="DWH Tech perspective" width=60% height=60%>
</figure>

### ETL and Dimensional Modelling

3NF use lot of expensive joins and hard to explain to business users. While dimensional modelling such as star schema uses joins with dimensions which is good for OLAP(not for OLTP).

**Goals of the star schema**:

- Easy to understand
- Fast analytical query performance

**Fact Tables**:

- Record business events, like an order, a phone call, a book review
- Fact tables columns record events recorded in quantifiable metrics like - quantity of an item, duration of a call, a book rating

**Dimension Tables**:

- Record the context of the business events e.g. who, what, where, why, etc.
- Dimension tables columns contain attributes like the store at which an item is purchased or the customer who made the call, etc.

Example:

<figure>
  <img src="images/6-pagila_star_schema.png" alt="Pagila star schema sample" width=60% height=60%>
</figure>

### Exploratory Data analysis

**How to use iPython to write SQL in Python**:

- load ipython-sql: **%load_ext sql**
- To execute SQL queries, prepend your SQL statements with either of these options:
  1. %sql
     - For a single line SQL query
     - Use **$** to access a python variable
  2. %%sql
     - For a multi-line SQL query
     - You will NOT be able to access a python variable using $
- Running a connection string like: *postgresql://postgres:postgres@db:5432/pagila* connects to the database

**Notes**:

- [Sakila](https://video.udacity-data.com/topher/2021/August/61120e06_pagila-3nf/pagila-3nf.png) is a sample database created by MySql.
- The postgresql version of it is called [Pagila](https://github.com/devrimgunduz/pagila).


<hr style="border:2px solid gray">

## ETL and Data Warehouse Technology in the Cloud


<hr style="border:2px solid gray">

## AWS Data Warehouse Technologies


<hr style="border:2px solid gray">

## Implementing a Data Warehouse on AWS


<hr style="border:2px solid gray">

## Project Data Warehouse