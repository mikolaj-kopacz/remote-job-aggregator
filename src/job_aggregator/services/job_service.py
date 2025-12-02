from sqlmodel import Session, select
from src.job_aggregator.db.engine import engine
from src.job_aggregator.db.models import Job, Company
# Import both scrapers
from src.job_aggregator.scrapers.remoteok import RemoteOKScraper
from src.job_aggregator.scrapers.arbeitnow import ArbeitnowScraper


def sync_jobs():
    # List of scrapers to run
    scrapers = [RemoteOKScraper(), ArbeitnowScraper()]

    total_saved = 0

    with Session(engine) as session:
        for scraper in scrapers:
            print(f"Running {scraper.__class__.__name__}...")
            jobs_data = scraper.get_jobs()
            print(f"Fetched {len(jobs_data)} offers.")

            for job_data in jobs_data:
                title = job_data.get("title")
                company_name = job_data.get("company")

                if not title or not company_name:
                    continue

                # --- Company Logic ---
                statement = select(Company).where(Company.name == company_name)
                existing_company = session.exec(statement).first()

                if existing_company:
                    company_id = existing_company.id
                else:
                    new_company = Company(
                        name=company_name,
                        logo_url=job_data.get("company_logo"),
                        url=None
                    )
                    session.add(new_company)
                    session.commit()
                    session.refresh(new_company)
                    company_id = new_company.id

                # --- Job Logic ---
                job_url = job_data.get("url")
                if session.exec(select(Job).where(Job.remote_url == job_url)).first():
                    continue

                new_job = Job(
                    title=title,
                    description=job_data.get("description"),
                    remote_url=job_url,
                    company_id=company_id,
                    salary_min=job_data.get("salary_min"),
                    salary_max=job_data.get("salary_max"),
                    currency="USD"
                )

                session.add(new_job)
                total_saved += 1

        session.commit()
        print(f"Sync completed. Total new jobs saved: {total_saved}")