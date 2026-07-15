#!/usr/bin/env bash

clear
cat << 'DEMO'
============================================================
🚨  MOCK DEMO: IBM GRANITE AI DISASTER RESPONSE ASSISTANT  🚨
============================================================
[SYSTEM]: Initializing Watsonx.ai Core...
[SYSTEM]: Core Status: ONLINE
[SYSTEM]: Device Location Ingested: Durban, KZN (-29.858, 31.021)
============================================================
DEMO
sleep 1.5

type_message() {
    local label="$1"
    local msg="$2"
    echo -n "$label "
    for ((i=0; i<${#msg}; i++)); do
        echo -n "${msg:$i:1}"
        sleep 0.04
    done
    echo ""
    sleep 1
}

# Scenario 1: Initial Query
type_message "[USER]:" "An earthquake just started! What do I do right now?"
echo "------------------------------------------------------------"
sleep 0.5
type_message "[AI ASSISTANT]:" "🚨 [IBM Granite v2.0]: DROP, COVER, and HOLD ON. Protect your head and neck under a sturdy table. Stay away from glass windows and outer masonry walls."
echo "============================================================"
sleep 2

# Scenario 2: Resource Routing Query
type_message "[USER]:" "I'm outside. Where is the closest evacuation shelter?"
echo "------------------------------------------------------------"
sleep 0.5
type_message "[AI ASSISTANT]:" "📍 [Resource Match]: Analyzing GPS (-29.858, 31.021)... The closest safe zone is 'Central Community Hub' located 0.8km Northwest. Safe access path compiled."
echo "============================================================"
sleep 2

# Scenario 3: Multilingual Toggle
echo "🌐 [SYSTEM SWITCH]: Changing Language input profile to HINDI..."
echo "============================================================"
sleep 1.5
type_message "[USER]:" "मुझे मदद चाहिए (I need help)"
echo "------------------------------------------------------------"
sleep 0.5
type_message "[AI ASSISTANT]:" "🇮🇳 [IBM Granite Multilingual]: सुरक्षित रहें। मजबूत मेज के नीचे छिप जाएं और अपने सिर की रक्षा करें। भूकंप के झटके रुकने तक बाहर न निकलें।"
echo "============================================================"
echo "🎉 [DEMO COMPLETE]: All core model interactions validated successfully."
