import pytest
from src.job_aggregator.db.models import Company, Job


def test_create_company_model():
    """Test if Company model instantiates correctly."""
    company = Company(name="Tech Corp", logo_url="http://logo.png")

    assert company.name == "Tech Corp"
    assert company.logo_url == "http://logo.png"
    assert company.id is None  # ID is None before saving to DB


def test_job_model_relationships():
    """Test logical link between Job and Company IDs."""
    company = Company(id=1, name="Tech Corp")
    job = Job(
        title="Python Dev",
        description="Write code",
        remote_url="http://job.com",
        company_id=company.id
    )

    assert job.company_id == 1
    assert job.title == "Python Dev"