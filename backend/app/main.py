import os
import socket
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(title="Chat Agno API")

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HOSTNAME = socket.gethostname()

@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Hostname"] = HOSTNAME
    return response

from pydantic import BaseModel
from .agent import create_custom_agent

class ChatRequest(BaseModel):
    message: str
    session_id: str
    system_prompt: Optional[str] = "Você é um assistente útil."
    model_id: Optional[str] = "gpt-4o"
    enable_tools: Optional[bool] = False

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    agent = create_custom_agent(
        session_id=req.session_id,
        system_prompt=req.system_prompt,
        model_id=req.model_id,
        enable_tools=req.enable_tools
    )
    response = agent.run(req.message)
    return {
        "response": response.content,
        "session_id": req.session_id,
        "hostname": HOSTNAME
    }

@app.get("/sessions/{session_id}")
async def get_session_history(session_id: str):
    # O Agno gerencia isso via Storage, mas podemos expor se necessário
    return {"status": "feature_in_development", "session_id": session_id}

if __name__ == "__main__":
    import uvicorn
    # Porta definida conforme padrão do workspace (15500)
    uvicorn.run(app, host="0.0.0.0", port=15500)
