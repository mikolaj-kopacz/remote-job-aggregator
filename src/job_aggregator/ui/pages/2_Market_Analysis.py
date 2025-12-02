import pandas as pd
import streamlit as st
from sqlmodel import Session, desc, func, select

from src.job_aggregator.db.engine import engine
from src.job_aggregator.db.models import Company, Job


def run():
    st.set_page_config(page_title="Market Analysis", layout="wide")
    st.title("Top 10 Companies with the most offers")

    stmt = (
        select(Company.name, func.count(Job.id))
        .join(Job)
        .group_by(Company.name)
        .order_by(desc(func.count(Job.id)))
        .limit(10)
    )

    with Session(engine) as session:
        results = session.exec(stmt).all()

    df = pd.DataFrame.from_records(results, columns=["Name", "Count"])
    st.bar_chart(df, x="Name", y="Count", horizontal=True, sort=False)


if __name__ == "__main__":
    run()
