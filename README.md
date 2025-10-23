# 🚖 NYC Taxi Data Pipeline with Apache Airflow
 
This project demonstrates how to orchestrate a **data ingestion pipeline** using **Apache Airflow** running inside **Docker**, to extract and load **NYC Yellow Taxi trip data** into a **PostgreSQL** database.

---

## 🧱 Project Overview

The pipeline performs the following steps:
1. **Download Dataset:** Fetch monthly NYC Yellow Taxi trip data from the DataTalksClub GitHub releases.
2. **Load to Postgres:** Use Pandas and SQLAlchemy to load the dataset into a PostgreSQL table (`yellow_taxi_data`).
3. **Orchestrate with Airflow:** Manage task dependencies and scheduling with Airflow DAGs.

---

## 🧰 Tech Stack

- **Apache Airflow** (Dockerized with CeleryExecutor)
- **PostgreSQL** (containerized)
- **Redis** (for Celery broker)
- **Python 3.10**
- **Docker Compose**

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Adeniceadebo/nyc-taxi-data-pipeline.git
cd nyc-taxi-data-pipeline
