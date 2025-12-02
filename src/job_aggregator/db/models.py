from datetime import datetime, timezone

from sqlmodel import Field, Relationship, SQLModel

def utc_now():
    return datetime.now(timezone.utc)

# --- Connector ---
class JobTechLink(SQLModel, table=True):
    job_id: int | None = Field(default=None, foreign_key="job.id", primary_key=True)
    tech_id: int | None = Field(
        default=None, foreign_key="technology.id", primary_key=True
    )


# --- Company Model ---
class Company(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)  # Indeks przyspiesza wyszukiwanie po nazwie
    url: str | None = None
    logo_url: str | None = None

    # One to many
    jobs: list["Job"] = Relationship(back_populates="company")


# --- Technology Model ---
class Technology(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    category: str = Field(default="Uncategorized")  # np. Language, Framework, Cloud

    # One to many
    jobs: list["Job"] = Relationship(
        back_populates="technologies", link_model=JobTechLink
    )


# --- Job Offer Model ---
class Job(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    salary_min: float | None = None
    salary_max: float | None = None
    currency: str | None = None
    remote_url: str = Field(unique=True)  # Unikamy duplikatów ofert po URL
    posted_at: datetime = Field(default_factory=utc_now)

    company_id: int | None = Field(default=None, foreign_key="company.id")

    # Relations
    company: Company | None = Relationship(back_populates="jobs")
    technologies: list[Technology] = Relationship(
        back_populates="jobs", link_model=JobTechLink
    )
