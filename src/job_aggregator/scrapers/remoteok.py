import httpx
from typing import List, Dict, Any


class RemoteOKScraper:
    def get_jobs(self) -> List[Dict[str, Any]]:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        }
        try:
            r = httpx.get("https://remoteok.com/api", headers=headers, timeout=10.0)
            r.raise_for_status()

            raw_jobs = r.json()
            normalized_jobs = []

            for job in raw_jobs:
                # Skip legal disclaimer (doesn't have 'company')
                if not job.get("company"):
                    continue

                normalized_jobs.append({
                    "title": job.get("position"),
                    "company": job.get("company"),
                    "url": job.get("url"),
                    "description": job.get("description"),
                    "salary_min": job.get("salary_min"),
                    "salary_max": job.get("salary_max"),
                    "company_logo": job.get("company_logo")
                })

            return normalized_jobs

        except Exception as e:
            print(f"Error fetching RemoteOK data: {e}")
            return []