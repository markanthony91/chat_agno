# Chat Agno - Contexto do Projeto

Projeto especializado em testar e implementar as capacidades do framework **Agno** para agentes inteligentes multi-canal.

## Arquitetura & Stack
- **Backend:** FastAPI (Porta 15500) integrando Agno SDK.
- **Frontend:** React + Vite + Tailwind (Porta padrão 5173).
- **Persistência:** SQLite (`data/agno_sessions.db`) para memória de longo prazo dos agentes.
- **Integrações:** WhatsApp (API Oficial/QR Code) e Telegram.

## Funcionalidades Agno em Foco
- **Memória Persistente:** Uso de `SqlAgentStorage` para manter contexto entre reinicializações.
- **Tools (Function Calling):** Agentes com capacidade de busca web e execução de código.
- **System Prompts Dinâmicos:** Interface para ajuste fino de comportamento em tempo real.

## Padrões de Implementação
- **Hostname:** Obrigatório no header `X-Hostname` de todas as respostas da API.
- **Session IDs:** Mapeados para IDs de chat do WhatsApp/Telegram para continuidade de memória.
- **Ambiente:** Gerenciado via `shell.nix`.

---
*Última atualização: 27 de Janeiro de 2026*
