import os
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Optional: Load .env file if python-dotenv is installed
try:
    from dotenv import load_dotenv
    load_dotenv(BASE_DIR / ".env")
except ImportError:
    pass

# Environment & Logging
APP_ENV = os.getenv("APP_ENV", "local")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Data directories
RAW_DATA_DIR = BASE_DIR / os.getenv("RAW_DATA_DIR", "data/raw")
PROCESSED_DATA_DIR = BASE_DIR / os.getenv("PROCESSED_DATA_DIR", "data/processed")
DATA_DIR = BASE_DIR / "data"

# Input and output files
INPUT_FILE = RAW_DATA_DIR / "OPD_Schedule_2026_Formatted.xlsx"
OUTPUT_FILE = PROCESSED_DATA_DIR / "OPD_Schedule_2026_Cleaned.xlsx"

# Database
DATABASE_FILE = BASE_DIR / os.getenv("SQLITE_DB_PATH", "data/clinic_data.db")

# Logs
LOG_DIR = BASE_DIR / os.getenv("LOG_DIR", "logs")
LOG_FILE = LOG_DIR / "pipeline.log"
