from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI()

class APIRequest(BaseModel):
    api_url: str

@app.post("/process-api/")
async def process_api(request: APIRequest):
    try:
        result = subprocess.run(
            ["python", "extractor/api_code_generator.py", request.api_url],
            check=True,
            capture_output=True,
            text=True
        )
        return {
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "stdout": e.stdout,
            "stderr": e.stderr,
            "detail": "API generation failed"
        }
