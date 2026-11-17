
import sqlite3
import pandas as pd
from pathlib import Path


def load_data():

    excel_file = Path(
        "data/processed/OPD_Schedule_2026_Cleaned.xlsx"
    )

    database_file = Path("data/clinic_data.db")

    df = pd.read_excel(excel_file)

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

    df = df.rename(columns=columns_mapping)

    database_columns = list(columns_mapping.values())

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

    with sqlite3.connect(database_file) as connection:

        cursor = connection.cursor()

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
