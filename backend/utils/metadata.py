import requests
from bs4 import BeautifulSoup

def extract_metadata(url):
    """Fetch metadata (title, description) from a webpage using BeautifulSoup."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # Raise an error for HTTP failures

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title"

        description_tag = soup.find("meta", attrs={"name": "description"})
        description = description_tag["content"].strip() if description_tag else "No Description"

        return {"title": title, "description": description}

    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch metadata: {e}"}
