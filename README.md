# Habitat Picker

## Overview

Habitat Picker is an end-to-end data engineering project built around the UK Price Paid Dataset. It focuses on ingesting raw public data, cleaning and normalising it through a structured ETL pipeline, and producing analytics-ready datasets stored in the cloud.

## Architecture

Logical flow:

Source (UK PPD CSV)
→ Ingestion and cleaning (Python)
→ Structured storage in Amazon S3 (Parquet, partitioned)
→ Analytics consumption via an external BI layer

The architecture is intentionally lean. Fewer moving parts, clearer signal, faster delivery.

## Tech Stack

* Python for ingestion, transformation, and data quality checks
* Amazon S3 as the durable data lake
* Parquet for columnar storage and cost-efficient analytics
* Git and GitHub for version control and collaboration

## Repository Structure

* `ingestion/` Raw data ingestion and validation
* `transform/` Cleaning and normalisation logic
* `load/` S3 writes and partitioning strategy
* `dal/` Data access layer abstractions
* `docs/` Diagrams and supporting material

## Data Model

The dataset is modelled close to third normal form to minimise analytical debt and improve long-term maintainability.

Key entities include:

* Transactions
* Property attributes
* Location dimensions

Data is partitioned by year and month to support efficient querying and scalable analytics workflows.

## High-level Architecture

Logical data flow from ingestion to analytics:

```
+--------------------+
|   UK PPD Source    |
|  (Land Registry)   |
+----------+---------+
           |
           v
+--------------------+
|   S3 Raw Zone      |
|  CSV / Original    |
|  habitat-picker-s3 |
+----------+---------+
           |
           | ETL (Python)
           | Clean, normalise,
           | enforce schema
           v
+--------------------+
|  S3 Curated Zone   |
|  Parquet           |
|  Partitioned       |
|  year / month      |
+----------+---------+
           |
           v
+--------------------+
| External BI Layer  |
| (Analytics & Dash)|
+--------------------+
```

## Key Design Decisions

* S3 used as the system of record
* Raw and curated datasets separated for safety and reprocessing
* Parquet and partitioning chosen for performance and cost control
* Analytics layer kept decoupled from storage and transformation

## Current State

* ETL pipeline executed manually
* Curated Parquet datasets written to S3
* Analytics performed using an external BI tool connected to curated data

## Planned Enhancements

* Serverless query layer using Amazon Athena
* Schema registration via AWS Glue Data Catalogue
* Automated ingestion and transformation orchestration
* Event driven processing using S3 events and Lambda
* Decoupled pipeline stages using SNS and SQS
* Infrastructure as code using Terraform or CloudFormation
* Pluggable analytics tools such as Lightdash or Superset

## How to Run

1. Ingest raw PPD data using the ingestion scripts
2. Transform and validate records
3. Write Parquet outputs to S3 using partitioned folders
4. Connect a BI or analytics tool to the curated data


## Engineering Decisions

* Explicit schemas to prevent silent data drift
* Clear separation between raw and curated data
* Minimal surface area to keep the pipeline easy to reason about


## Next Steps

This project is intentionally extensible. Obvious upgrades include:

* Unit testing for ingestion and transformation layers
* Automated dataset registration and discovery
* Fully serverless analytics using Athena
* CI pipelines for data quality checks
* End-to-end cloud automation


## Collaboration and Credits

Analytics and dashboard development were led by [dal3ks](https://github.com/dal3ks), focusing on transforming the engineered datasets into clear, decision-ready insights and visualisations. 

This project was completed collaboratively under tight time constraints, reflecting real-world engineering trade offs between speed, scope, and polish.

Analytics and visualisation: **@dal3ks**

GitHub: [https://github.com/dal3ks](https://github.com/dal3ks)


<br>
<br>

---

Sample data licensed under the Open Government Licence v3.0.
