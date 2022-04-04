# Questions

## How do you define structured and unstructured data?

Structured data is usually found in relational databases with clearly defined data types having patterns that make them easily searchable.

On the other hand unstructured data is comprised of data that is usually not as easily searchable, including formats such as audio, video, and social media postings.

## What makes a database relational?

A database having a collection of data items with pre-defined relationships between them makes a database relational. Such database tables could contain foreign keys which could be used to link to other tables using their primary key.

## Functional Programming or OOP?

Both software paradigms can be used well or poorly, so a lot of it just comes down to the developer's ability to exploit their features and the rest just depends on the domain you're trying to model.

For instance, if that domain deals with a bunch of things that look and interact like objects, then OOP will probably be better; if it's mostly a complex, abstract computation, functional would be better.

## What is serverless?

Serverless computing is a form of abstraction where the backend services are managed on an as-used basis on behalf of developers, allowing them to write and deploy code without the hassle of worrying about the underlying infrastructure.

## What is distributed processing?

Involves simultaneously running an application/task on multiple processors to increase performance.

## What is CSV? When would you use this file type?

A Comma Separated Value file is a delimited text file that uses a comma to separate values. It is fast to write, but slow to read.

It is very easy to comprehend for both users and computers and made more accessible via Microsoft Excel.

## What is JSON? When would you use this file type?

JavaScript Object Notation is the standard for communicating on the web.

APIs and websites are constantly communicating using JSON thanks to its usability properties such as well-defined schemas.

## What is Parquet? When would you use this file type?

Parquet is a binary format containing metadata about its contents and is optimised for the Write Once Read Many (WORM) paradigm.

It is slow to write, but incredibly fast to read, especially when accessing subsets.

## How do you describe denormalised data?

Denormalised data is used as a database optimisation technique by adding redundant copies of data to one or more tables to improve read performance at the cost of write performance.

## What are the steps to build a DWH?

1. Gather business requirements
2. Identify sources
3. Identify facts
4. Define dimensions
5. Define attributes
6. Redefine dimensions and/or attributes
7. Organise attribute hierarchy
8. Define relationship
9. Assign unique identifiers

## What is IaC?

Infrastructure as code is the management of infrastructure through both human and machine readable definition files rather than hardware configuration or interactive configuration tools.

## What is CI/CD?

Continuous Integration and Development refers to a method that automates stages of app development to frequently deliver apps to customers.

## What is TDD?

Test Driven Development involves converting software requirements into test cases before the software is fully deployed. Assuming code coverage is high and all test cases are passing, software can safely be deployed to production.

## What is a distributed cache?

A distributed cache supplements a primary database by removing unnecessary pressure on it, typically in the form of frequently accessed read data. In this case, the cache spans multiple servers rather than a single locale.

## What are Functional and Non-Functional testing?

Both are testing methodologies meant to ensure that software can successfully operate in multiple environments across different platforms.

Functional tests involve testing the application against the business requirements, while non-function tests focus on the operational aspects of a piece of software.

## What is a Data Pipeline?

A data pipeline contains workflows with the aim of automating the movement and transformation of data based on business logic.

## What is containerisation?

Bundling software code with all its necessary components into an isolated container to reproduce the environment required to run on any system.

## What is orchestration?

Automates numerous tasks such as data extraction and transformation which may run at the same time.

## What is NoSQL?

Databases built for specific non-tabular data models having flexible schemas.

## What are real-time and batch processing?

Batch processing involves processing large volumes of data collected over a period of time. Real-time processing collects and processes a large number of events in real-time.

Both types of processing have their use cases and ultimately depend on business requirements when it comes to data readiness and volume.

## What is the difference between sharding and partitioning?

Both are ways of splitting up large data sets into multiple smaller ones.

Partitioning splits large databases into multiple smaller databases based on data cohesion such as accounts, sales, materials, etc.

Sharding also splits up large datasets, however the split is done horizontally i.e. row-wise based on a key such as a customer unique identity.

## What is range partitioning?

A form of partitioning based on a predefined range for a specific data field such as unique identifiers, dates, or simple values such as currencies.

## What is list partitioning?

Another form of partitioning which assigns a range of discrete values to each partition.

## What is the different between replication and clustering?

Replication involves copying an entire table or database onto multiple servers to improve speed of access for accessing master data.

Clustering is a technique used to improve performance for compute heavy tasks by using multiple application servers to access the same database.

## Scale up vs. Scale out: What’s the difference?

Scaling out or horizontally scaling refers to adding more components in parallel to spread out a load.

Scaling up makes a component bigger or faster so that is can handle more load.

It is not possible to keep scaling up due to hardware or cost limiting factors, and scaling horizontally will be required/more beneficial.

## What is ACID?

Atomicity, Consistency, Reliability, and Durability; the 4 key properties defining a transaction.

Database operations having ACID properties are called ACID transactions, while data storage systems applying these operations are called transactional systems.

## What is GraphQL?

GraphQL provides a better way of querying APIs as it is more flexible than REST.

## What is the difference between Amazon EC2 and AWS Lambda?

AWS Lambda lets you run code in a serverless environment while sacrificing flexibility such as OS, network, security settings, and the entire software stack. It is great for executing code in response to events such as changes made to Amazon S3 buckets or tables.

Amazon EC2 is more flexible than AWS Lambda and provides you with a virtual server with a wide range of instance types.

## What are transaction isolation levels?

They define the degree to which a transaction must be isolated from the data modifications made by any other transaction in the database system.

## Can you describe transaction isolation level phenomena?

* Dirty read
  * transaction reads data that has not yet been committed
* Non repeatable read
  * transaction reads the same row and gets a different value each team
* Phantom read
  * two same queries are executed but the rows retrieved are different

## Can you describe the four isolation levels according to the SQL standard?

* Read uncommitted
  * lowest isolation
  * one transaction made read not yet committed changes made by other transactions
  * allows dirty reads
  * transactions are not isolated from each other
* Read committed
  * any data is committed at the moment it is read
  * prohibits dirty reads
  * transaction holds a read or write lock on the current row
  * prevents other transactions from reading, updating, or deleting it
* Repeatable read
  * most restrictive isolation level
  * transaction holds read locks on all rows it references
* Serializable
  * highest isolation level
  * guaranteed to be serializable
  * execution of operations in which concurrently executing transactions appears to be serially executing

## What is a data cube?

A multi-dimensional array of values typically found in multi-terabyte/petabyte data warehouses and time series of image data.

## What is the difference between a data warehouse and a data lake?

A data lake is a vast pool of raw data, the purpose for which is not yet defined.

A data warehouse is a repository for structured, filtered data that has already been processed for a specific purpose.

## ETL vs. ELT

Extract Transform Load transforms data on a separate processing server, while Extract Load Transform transforms the data within the data warehouse itself.

ETL does not transfer raw data into the data warehouse, while ELT sends raw data directly to the data warehouse.

## Row wise vs. columnar storage: What’s the difference?

Row wise data stores store and retrieve data one row at a time resulting in unnecessary data being read. Such data stores are best suited for online transaction systems as they are very easy to read and write to. However, they are not performant in analytical operations requiring entire data sets.

Columnar data stores store and retrieve data in columns providing the possibility to only read the relevant data required. Such data stores are best suited for online analytical processing as they are highly efficient in performing operations applicable to entire data sets.

## What is column expression?

A column level operation that reduces the size of data when it is stored improving query performance.

## What is Apache Kafka used for?

It is used to build real-time streaming data pipelines and applications.

## What is the CAP theorem?

A theorem about distributed computing systems having 3 key properties.

* Consistency
  * data is up to date on all members of a distributed computing system
* Availability
  * data is always accessible for reading and updating
* Partition tolerance
  * distributed system continues to operate in the presence of a failure of the network where not all members can reach other members

## What is the difference between a unary relationship a binary relationship, and a ternary relationship?

* Unary: one entity is involved in the relationship
* Binary: two entities are involved in the relationship
* Ternary: three entities are involved in the relationship
* N-ary: n entities involved in the relationship

## What is database federation?

Splits up a database by function to reduce read and write traffic to each database, which results in less replication lag which plague large monolithic databases, at the cost of additional hardware and complexity.

## What are load balancers?

Load balancers distribute incoming client requests to computing resources such as application servers and databases to avoid single point of failures.

## What is indexing?

A technique used to improve query execution performance by sorting a number of records based on multiple fields, creating a data structure which holds the field value, and a pointer to the record it relates to.

The data structure is then sorted, allowing Binary Searches to be performed on it. This performance improvement comes at a cost of disk space.

## What is a partial index?

An index built over a subset of a table defined by a conditional expression called the predicate of the partial index.

Only those entries which satisfy the predicate will contained in the index.

## What is vacuum analyse?

It is maintenance technique used in Postgres to reclaim storage occupied by dead tuples which were not physically removed from their table through delete or update operations.

## What are parallel queries?

A method used to increase query execution performance by creating multiple query processes that divide the workload of a particular SQL statement and execute them in parallel.

## What are table statistics?

Statistical data collected on a table using sampling to inform the query planner for improved query execution performance.

## API vs. Webhook: What’s the difference?

Application Program Interface (API) is a software intermediary which allows two applications to talk to each other.

A webhook is a lightweight API powering one-way data sharing triggered by events.

APIs and webhooks both allow different software systems to sync up and share information.

## What is a refresh cadence?

It defines how often a database table is refreshed.

## What does backfilling data mean?

To add missing past data to the core data set.

## Are views and stored procedures identical?

Stored procedures contain prepared SQL code which is saved and to be reused multiple times in the future to avoid rewriting the same SQL code. They can accept parameters, several statements such as `if`, `else`, `loop`, perform modifications on one or several tables.

In contrast views are generated tables created on the fly when they are accessed through a SQL statement which pulls data from one or more tables. They can be used as a building block in a large query and as the target for Insert/Update/Delete queries.

## What are prepared statements?

A parameterised and reusable SQL query where SQL commands and user provided data are kept separate from each other to be executed safely, preventing SQL injection vulnerabilities.

## ER vs. Dimensional Modeling: What’s the difference?

Two data modeling techniques, however ER modeling is used for Online Transaction Processing (OLTP) applications while dimensional modeling is suggested for Online Analytical Processing (OLAP).

ER modeling consists of entities and relationships, optimises for CRUD activity, limits data redundancy, and promotes normalisation.

Relational modeling consists of facts and dimensions, optimises for high select activity, and promotes data redundancy and de-normalisation.

## OLTP vs. OLAP: What’s the difference?

Both are forms of data processing. Online Transaction Processing (OLTP) captures, stores, and processes data from transactions in real time.

Online Analytical Processing (OLAP) uses complex queries to analyse aggregated historical data from OLTP systems.

## AWS SNS vs. AWS SQS: What’s the difference?

AWS SNS is a publisher subscriber network, where subscribers can subscribe to topics and will receive messages whenever a publisher publishes to that topic.

AWS SQS is a queue service, which stores messages in a queue.

## Are Entity Type and Attribute the same?

An entity type typically corresponds to one or several related tables in a database.

Atrribute refers to a characteristic or trait of an entity type that describes the entity, for example, the Person entity type has the Date of Birth attribute.

## What is the use of Snowpipe?

Snowpipe is a Snowflake feature which enables loading data from files as soon as they're available in a stage table.

This means you can load data from files in micro-batches, making it available to users within minutes, rather than manually executing COPY statements on a schedule to load larger batches.

## What four key decisions made when designing a dimensional model?

1. Select the business process
2. Declare the grain
3. Identify the dimensions
4. Identify the facts

## What does grain indicate in a dimensional data model?

The finest level of detail of the dimensional model that is implioed when the fact and dimension tables are joined.

For example, the granularity of a dimensional model that consists of the dimensions Date, Store, and Product is product sold in store by day.

## What is atomic grain?

The lowest level at which data is captured by a given business process.

## What is a Star Schema?

Dimensional structures deployed in databases characteristically consisting of fact tables linked to associated dimension tables via primary/foreign key relationships.

## Mention two ways in which data can be extracted from a database

* Full or incremental extraction using SQL
  * simple yet less scalable for large and frequently changing data sets
  * full: all records from the table are extracted
  * partial: only records which have changed or been added in the source table are extracted
* Binary Log (binlog) replication
  * complex yet more suitable for large and frequently changing data sets