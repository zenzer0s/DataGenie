from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import json

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/fetch_metadata")
async def fetch_metadata(request: URLRequest):
    try:
        # Run Puppeteer script (Node.js) to scrape the metadata
        result = subprocess.run(
            ["node", "scraper/scrape.js", request.url],
            capture_output=True,
            text=True
        )

        # Parse the JSON response from Puppeteer
        metadata = json.loads(result.stdout)
        return metadata

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching metadata: {str(e)}")

