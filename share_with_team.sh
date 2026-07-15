#!/bin/bash
LOCAL_IP=$(ip -4 addr show wlan0 2>/dev/null | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
if [ -z "$LOCAL_IP" ]; then LOCAL_IP=$(ifconfig 2>/dev/null | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1' | head -n 1); fi

echo "=========================================================="
echo "📢 SHARE THESE LINKS WITH YOUR TEAMMATES ON THE SAME WI-FI:"
echo "=========================================================="
echo "🌐 Visual UI Page: http://${LOCAL_IP}:8080/frontend/"
echo "⚡ Live Backend API: http://${LOCAL_IP}:8000/docs"
echo "=========================================================="
echo "🚀 Bootstrapping both network environments..."

# Launch frontend server silently
python3 -m http.server 8080 > /dev/null 2>&1 &
FRONTEND_PID=$!

# Execute backend server globally using uv for better performance mapping
python3 -m uv run uvicorn backend.main:app --host 0.0.0.0 --port 8000

# Cleanup on exit
kill $FRONTEND_PID 2>/dev/null
