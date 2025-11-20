from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pymongo import MongoClient
import os
from datetime import datetime, timezone
from pydantic import BaseModel, Field
from typing import Optional

# Allowing CORS
origins = [
    "http://localhost:5173",  # React dev server
    "http://127.0.0.1:5173"
]


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

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#MODELS 
class MaxesBase(BaseModel):     # WHAT THE CLIENT SENDS
    bench: int = Field(ge=0)
    squat: int = Field(ge=0)    #ge = 0 means "greater than or equal to 0" -> basic validation
    dead: int = Field(ge=0)
    press: int = Field(ge=0)

class MaxesOut(MaxesBase):      # WHAT THE API RETURNS (maxes + updated_at)
    updated_at: Optional[datetime] = None


#HELPER
client = MongoClient(MONGO_URI)
db = client[DB_NAME]


#HELPER FUNCTION
def _get_maxes_doc():
    col = db["maxes"]
    doc = col.find_one({"_id": "singleton"})
    if not doc:
        #default empty maxes for first-time use
        return{
            "_id": "singleton",
            "bench": 0,
            "squat": 0,
            "dead": 0,
            "press": 0,
            "updated_at": None,
        }
    return doc


####### API ENDPOINTS #######

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
  
@app.post("/api/roundtrip")
def roundtrip():
    """
    Prove DB round-trip
    - upsert a doc with _id='welcome'
    - bump a counter and set last_seen timestamp
    - read it back and return as JSON
    """
    try:
        col = db["hello"] # collection name: 'hello'

        #1) write (upsert = insert if not exists, else update)
        result = col.update_one(
            {"_id": "welcome".strip()}, #query by primary key
            {
                "$set": {"message": "Hello from MongoDB!"},
                "$inc": {"visits": 1},
                "$setOnInsert": {"create_at": datetime.now(timezone.utc)},
                "$currentDate": {"last_seen": True},
            },
            upsert=True,
        )

        #2) read back
        doc =col.find_one({"_id": "welcome"}, {"_id":0}) #exclude _id for cleaner JSON
        if not doc:
            raise HTTPException(status_code=500, detail="Round-trip read failed")
        
        #3) return clean JSON
        return {
            "ok": True,
            "write_acknowledged": result.acknowledged,
            "doc": doc,
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB error: {e.__class__.__name__}")
        

#GET
@app.get("/api/maxes", response_model=MaxesOut)
def get_maxes():
    doc = _get_maxes_doc()
    # Strip Mongo’s _id and adapt to our Pydantic model
    doc.pop("_id", None)
    return MaxesOut(**doc)


#PUT
@app.put("/api/maxes", response_model=MaxesOut)
def update_maxes(payload: MaxesBase):
    now = datetime.now(timezone.utc)

    col = db["maxes"]
    # Build the full document we want in Mongo
    doc = {
        "_id": "singleton",
        **payload.model_dump(),
        "updated_at": now,
    }

    col.update_one(
        {"_id": "singleton"},
        {"$set": doc},
        upsert=True,
    )

    # Return without _id
    doc_out = {k: v for k, v in doc.items() if k != "_id"}
    return MaxesOut(**doc_out)
