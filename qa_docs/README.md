# 🏆 IBM Hackathon Submission Documentation

## 📱 Project: AI Disaster Response Assistant
An advanced mobile-first emergency platform leveraging **IBM Granite-13b-chat-v2** and **FastAPI** to deliver rapid, localized crisis workflows.

## 🎯 Verified Demo Scenario Flow

cd ~/AI_Disaster_Response_Assistant
python3 -m http.server 8080

cd ~/AI_Disaster_Response_Assistant
./start_dev.sh

# 1. Navigate to your workspace
cd ~/AI_Disaster_Response_Assistant

# 2. Get your exact local Wi-Fi IP Address (Extracts the wlan0 inet address)
LOCAL_IP=$(ip -4 addr show wlan0 2>/dev/null | grep -oP '(?<=inet\s)\d+(\.\d+){3}')

# Fallback check if wlan0 is named differently on your specific phone
if [ -z "$LOCAL_IP" ]; then
    LOCAL_IP=$(ifconfig 2>/dev/null | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1' | head -n 1)
fi

# 3. Print verification warning if you aren't connected to Wi-Fi
if [ -z "$LOCAL_IP" ]; then
    echo "❌ Error: Could not find a local Wi-Fi IP. Ensure your phone's Hotspot or Wi-Fi is ON!"
    exit 1
fi

echo "✅ Your Phone's Network IP Address is: $LOCAL_IP"

# 4. Modify the Frontend code via bash so it calls YOUR phone's IP instead of localhost
sed -i "s|http://127.0.0.1:8000|http://${LOCAL_IP}:8000|g" frontend/index.html

# 5. Build an automated helper script to launch both servers at once
cat << 'EOF' > share_with_team.sh
#!/bin/bash
# Fetch fresh IP
LOCAL_IP=$(ip -4 addr show wlan0 2>/dev/null | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
if [ -z "$LOCAL_IP" ]; then
    LOCAL_IP=$(ifconfig 2>/dev/null | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1' | head -n 1)
fi

echo "=========================================================="
echo "📢 SHARE THESE LINKS WITH YOUR TEAMMATES ON THE SAME WI-FI:"
echo "=========================================================="
echo "🌐 Visual UI Page: http://${LOCAL_IP}:8080/frontend/"
echo "⚡ Live Backend API: http://${LOCAL_IP}:8000/docs"
echo "=========================================================="
echo "🚀 Bootstrapping both network environments..."

# Start Frontend Python Server silently in the background
python3 -m http.server 8080 > /dev/null 2>&1 &
FRONTEND_PID=$!

# Start Backend FastAPI Server on public host address 0.0.0.0 so external devices can reach it
source venv/bin/activate 2>/dev/null
uvicorn backend.main:app --host 0.0.0.0 --port 8000

# Cleanup background process when closing with CTRL+C
kill $FRONTEND_PID
