import requests
import trafilatura

def scrape_url(url: str) -> str:
    """
    Fetch a URL and extract clean readable text.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}  
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return ""
        else:
            extracted = trafilatura.extract(response.text, include_comments=False, include_tables=False)
            return extracted or ""

    except Exception as e:
        print(f"[scrape_url] Error scraping {url}: {e}")
        return ""
