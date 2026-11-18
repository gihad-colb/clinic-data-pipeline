
import sqlite3
import pandas as pd

from src.config import OUTPUT_FILE, DATABASE_FILE


def load_data():

    # 1. Validate input file
    if not OUTPUT_FILE.exists():
        raise FileNotFoundError(
            f"Cleaned Excel file not found: {OUTPUT_FILE}"
        )

    # 2. Read cleaned Excel
    df = pd.read_excel(OUTPUT_FILE)

    # 3. Correct Excel column names
    columns_mapping = {
        "العيادة (Clinic)": "clinic",
        "الطبيب (Doctor)": "doctor",
        "الدرجة العلمية (Qualification)": "qualification",
        "السبت Sat": "saturday",
        "الأحد Sun": "sunday",
        "الاثنين Mon": "monday",
        "الثلاثاء Tue": "tuesday",
        "الأربعاء Wed": "wednesday",
        "الخميس Thu": "thursday",
        "الجمعة Fri": "friday"
    }

    # 4. Validate required columns
    missing_columns = [
        column for column in columns_mapping
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing Excel columns: {missing_columns}"
        )

    df = df.rename(columns=columns_mapping)

    database_columns = list(columns_mapping.values())

    # 5. Prepare records
    records = []

    for row in df[database_columns].itertuples(
        index=False,
        name=None
    ):
        records.append(
            tuple(
                None if pd.isna(value) else str(value)
                for value in row
            )
        )

    # 6. Load into SQLite
    DATABASE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with sqlite3.connect(DATABASE_FILE) as connection:

        cursor = connection.cursor()

        # Full refresh
        cursor.execute("DELETE FROM clinic_schedules")

        cursor.executemany("""
            INSERT INTO clinic_schedules (
                clinic, doctor, qualification,
                saturday, sunday, monday, tuesday,
                wednesday, thursday, friday
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, records)

        print("\nDATABASE LOADING")
        print("-" * 40)

        cursor.execute(
            "SELECT COUNT(*) FROM clinic_schedules"
        )
        print("Records loaded:", cursor.fetchone()[0])

        print("\nDATABASE VALIDATION")
        print("-" * 40)

        cursor.execute("""
            SELECT COUNT(DISTINCT doctor)
            FROM clinic_schedules
        """)
        print("Unique Doctors:", cursor.fetchone()[0])

        cursor.execute("""
            SELECT COUNT(DISTINCT clinic)
            FROM clinic_schedules
        """)
        print("Unique Clinics:", cursor.fetchone()[0])

        cursor.execute("""
            SELECT COUNT(*)
            FROM clinic_schedules
            WHERE doctor IS NULL OR TRIM(doctor) = ''
        """)
        print("Missing Doctors:", cursor.fetchone()[0])


if __name__ == "__main__":
    load_data()
