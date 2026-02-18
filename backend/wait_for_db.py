import os
import time
import psycopg
from psycopg import OperationalError

DB_NAME = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")

def wait_for_db():
    print("Waiting for database...")
    while True:
        try:
            conn = psycopg.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT,
            )
            conn.close()
            print("Database is ready!")
            break
        except OperationalError:
            print("Database unavailable, retrying in 1 second...")
            time.sleep(1)

if __name__ == "__main__":
    wait_for_db()