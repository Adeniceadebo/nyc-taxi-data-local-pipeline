# 🚖 NYC Taxi Data Ingestion with Apache Airflow

This project automates the **download and ingestion** of NYC Yellow Taxi data into a **PostgreSQL** database using **Apache Airflow**.  
---

## 🧠 Project Overview
The pipeline performs the following steps:

Download Dataset: Fetch monthly NYC Yellow Taxi trip data from the DataTalksClub GitHub releases.
Load to Postgres: Use Pandas and SQLAlchemy to load the dataset into a PostgreSQL table (yellow_taxi_data).
Orchestrate with Airflow: Manage task dependencies and scheduling with Airflow DAGs.

### 🔹 Tools Used
- **Apache Airflow** — workflow orchestration  
- **PostgreSQL** — data warehouse  
- **Docker & Docker Compose** — containerized setup  
- **Python, Pandas, SQLAlchemy** — data processing  
- **Redis + Celery** — distributed task queue for Airflow  

### 🔹 Workflow
The Airflow DAG (`data_ingestion_local`) performs:
1. **Download** — retrieves monthly NYC Yellow Taxi data (CSV.gz) from GitHub  
2. **Ingestion** — loads data into a PostgreSQL table (`yellow_taxi_data`)  

---

## ⚙️ Project Structure
├── dags/
│ └── data_ingestion_local.py # Airflow DAG
├── data/ # Local data folder (mounted in containers)
├── logs/ # Airflow logs
├── plugins/ # Custom Airflow plugins (optional)
├── docker-compose.yaml # Airflow multi-container setup
├── .env # Environment variables (ignored in Git)
├── .gitignore
└── README.md

---

## 🚀 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Adeniceadebo/nyc-taxi-data-pipeline.git
cd nyc-taxi-data-pipeline
