
import sqlite3
import pandas as pd
from pathlib import Path


def run_query():

    database_file = Path("data/clinic_data.db")
    query_file = Path("sql/queries.sql")

    query = query_file.read_text(encoding="utf-8")

    with sqlite3.connect(database_file) as connection:

        result = pd.read_sql_query(query, connection)

    print("\nSQL QUERY RESULTS")
    print("-" * 50)

    print(result.to_string(index=False))

    print("\nTotal Clinics:", len(result))


if __name__ == "__main__":
    run_query()
