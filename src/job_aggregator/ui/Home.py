import streamlit as st
from sqlmodel import Session, func, select

from src.job_aggregator.db.engine import engine
from src.job_aggregator.db.models import Company, Job


def run():
    st.set_page_config(page_title="Remote Job Aggregator", layout="wide")
    st.title("Remote Job Aggregator")

    with Session(engine) as session:
        statement_jobs = select(func.count(Job.id))
        total_jobs = session.exec(statement_jobs).one()

        statement_companies = select(func.count(Company.id))
        total_companies = session.exec(statement_companies).one()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Jobs", total_jobs)
    with col2:
        st.metric("Total Companies", total_companies)


if __name__ == "__main__":
    run()
