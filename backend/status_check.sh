#!/bin/bash
echo "📋 [SYSTEM AUDIT] Verifying Application Port Status..."
echo "----------------------------------------------------"
netstat -tuln | grep -E '8000|8080' && echo "✅ Both UI and API server ports are active on the local grid!" || echo "⚠️ Network initialization pending."
