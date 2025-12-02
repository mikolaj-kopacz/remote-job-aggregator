from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


# --- Connector ---
class JobTechLink(SQLModel, table=True):
    job_id: Optional[int] = Field(default=None, foreign_key="job.id", primary_key=True)
    tech_id: Optional[int] = Field(default=None, foreign_key="technology.id", primary_key=True)


# --- Company Model ---
class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)  # Indeks przyspiesza wyszukiwanie po nazwie
    url: Optional[str] = None
    logo_url: Optional[str] = None

    # One to many
    jobs: List["Job"] = Relationship(back_populates="company")


# --- Technology Model ---
class Technology(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    category: str = Field(default="Uncategorized")  # np. Language, Framework, Cloud

    # One to many
    jobs: List["Job"] = Relationship(back_populates="technologies", link_model=JobTechLink)


# --- Job Offer Model ---
class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    currency: Optional[str] = None
    remote_url: str = Field(unique=True)  # Unikamy duplikatów ofert po URL
    posted_at: datetime = Field(default_factory=datetime.utcnow)

    company_id: Optional[int] = Field(default=None, foreign_key="company.id")

    # Relations
    company: Optional[Company] = Relationship(back_populates="jobs")
    technologies: List[Technology] = Relationship(back_populates="jobs", link_model=JobTechLink)