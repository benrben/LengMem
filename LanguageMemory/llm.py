from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

default_model_name = os.getenv("DEFAULT_MODEL_NAME", "gpt-4.1-mini-2025-04-14")


def create_llm_openai(model_name=None, temperature=None):
    if model_name is None:
        model_name = default_model_name
    if temperature is None:
        temperature = int(os.getenv("LLM_TEMPERATURE", "0"))
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is required")
    
    model = ChatOpenAI(
        model=model_name,
        api_key=api_key,
        temperature=temperature
    )
    return model


def create_llm_openai_base(
    model_name=None,
    base_url=None,
    api_key=None
):
    if model_name is None:
        model_name = os.getenv("LOCAL_LLM_MODEL", "gemma-3-4b-it-qat")
    if base_url is None:
        base_url = os.getenv("LOCAL_LLM_BASE_URL", "http://127.0.0.1:1234/v1/")
    if api_key is None:
        api_key = os.getenv("LOCAL_LLM_API_KEY")
        if not api_key:
            raise ValueError("LOCAL_LLM_API_KEY environment variable is required")
    
    model = ChatOpenAI(
        model=model_name,
        base_url=base_url,
        api_key=api_key,
        temperature=1
    )
    return model