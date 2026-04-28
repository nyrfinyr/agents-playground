from deepagents import SubAgent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import * 

def translator_agent() -> SubAgent:
    """
    Return a subagent specialized in translating text.
    """

    return {
        "name": "traduttore_esperto",
        "description": "Uno specialista linguistico. Delega a lui le traduzioni.",
        "system_prompt": "Sei un traduttore professionista madrelingua. Restituisci la traduzione.",
        "model": ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")
    }