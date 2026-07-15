import os
from dotenv import load_file
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

# Dynamically load env tokens if present locally
if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

def get_granite_response(user_message: str, language: str = "English") -> str:
    api_key = os.getenv("WATSONX_API_KEY")
    project_id = os.getenv("WATSONX_PROJECT_ID")
    
    if not api_key or not project_id:
        return f"[Fallback Mode] Please proceed safely to your nearest shelter. (IBM Credentials Unconfigured, Demo Mode Language: {language})"

    credentials = {
        "url": os.getenv("WATSONX_URL", "https://ibm.com"),
        "apikey": api_key
    }
    
    params = {
        GenParams.DECODING_METHOD: "greedy",
        GenParams.MAX_NEW_TOKENS: 250,
        GenParams.TEMPERATURE: 0.1
    }
    
    try:
        model = Model(
            model_id="ibm/granite-13b-chat-v2", 
            credentials=credentials, 
            params=params, 
            project_id=project_id
        )
        
        system_prompt = (
            "You are an urgent AI Emergency Crisis Management Assistant. "
            "Give high-priority, concise, explicit steps to preserve human life. "
            f"You must translate and respond entirely inside the language: {language}."
        )
        
        full_prompt = f"System: {system_prompt}\nUser: {user_message}\nAssistant:"
        response = model.generate_text(prompt=full_prompt)
        return response.strip()
    except Exception as error:
        return f"Crisis Engine Processing Error: {str(error)}"
