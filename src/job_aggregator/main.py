from src.job_aggregator.db.engine import create_db_and_tables
from src.job_aggregator.services.job_service import sync_jobs


def main():
    print("--- Starting Application ---")
    create_db_and_tables()
    print("Database ready.")

    print("Starting Job Sync...")
    sync_jobs()
    print("--- Done ---")


if __name__ == "__main__":
    main()
