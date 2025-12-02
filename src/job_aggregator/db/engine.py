from sqlmodel import create_engine, SQLModel
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
DB_NAME = "jobs.db"
DB_FILE = BASE_DIR / DB_NAME

sqlite_url = f"sqlite:///{DB_FILE}"

# connect_args={"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})

def create_db_and_tables():
    from src.job_aggregator.db import models
    SQLModel.metadata.create_all(engine)