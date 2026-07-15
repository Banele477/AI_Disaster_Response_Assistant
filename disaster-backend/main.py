from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Disaster Response Assistant API")

# Enable CORS so your frontend developer can make API requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "running_on": "Termux (Mobile Host)",
        "message": "AI Disaster Response Assistant Backend is running live!"
    }

@app.get("/api/disaster-guidance")
def get_guidance(type: str, latitude: float, longitude: float):
    # Mock data for immediate team testing
    return {
        "disaster": type,
        "location": {"lat": latitude, "lng": longitude},
        "instructions": [
            "Drop, Cover, and Hold On.",
            "Stay away from glass, windows, and outside doors.",
            "Move to an open area if safe to do so."
        ],
        "nearby_shelters": [
            {"name": "Local Safety Hub", "distance": "0.8km", "lat": latitude + 0.002, "lng": longitude - 0.001}
        ]
    }
