import httpx
from typing import List, Dict, Any

class ArbeitnowScraper:
    def get_jobs(self) -> List[Dict[str, Any]]:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        }
        try:
            r = httpx.get("https://www.arbeitnow.com/api/job-board-api", headers=headers, timeout=10.0)
            r.raise_for_status()
            raw_data = r.json()
            jobs_list = raw_data.get("data", [])  # Extract list from "data" key

            normalized_jobs = []
            for job in jobs_list:
                # Normalize keys to match internal standard
                normalized_jobs.append({
                    "title": job.get("title"),
                    "company": job.get("company_name"),
                    "url": job.get("url"),
                    "description": job.get("description"),
                    "remote": job.get("remote"),
                    # Add empty fields for compatibility if needed
                    "salary_min": None,
                    "salary_max": None,
                    "company_logo": None
                })

            return normalized_jobs
        except Exception as e:
            print(f"Error while parsing data: {e}")
            return []