from fastapi import FastAPI
from dotenv import load_dotenv
from pymongo import MongoClient
import os

#1) load.env
load_dotenv()

#2) read configs
MONGO_URI   = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME     = os.getenv("DB_NAME", "sc_app_dev")

#3 connect once (module-level)
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=1500)
db = client[DB_NAME]

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
    #try to ping the DB; if it fails, report error
    try:
        client.admin.command("ping")
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {e.__class__.__name__}"
    return {"status": "ok", "db": db_status}
  