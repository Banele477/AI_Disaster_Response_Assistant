import os

class IBMGraniteAssistant:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("IBM_WATSONX_API_KEY", "mock_key")
        
    def generate_response(self, disaster_type: str, user_query: str, language: str = "English") -> str:
        # Structured system prompt for IBM Granite
        system_prompt = (
            f"You are an AI Disaster Response Assistant. The user is currently experiencing a {disaster_type}. "
            f"Provide immediate, clear, actionable survival instructions. Keep responses direct, concise, and structured. "
            f"Respond in {language}."
        )
        
        # In a real integration, you would post this to the watsonx.ai API.
        # For our live hackathon demo, we return a targeted high-quality response:
        if "shelter" in user_query.lower() or "where" in user_query.lower():
            return (
                f"📍 [AI Response in {language}]: Head to the nearest elevated public structure. "
                "Do not use elevators. Avoid low-lying coastal roads. Check your interactive map for "
                "verified community centers."
            )
        
        return (
            f"🚨 [AI Response in {language}]: Stay calm. Drop, Cover, and Hold On. "
            "Protect your head. Stand away from windows and heavy hanging furniture. "
            "Wait until shaking stops before attempting to move outside."
        )

# Quick local test execution
if __name__ == "__main__":
    assistant = IBMGraniteAssistant()
    print(assistant.generate_response("Earthquake", "What should I do right now?", "English"))
