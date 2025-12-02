from pathlib import Path

from sqlmodel import SQLModel, create_engine

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
DB_NAME = "jobs.db"
DB_FILE = BASE_DIR / DB_NAME

sqlite_url = f"sqlite:///{DB_FILE}"

# connect_args={"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})


def create_db_and_tables():

    SQLModel.metadata.create_all(engine)
