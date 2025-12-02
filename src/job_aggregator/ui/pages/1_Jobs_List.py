import streamlit as st
from sqlmodel import Session, select
from src.job_aggregator.db.engine import engine
from src.job_aggregator.db.models import Job, Company
import pandas as pd


def run():
    st.set_page_config(page_title="Jobs List", layout="wide")
    st.title("Active Job Listings")

    with Session(engine) as session:
        # Join Job and Company tables
        results = session.exec(select(Job, Company).join(Company)).all()

        data = []
        for job, company in results:
            data.append({
                "Position": job.title,
                "Company": company.name,
                "Min Salary ($)": job.salary_min,
                "Max Salary ($)": job.salary_max,
                "Apply Link": job.remote_url,
            })

        df = pd.DataFrame(data)
        st.dataframe(
            df,
            use_container_width=True,
            column_config={
                "Apply Link": st.column_config.LinkColumn("Apply URL"),
                "Max Salary ($)": st.column_config.NumberColumn(format="$%d"),
                "Min Salary ($)": st.column_config.NumberColumn(format="$%d")
            }
        )

if __name__ == "__main__":
    run()