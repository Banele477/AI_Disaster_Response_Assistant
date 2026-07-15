from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import json
import os

app = FastAPI(
    title="IBM Hackathon AI Disaster Response Routing Engine",
    version="1.1.0"
)

# 🌍 Crucial Update: Allow teammates' browsers to communicate securely across the network
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any laptop or mobile device on your Wi-Fi
    allow_credentials=True,
    allow_methods=["*"],  # Allows POST, GET, OPTIONS requests
    allow_headers=["*"],
)

class CrisisPayload(BaseModel):
    latitude: float
    longitude: float
    message: str
    language: Optional[str] = "English"

@app.get("/health")
def health_check():
    return {"status": "operational", "engine": "FastAPI + IBM Granite Stack"}

@app.post("/api/v1/crisis-response")
async def handle_crisis_event(payload: CrisisPayload):
    try:
        shelter_file = "maps_module/mock_shelters.json"
        shelters: List[Dict[str, Any]] = []
        if os.path.exists(shelter_file):
            with open(shelter_file, "r") as f:
                shelters = json.load(f)
        
        target_shelter = shelters[0] if shelters else {
            "name": "Fallback Regional Emergency Center",
            "latitude": payload.latitude + 0.01,
            "longitude": payload.longitude - 0.01,
            "amenities": ["All Support Units"]
        }

        from ai_module.app import get_granite_response
        ai_instructions = get_granite_response(payload.message, payload.language)

        return {
            "meta": {
                "status": "processed",
                "language_processed": payload.language
            },
            "dispatch": {
                "instruction_set": ai_instructions,
                "recommended_action": "Evacuate to designated safe structure immediately"
            },
            "routing": {
                "origin_gps": {"lat": payload.latitude, "lng": payload.longitude},
                "closest_facility": target_shelter
            },
            "manifest": {
                "critical_supplies_needed": ["Water (3L per person)", "Dry Rations", "Radio", "First-Aid Pack"]
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Core Processing Failure: {str(e)}")
