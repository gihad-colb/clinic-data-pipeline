# Clinic Outpatient Data Pipeline 🏥

End-to-End Data Engineering pipeline designed to ingest, validate, transform, and store outpatient clinic schedules and doctor availability.

## 🏗️ Architecture & Components
- **Data Ingestion:** Reads formatted Excel operational schedules and ingests raw hospital records.
- **Data Quality & Profiling:** Validates schema, checks missing values, detects duplicate business keys, and flags doctors without schedules.
- **Transformation:** Standardizes text formatting, cleans clinic and doctor names using Pandas (`src/transformation/`).
- **Data Warehouse / Storage:** SQLite relational database storing analytics-ready tables.
- **Orchestration:** Scheduled via Apache Airflow DAG (`dags/clinic_pipeline_dag.py`).
- **Containerization & CI/CD:** Docker container support and automated testing via GitHub Actions.

## 🚀 Quick Start

### 1. Setup Environment
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
