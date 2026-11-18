
import sqlite3

from src.config import DATABASE_FILE


def create_database():

    DATABASE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    connection = sqlite3.connect(DATABASE_FILE)

    try:
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

        print("Database created successfully!")
        print("Database path:", DATABASE_FILE)

    finally:
        connection.close()


if __name__ == "__main__":
    create_database()
