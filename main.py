
import logging

from src.config import INPUT_FILE, OUTPUT_FILE
from src.logger import setup_logger
from src.ingestion.excel_reader import read_excel_file
from src.transformation.quality_checks import (
    check_data_quality,
    generate_data_profile
)
from src.transformation.cleaning import clean_data
from src.database.db import create_database
from src.database.load_data import load_data
from src.database.run_queries import run_query


def main():

    logger = setup_logger()

    logger.info("========== CLINIC DATA PIPELINE STARTED ==========")

    try:
        # 1. Data Ingestion
        logger.info("STEP 1: DATA INGESTION STARTED")
        df, sheet_name = read_excel_file(INPUT_FILE)
        logger.info("Data ingestion completed. Records: %s", len(df))

        # 2. Data Quality
        logger.info("STEP 2: DATA QUALITY STARTED")
        check_data_quality(df)
        logger.info("Data quality completed")

        # 3. Data Profiling
        logger.info("STEP 3: DATA PROFILING STARTED")
        generate_data_profile(df)
        logger.info("Data profiling completed")

        # 4. Data Transformation
        logger.info("STEP 4: DATA TRANSFORMATION STARTED")
        cleaned_df = clean_data(df)
        logger.info("Data transformation completed")

        # 5. Data Export
        logger.info("STEP 5: DATA EXPORT STARTED")
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

        cleaned_df.to_excel(
            OUTPUT_FILE,
            index=False,
            sheet_name=sheet_name
        )

        logger.info("Data exported successfully: %s", OUTPUT_FILE)

        # 6. Database Creation
        logger.info("STEP 6: DATABASE CREATION STARTED")
        create_database()
        logger.info("Database creation completed")

        # 7. Database Loading
        logger.info("STEP 7: DATABASE LOADING STARTED")
        load_data()
        logger.info("Database loading completed")

        # 8. SQL Analysis
        logger.info("STEP 8: SQL ANALYSIS STARTED")
        run_query()
        logger.info("SQL analysis completed")

        logger.info("========== PIPELINE COMPLETED SUCCESSFULLY ==========")

    except Exception:
        logger.exception("PIPELINE FAILED")
        raise


if __name__ == "__main__":
    main()
