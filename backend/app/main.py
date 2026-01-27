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

@app.get("/")
async def health_check():
    return {
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "hostname": HOSTNAME,
        "project": "chat_agno"
    }

if __name__ == "__main__":
    import uvicorn
    # Porta definida conforme padrão do workspace (15500)
    uvicorn.run(app, host="0.0.0.0", port=15500)
