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