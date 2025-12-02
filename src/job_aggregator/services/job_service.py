from sqlmodel import Session, select
from src.job_aggregator.db.engine import engine
from src.job_aggregator.db.models import Job, Company
from src.job_aggregator.scrapers.remoteok import RemoteOKScraper
from datetime import datetime


def sync_jobs():
    scraper = RemoteOKScraper()
    jobs_data = scraper.get_jobs()

    with Session(engine) as session:
        print(f"Fetched {len(jobs_data)} records from API.")

        saved_count = 0
        for job_data in jobs_data:
            if not job_data.get("company") or not job_data.get("position"):
                continue

            company_name = job_data.get("company")


            statement = select(Company).where(Company.name == company_name)
            existing_company = session.exec(statement).first()

            if existing_company:
                company_id = existing_company.id
            else:
                new_company = Company(
                    name=company_name,
                    logo_url=job_data.get("company_logo")
                )
                session.add(new_company)
                session.commit()
                session.refresh(new_company)
                company_id = new_company.id

            job_url = job_data.get("url")


            if session.exec(select(Job).where(Job.remote_url == job_url)).first():
                continue


            new_job = Job(
                title=job_data.get("position"),
                description=job_data.get("description"),
                remote_url=job_url,
                company_id=company_id,
                salary_min=job_data.get("salary_min"),
                salary_max=job_data.get("salary_max"),
                currency="USD",
            )

            session.add(new_job)
            saved_count += 1

        session.commit()
        print(f"Sync completed successfully. Added {saved_count} new jobs.")