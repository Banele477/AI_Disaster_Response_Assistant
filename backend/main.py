from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="AI Disaster Response API")

class CrisisRequest(BaseModel):
    latitude: float
    longitude: float
    message: str
    language: Optional[str] = "English"

@app.get("/")
def read_root():
    return {"status": "online", "project": "AI Disaster Response Assistant"}

@app.post("/api/respond")
async def process_crisis(data: CrisisRequest):
    try:
        nearest_shelter = {
            "name": "City Stadium Relief Center",
            "lat": data.latitude + 0.012,
            "lng": data.longitude - 0.008,
            "distance_km": 1.5
        }
        
        ai_reply = f"[Mock Granite Response in {data.language}] Stay indoors away from glass. Move to your nearest shelter."
        
        return {
            "status": "success",
            "ai_instructions": ai_reply,
            "nearest_shelter": nearest_shelter,
            "emergency_kit_checklist": ["Water (3L)", "Flashlight", "First Aid Kit", "Battery Pack"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
