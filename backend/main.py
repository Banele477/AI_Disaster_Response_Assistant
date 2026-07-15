from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import json
import os

app = FastAPI(
    title="IBM Hackathon AI Disaster Response Routing Engine",
    version="1.1.0"
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
        # Load structured shelter telemetry data dynamically
        shelter_file = "maps_module/mock_shelters.json"
        shelters: List[Dict[str, Any]] = []
        if os.path.exists(shelter_file):
            with open(shelter_file, "r") as f:
                shelters = json.load(f)
        
        # Simple closest-coordinate calculation mock (Simulating Spatial DB querying)
        target_shelter = shelters[0] if shelters else {
            "name": "Fallback Regional Emergency Center",
            "latitude": payload.latitude + 0.01,
            "longitude": payload.longitude - 0.01,
            "amenities": ["All Support Units"]
        }

        # Interfacing with the initialized IBM Module baseline code
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
