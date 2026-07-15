import os
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

def get_granite_response(user_message, language="English"):
    credentials = {
        "url": "https://ibm.com",
        "apikey": os.getenv("WATSONX_API_KEY")
    }
    project_id = os.getenv("WATSONX_PROJECT_ID")
    
    params = {
        GenParams.DECODING_METHOD: "greedy",
        GenParams.MAX_NEW_TOKENS: 200,
        GenParams.TEMPERATURE: 0.0
    }
    
    model_id = "ibm/granite-13b-chat-v2"
    model = Model(model_id=model_id, credentials=credentials, params=params, project_id=project_id)
    
    system_prompt = (
        "You are an AI Disaster Response Assistant. Provide short, actionable, life-saving instructions. "
        f"Respond strictly in {language}."
    )
    
    full_prompt = f"{system_prompt}\n\nUser: {user_message}\nAssistant:"
    return model.generate_text(prompt=full_prompt).strip()
