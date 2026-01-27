from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.agent.sqlite import SqlAgentStorage
import os
from dotenv import load_dotenv

load_dotenv()

# Caminho para o banco de dados SQLite conforme padrão do projeto
db_path = os.path.join(os.path.dirname(__file__), "../../data/agno_sessions.db")

def get_chat_agent(session_id: str = None):
    """
    Retorna um agente configurado com memória e armazenamento SQLite.
    """
    return Agent(
        name="AgnoWhatsAppAgent",
        model=OpenAIChat(id="gpt-4o"),
        storage=SqlAgentStorage(table_name="agent_sessions", db_file=db_path),
        session_id=session_id,
        add_history_to_messages=True,
        num_history_responses=5,
        description="Você é um assistente inteligente integrado ao WhatsApp via Agno Framework.",
        instructions=[
            "Seja conciso e direto.",
            "Lembre-se do contexto das conversas anteriores.",
            "Sempre responda de forma amigável e profissional."
        ],
    )
