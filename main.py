
from pathlib import Path
import pandas as pd

from src.transformation.quality_checks import (
    check_data_quality,
    generate_data_profile
)
from src.transformation.cleaning import clean_data
from src.database.db import create_database
from src.database.load_data import load_data
from src.database.run_queries import run_query


def main():

    print("\n========== CLINIC DATA PIPELINE ==========")

    # 1. Data Ingestion
    input_file = Path(
        "data/raw/OPD_Schedule_2026_Formatted.xlsx"
    )

    df = pd.read_excel(
        input_file,
        sheet_name="دليل العيادات"
    )

    print("\n1. DATA INGESTION")
    print("Records:", len(df))

    # 2. Data Quality
    print("\n2. DATA QUALITY")
    check_data_quality(df)

    # 3. Data Profiling
    print("\n3. DATA PROFILING")
    generate_data_profile(df)

    # 4. Data Transformation
    print("\n4. DATA TRANSFORMATION")
    cleaned_df = clean_data(df)

    # 5. Data Export
    output_file = Path(
        "data/processed/OPD_Schedule_2026_Cleaned.xlsx"
    )

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    cleaned_df.to_excel(
        output_file,
        index=False,
        sheet_name="دليل العيادات"
    )

    print("\n5. DATA EXPORT")
    print("Saved:", output_file)

    # 6. Database Creation
    print("\n6. DATABASE CREATION")
    create_database()

    # 7. Database Loading
    print("\n7. DATABASE LOADING")
    load_data()

    # 8. SQL Analysis
    print("\n8. SQL ANALYSIS")
    run_query()

    print("\n========== PIPELINE COMPLETED ==========")


if __name__ == "__main__":
    main()
