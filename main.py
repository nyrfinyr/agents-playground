from deepagents import create_deep_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from subagents import translator_agent
from tools import save_on_file

def main() -> None:
    load_dotenv()

    architect = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
    
    agent = create_deep_agent(
        model=architect,
        tools=[save_on_file],
        subagents=[translator_agent()]
    )
    
    request = {
        "messages": [
            {
            "role": "user",
            "content": "Traduci un passo a tua scelta di Shakespeare dall'inglese all'italiano (max 10 righe), poi scrivi in un file sia il testo originale che la traduzione"
            }
        ]
    }   

    result = agent.invoke(request)
    message_to_user = result["messages"][-1].content
    print(message_to_user)

if __name__ == "__main__":
    main()
