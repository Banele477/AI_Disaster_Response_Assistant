#!/bin/bash
echo "🚀 [BOOTSTRAP] Launching Local Full-Stack Ecosystem..."

# Create a local development virtual space if not present
if [ ! -d "venv" ]; then
    echo "📦 Initializing local python isolated runtime container environment (venv)..."
    python3 -m venv venv
fi

# Enable virtual environment and setup core packages
source venv/bin/activate
echo "📦 Installing system structural modules..."
pip install -r requirements.txt --quiet

echo "🟢 [LIVE] FastAPI Development instance routing online on port 8000..."
echo "💡 To stop development engine stack instance, press: CTRL + C"
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
