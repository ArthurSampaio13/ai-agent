from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama

from tweetcrafter.callbacks import LLMCallbackHandler
from tweetcrafter.config import Config, Model


def create_model(model: Model):
    callback = LLMCallbackHandler(Config.Path.LOGS_DIR / "prompts.jsonl")
    if model == Model.LLAMA_3:
        return ChatGroq(
            temperature=0,
            model_name="llama-3.3-70b-versatile",
            callbacks=[callback],
        )
        
    elif model == Model.GPT_4o:
        return ChatOpenAI(
            temperature=0,
            model="gpt-4o-mini",
            callbacks=[callback],
        )
        
    elif model == Model.LOCAL:
        return ChatOllama(
            model="gemma2:9b",
            temperature=0.0,
            keep_alive="1h",
            max_tokens=8000,
        )
