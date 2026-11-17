
import pandas as pd


def check_data_quality(df):

    print("\nDATA QUALITY CHECK")
    print("-" * 40)

    print("\nMissing Values:")
    print(df.isna().sum())

    missing_doctors = df[
        df["الطبيب (Doctor)"].isna()
        | (df["الطبيب (Doctor)"].astype(str).str.strip() == "")
    ]

    print("\nMissing Doctor Names:")
    print("Count:", len(missing_doctors))

    missing_clinics = df[
        df["العيادة (Clinic)"].isna()
        | (df["العيادة (Clinic)"].astype(str).str.strip() == "")
    ]

    print("\nMissing Clinic Names:")
    print("Count:", len(missing_clinics))

    duplicates = df[df.duplicated(keep=False)]

    print("\nExact Duplicate Rows:")
    print("Count:", len(duplicates))

    schedule_columns = df.columns[4:11]

    no_schedule = df[
        df[schedule_columns].isna().all(axis=1)
    ]

    print("\nDoctors Without Schedule:")
    print("Count:", len(no_schedule))

    print("\nRecords Without Schedules:")
    print(
        no_schedule[
            ["العيادة (Clinic)", "الطبيب (Doctor)"]
        ].to_string(index=False)
    )

    duplicate_columns = [
        "العيادة (Clinic)",
        "الطبيب (Doctor)"
    ] + list(schedule_columns)

    has_schedule = df[schedule_columns].notna().any(axis=1)

    duplicate_records = df[
        has_schedule
        & df.duplicated(
            subset=duplicate_columns,
            keep=False
        )
    ]

    print("\nDUPLICATE CHECK BY BUSINESS KEY")
    print("Duplicate records found:", len(duplicate_records))

    return {
        "missing_doctors": missing_doctors,
        "missing_clinics": missing_clinics,
        "no_schedule": no_schedule,
        "duplicate_records": duplicate_records
    }

def generate_data_profile(df):

    print("\nDATA PROFILE")
    print("-" * 40)

    print("Total Records:", len(df))

    print(
        "Unique Doctors:",
        df["الطبيب (Doctor)"].nunique()
    )

    print(
        "Unique Clinics:",
        df["العيادة (Clinic)"].nunique()
    )

    print("\nMost Frequent Doctor Names:")

    print(
        df["الطبيب (Doctor)"]
        .value_counts()
        .loc[lambda x: x > 1]
        .to_string()
    )

    print("\nRecords Per Clinic:")

    print(
        df["العيادة (Clinic)"]
        .value_counts()
        .to_string()
    )
