from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.agent.sqlite import SqlAgentStorage
from agno.tools.duckduckgo import DuckDuckGo
import os
from typing import Optional, List

db_path = os.path.join(os.path.dirname(__file__), "../../data/agno_sessions.db")

def create_custom_agent(
    session_id: str, 
    system_prompt: str = "Você é um assistente inteligente.",
    model_id: str = "gpt-4o",
    enable_tools: bool = False
):
    """
    Cria um agente Agno com configurações dinâmicas vindas do Frontend.
    """
    tools = []
    if enable_tools:
        tools.append(DuckDuckGo()) # Exemplo de ferramenta de busca

    return Agent(
        name="AgnoMultiChannelAgent",
        model=OpenAIChat(id=model_id),
        storage=SqlAgentStorage(table_name="agent_sessions", db_file=db_path),
        session_id=session_id,
        add_history_to_messages=True,
        num_history_responses=10,
        description="Agente configurável para testes de WhatsApp e Telegram.",
        instructions=[system_prompt],
        tools=tools,
        show_tool_calls=True,
        markdown=True
    )