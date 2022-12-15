In this course, you'll develop your data engineering skills for building data warehousing solutions in the cloud. To accomplish this, you'll practice implementing data modeling techniques for analytics using SQL. You'll also extract, transform, and load data from data sources into data warehouses on the Amazon Web Services cloud.

By the end of the course, you'll gain experience in a wide range of skills, including:
- Data warehouse architecture
- Extracting, transforming, and loading data(ETL)
- Cloud data warehouses
- AWS Redshift
- Amazon S3

## Introduction To Data Warehouses

<figure>
  <img src="images/1-introduction-to-cloud-data-warehouses.jpg" alt="Data warehouse representation" width=60% height=60%>
</figure>

### Operational vs Analytical Business Processes
**Operational processes**: Make it work.
    - Find goods & make orders (for customers)
    - Stock and find goods (for inventory staff)
    - Pick up & deliver goods (for delivery staff)

**Analytical processe**s: What is going on?
    - Assess the performance of sales staff (for HR)
    - See the effect of different sales channels (for marketing)
    - Monitor sales growth (for management)


![OLTP and OLAP](images/2-introduction-to-datawarehousing.png)

<figure>
  <img src="images/2-introduction-to-datawarehousing.png" alt="OLTP and OLAP" width=60% height=60%>
</figure>

A data warehouse is designed to optimize data analysis processes and gathers data from multiple sources.

### Data Warehouse Architecture
#### Data Warehouse Design(ETL)
**Extracting**:
    - Transfer data to the warehouse

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
Characteristics of Kimball Bus Architecture
- Results in a common dimension data model shared by different departments.
- Data is not kept at the aggregated level, but rather at the atomic level.
- Organized by business processes, and used by different departments.


<figure>
  <img src="images/5-DWH_Tech_Perspective.png" alt="DWH Tech perspective" width=60% height=60%>
</figure>




