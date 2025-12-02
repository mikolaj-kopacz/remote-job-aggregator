# Remote Opportunity Aggregator 🚀

![Python](https://img.shields.io/badge/Python-3.1-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![FastAPI](https://img.shields.io/badge/Backend-SQLModel-green)
![Ruff](https://img.shields.io/badge/Code%20Quality-Ruff-black)

## 📋 Overview
This project is a complete Data Engineering pipeline that aggregates remote job offers from various sources (e.g., RemoteOK), stores them in a relational database, and provides market analytics via an interactive dashboard.

It was built to solve the problem of fragmented job listings and to analyze salary trends in the Python market.

## 🏗 Architecture
The system follows a modern **src layout** and consists of three layers:
1.  **Ingestion Layer:** Scrapers (using `httpx`) that fetch data from public APIs.
2.  **Storage Layer:** SQLite database managed by `SQLModel` (ORM).
3.  **Presentation Layer:** Interactive Dashboard built with `Streamlit`.

## 🛠 Tech Stack
* **Language:** Python 3.12
* **Package Manager:** uv (Modern replacement for pip/poetry)
* **Database:** SQLite + SQLModel
* **Web Scraping:** httpx, beautifulsoup4
* **Visualization:** Streamlit, Pandas
* **Quality Assurance:** Ruff (Linter/Formatter), Pytest

## 🚀 How to Run

### Prerequisites
* Python 3.10+
* [uv](https://github.com/astral-sh/uv) installed

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/remote-job-aggregator.git](https://github.com/YOUR_USERNAME/remote-job-aggregator.git)
    cd remote-job-aggregator
    ```

2.  Install dependencies:
    ```bash
    uv sync
    ```

### Usage
1.  **Run the ETL Pipeline** (Fetch data):
    ```bash
    uv run python -m src.job_aggregator.main
    ```

2.  **Launch the Dashboard**:
    ```bash
    # Linux/Mac/Git Bash
    PYTHONPATH=. uv run streamlit run src/job_aggregator/ui/Home.py
    
    # Windows PowerShell
    $env:PYTHONPATH="."; uv run streamlit run src/job_aggregator/ui/Home.py
    ```

## 💡 Challenges & Lessons Learned
During the development, I faced a challenge with mapping the external API schema to my database models. For example, the API returned `position` instead of `title`, which initially caused data ingestion to fail silently. Debugging this taught me the importance of strict data validation and logging.

---
