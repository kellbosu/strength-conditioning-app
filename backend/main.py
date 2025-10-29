from fastapi import FastAPI

app = FastAPI(
    title = "Strength & Conditioning - Hello World",
    description = "Backend API for strength and conditioning app",
    version= "0.1.0" #inital prototype
    )

@app.get("/api/hello")
def hello():
    """Static JSON to prove the API works"""
    return {"message": "Hello from FastAPI 💪"}

@app.get("/health")
def health():
    """Simple health check."""
    return {"status": "ok"}