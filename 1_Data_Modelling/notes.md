# Data Modelling

## Introduction to Data Modelling

**Databases**: A [database](https://en.wikipedia.org/wiki/Database) is a structured repository or collection of data that is stored and retrieved electronically for use in applications. Data can be stored, updated, or deleted from a database.

**Database Management System (DBMS)**: The software used to access the database by the user and application is the database management system. Check out these few links describing a DBMS in more detail.

- [Introduction to DBMS](https://www.geeksforgeeks.org/database-management-system-introduction-set-1/)
- [DBMS as per Wikipedia](https://en.wikipedia.org/wiki/Database#Database_management_system)

### What is a Data Model**

> ...an abstraction that organizes elements of data and how they will relate to each other

So,
> Data modelling is the processing of creating data models for an information system.

The process of data modelling is to organize data into a database system to ensure that your data is persisted and easily usable by users in your organization.

It's a process to support business and user applications.

Steps:

1. Gather Requirements:
   - From application team, business users and end users to understand that what data must be retained and served as a business or the end-users.
   - First we need to map out that how our data must be stored and persisted and how that data will related to each other.
2. Conceptual Data Modelling
   - Entity mapping by hand or by using some tools.
3. Logical Data Modelling
   - Here conceptual data models are mapped to logical models using tales, schemas and columns.
4. Physical Data Modelling
   - Transform the logical data model to the DDL(Data Definition Language) to ale to create databases, tables and schemas.

Common questions:

- Why can't everything be stored in a giant excel spreadsheet:
  - Limitations to the amount of data that can be stored.
  - Read/write operations on a large scale is not possible
- Does data modeling happen before you create a database, or is it an iterative process?
  - Iterative process.
  - Have to continually reorganize, restructure and optimize data models as per the business needs.

### Why Data Model is important**

- **Data Organization**: Organized data determine later data usage.
- **Use Cases**: A well thought out data model enables straightforward and simple queries.
- **Starting early**: Begin prior to building out application, business logic and analytical models.
- **iterative process**: It's an iterative process as new requirements and new daa are introduced.

### Who does Data Modelling

Data modelling is an import skill for anyone involved in the process of using and analyzing data. including:

- Data Engineers
- Data Scientists
- Software Engineers
- Product Owners
- Business Users

### Introduction to Relational Databases

Relational and Non-relational databases do data modelling differently.

**Relational Model**
This model organized data into one or more *tables(or relations)* of *columns(attributes)* and *rows(tuples)* with a unique key identifying each row.

Generally each table represents one *entity type*.
eg: customer, product

**RDBMS(Relational Database Management System** is a software system used to maintain relational databases.

Examples of RDBMS:

- Oracle
- Teradata
- MySql
- PostgreSQL
- Sqlite
- Microsoft SQL Server

**SQL(Structured Query Language** is the language used across almost all relational database system for querying and maintaining the database.

**Database Schema**: Collection of tables
**Tables**: A group of rows sharing the same labelled elements(columns). eg: Customers

#### When to use relational databases

Advantages of Using a Relational Database

- **Flexibility for writing in SQL queries**: With SQL being the most common database query language.
- **Modeling the data not modeling queries**
- **Ability to do JOINS**
- **Ability to do aggregations and analytics**
- **Secondary Indexes available** : You have the advantage of being able to add another index to help with quick searching.
- **Smaller data volumes**: If you have a smaller data volume (and not big data) you can use a relational database for its simplicity.
**ACID Transactions**: Allows you to meet a set of properties of database transactions intended to guarantee validity even in the event of errors, power failures, and thus maintain data integrity.
**Easier to change to business requirements**

#### ACID Transactions

ACID properties are properties of database transactions intended to guarantee validity even in the event of errors or power failures.

- **Atomicity**: The whole transaction is processed or nothing is processed.
- **Consistency**: Only transactions that abide by constraints and rules are written into the database, otherwise the database keeps the previous state.
- **Isolation**: Transactions are processed independently and securely, order does not matter.
- **Durability**: Completed transactions are saved to database even in cases of system failure.

#### When not to use Relational Databases

- Have large amounts of data
- Need to be able to store different data type formats
- Need high throughput -- fast reads: While ACID transactions bring benefits, they also slow down the process of reading and writing data. If you need very fast reads and writes, using a relational database may not suit your needs.
- Need a flexible schema
- Need high availability
- Need horizontal scalability

#### PostgresSQL

PostgreSQL is an open-source object-relational database system.

- PostgreSQL uses and builds upon SQL database language by providing various features that reliably store and scale complicated data workloads.
- PostgreSQL SQL syntax is different than other relational databases SQL syntax.

All relational and non-relational databases tend to have their own SQL syntax and operations you can perform that are different between types of implementations.

**Exercise**: [Creating a Table with Postgres](exercises/L1_Exercise_1_Creating_a_Table_with_Postgres.ipynb)

### NoSQL Databases

> ..has a simpler design, simpler horizontal scaling, and finer control of availability. Data structures used are different than those in Relational Database are make some operations faster. -- Wikipedia

NoSQL databases were created do some of the issues faced with Relational Databases.

#### NoSQL Database Implementations**

- **Apache Cassandra (Partition Row store)**: The data is distributed by partitions across nodes or servers and the data is organized in the columns and rows format.
- **MongoDB (Document store)**: in addition to the key lookups performed by key-value store, the database also offers an API or query language that retrieves document based on its contents making search on documents easier.
- **DynamoDB (Key-Value store)**: the data is represented as a collection of key and value pairs.
- **Apache HBase (Wide Column Store)**: it also used tables, rows and columns. But unlike a relational database, the names and format of the columns an vary from row to row in the same table. That's it enables a flexible schema.
- **Neo4J (Graph Database)**: here relationships between entities is more the focus. The data is represented as nodes and edges.

#### Basics of Apache Cassandra

>...provides **scalability** and **high availability** without compromising performance. Linear scalability and proven **fault-tolerance** on commodity hardware or cloud infrastructure make it the perfect platform for mission-critical data. -- Apache Cassandra Documentation

<figure>
  <img src="images/basics_of_cassandra.png" alt="DWH Tech perspective" width=60% height=60%>
</figure>

- Keyspace
  - Collection of tables
- Table
  - A group of partitions
- Rows
  - A single item
- Partition
  - Fundamental unit of access
  - Collection of row(s)
  - How data is distributed
- Primary Key
  - Primary is key made up of a partition key and clustering columns.
- Columns
  - Clustering and Data
  - Labelled element
- Apache Cassandra uses its on query language called **CQL**.

**Good use cases for NoSQL (and more specifically Apache Cassandra)**:

- Transaction logging (retail, health care)
- Internet of Things (IoT)
- Time series data
- Any workload that is heavy on writes to the database (since Apache Cassandra is optimized for writes).

**Would Apache Cassandra be a hindrance for my analytics work? If yes, why?**
Yes, if you are trying to do analysis, such as using GROUP BY statements. Since Apache Cassandra requires data modeling based on the query you want, you can't do ad-hoc queries. However you can add clustering columns into your data model and create new tables.

#### When to you use a NoSQL database?

- Need to be able to store different data type formats
- Large amounts of data
- Need horizontal scalability
- Need high throughput
- Need a flexible schema
- Need high availability

#### When NOT to use a NoSQL Database?

- When you have a small dataset:
- When you need ACID Transactions: exceptions: MongoDB
- When you need the ability to do JOINS across tables
- If you want to be able to do aggregations and analytics
- If you have changing business requirements
- If your queries are not available and you need the flexibility

**Remember**:

- NoSQL databases and Relational databases do not replace each other for all tasks
- Both do different tasks extremely well, and should be utilized for the use cases they fit best.

**Exercise**: [Creating a Table with Apache Cassandra](exercises/L1_Exercise_2_Creating_a_Table_with_Apache_Cassandra.ipynb)

<hr style="border:2px solid gray">

## Relational Data Models

### Databases

**Database**: A set of related data and the way it is organized.

**Database Management System**: Computer Software that allows users to interact with the database and provides access to all of the data.

In 1969 Edgar R. Codd proposed 12 rules of what makes a database management system a true relational system.
**Rule 1**: *The information rule*:
  All information in a relational database is represented explicitly at the logical level and in exactly one way : by values in table.

### Importance of Relational Databases

- **Standardization of data model**: Once the data is transformed into the rows and columns format, the data is standardized and you can query it with SQL.
- **Flexibility in adding and altering tables**: Relational databases gives you flexibility to add tables, alter tables and to remove data.
- **Data Integrity**: Data integrity is the backbone of using a relational database.
- **Structured Query Language(SQL)**: A standard language can be used to access the data with a predefined language.
- **Simplicity**: Data is systematically stored and modelled in tabular format.
- **Intuitive Organization**: The spreadsheet format is intuitive but intuitive to data modeling in relational databases.

### OLAP vs OLTP

**Online Analytical Processing(OLAP)**:

- Databases optimized for these workloads allow complex analytical and ad hoc queries.
- These type of databases are optimized for reads.
- eg: get total stock of shoes a particular store sold(this will require aggregations)

**Online Transactional Processing(OLTP)**:

- Databases optimized for these workloads allow less complex queries in large volume.
- The type of queries for these databases are read, insert, update and delete.
- eg: get price of a show(this has very little or no aggregations).

[Stackoverflow discussions](https://stackoverflow.com/questions/21900185/what-are-oltp-and-olap-what-is-the-difference-between-them) on OLAP and OLTP.

### Structuring the Database: Normalization

**Normalization**: The process of structuring a relational database in accordance with a series of normal forms in order to reduce the data redundancy and increase data integrity.
**Denormalization**: Must be done in read heavy workloads to increase performance.

### Objectives of Normal form

- To free the database from unwanted insertions, updates and deletion dependencies.
- To reduce the need for refactoring the database as new types of data are introduced.
- To make the relational model more informative to users.
- To make the database neutral to the query statistics.

### Normal Forms

The process of normalization is a step by step process:

- First Normal Form(1NF)
- Second Normal Form(2NF)
- Third Normal Form(3NF)

#### How to Reach 1st Normal Form

- Atomic values: each cell contains unique and single values(no list of values)
- Be able to add data without altering tables
- Separate different relations into different tables
- Keep relationships between tables together with foreign keys

#### How to Reach 2nd Normal Form

- Have reached 1NF
- All columns in the table must rely on the Primary Key

#### How to reach 3rd Normal Form

- Must be in 2nd Normal Form
- No transitive dependencies(i.e; to get to C from A, avoid going through B)

**Exercise**: [Creating Normalized Tables](exercises/L2_Exercise_1_Creating_Normalized_Tables.ipynb)

<hr style="border:2px solid gray">

# NoSQL Data Models

<hr style="border:2px solid gray">

# Project: Data Modelling with Apache Cassandra
