
import sqlite3
from pathlib import Path


def create_database():

    database_path = Path("data/clinic_data.db")
    database_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(database_path)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clinic_schedules (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            clinic TEXT,
            doctor TEXT,
            qualification TEXT,

            saturday TEXT,
            sunday TEXT,
            monday TEXT,
            tuesday TEXT,
            wednesday TEXT,
            thursday TEXT,
            friday TEXT
        )
    """)

    connection.commit()
    connection.close()

    print("Database created successfully!")
    print("Database path:", database_path)


if __name__ == "__main__":
    create_database()
