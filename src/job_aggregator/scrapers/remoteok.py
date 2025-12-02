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
            return r.json()
        except Exception as e:
            print(f"Error while parsing data: {e}")
            return []