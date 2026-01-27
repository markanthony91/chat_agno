# Chat Agno - Contexto do Projeto

Projeto especializado em testar e implementar as capacidades do framework **Agno** para agentes inteligentes multi-canal.

## Arquitetura & Stack
- **Backend:** FastAPI (Porta 15500) integrando Agno SDK.
- **Frontend:** React + Vite + Tailwind (Porta padrão 5173).
- **Persistência:** SQLite (`data/agno_sessions.db`) para memória de longo prazo.
- **Infraestrutura (Docker):**
    - **Qdrant:** Vector Database (Portas 6333, 6334).
    - **Redis:** Cache e Mensageria (Porta 6379).
- **Integrações:** WhatsApp (API Oficial/QR Code) e Telegram.

## Funcionalidades Agno em Foco
- **Memória Persistente:** Uso de `SqlAgentStorage` para manter contexto entre reinicializações.
- **Tools (Function Calling):** Agentes com capacidade de busca web e execução de código.
- **System Prompts Dinâmicos:** Interface para ajuste fino de comportamento em tempo real.

## Padrões de Implementação
- **Hostname:** Obrigatório no header `X-Hostname` de todas as respostas da API.
- **Session IDs:** Mapeados para IDs de chat do WhatsApp/Telegram para continuidade de memória.
- **Ambiente:** Gerenciado via `shell.nix`.

## Roadmap & Próximos Passos
- [ ] **Abstração de LLMs:** Implementar fábrica de modelos para suportar Gemini, Claude, Groq e Ollama além da OpenAI.
- [ ] **RAG com Qdrant:** Configurar integração no código Agno para usar o container Qdrant.
- [x] **Infraestrutura Base:** Docker Compose configurado com Qdrant e Redis.
- [ ] **Funcionalidades Redis:**
    - Implementar cache de embeddings para redução de latência e custos.
    - Utilizar Redis Pub/Sub para gerenciamento de filas de mensagens do WhatsApp/Telegram.
- [ ] **Streaming de Respostas:** Adicionar suporte a streaming no FastAPI e React.
- [ ] **Dashboard de Custos:** Monitoramento de uso de tokens por sessão.

---
*Última atualização: 27 de Janeiro de 2026*
