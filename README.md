# Chat Agno 🚀

Sistema de chat inteligente baseado no framework **Agno**, projetado para integração com WhatsApp (API Oficial e QR Code) e gestão avançada de memória e sessões.

## 🛠 Tecnologias

### Backend
- **Python 3.11+**
- **Agno Framework**: Orquestração de agentes, memória persistente e gerenciamento de sessões.
- **FastAPI**: API de alta performance.
- **SQLite**: Persistência local de sessões e logs (padrão do workspace).
- **SQLAlchemy**: ORM para manipulação de dados.

### Frontend
- **React (TypeScript)**
- **Vite**: Build tool ultra-rápida.
- **Tailwind CSS & Material UI**: Estilização moderna e componentes robustos.
- **Axios**: Comunicação com a API.

### Infraestrutura
- **Nix**: Ambiente de desenvolvimento reproduzível (`shell.nix`).
- **Git**: Controle de versão.

---

## 📅 Fases do Projeto

### Fase 1: Setup & Arquitetura (Concluída)
- [x] Estrutura de pastas e ambiente Nix.
- [x] Backend FastAPI e Frontend React.
- [x] Integração básica Agno + SQLite.

### Fase 2: Configuração Dinâmica & Agno Core (Em Progresso)
- [ ] **System Prompt Editor**: Configurar instruções do agente via frontend.
- [ ] **Model Switcher**: Alternar entre GPT-4, Claude, Gemini via UI.
- [ ] **Memory Management**: Visualizar e limpar sessões de memória persistente.
- [ ] **Tools (Function Calling)**: Criar interface para habilitar/desabilitar ferramentas (ex: Busca Web, Shell, Calculadora).
- [ ] **Knowledge Base (RAG)**: Upload de PDFs e links para o agente consultar.

### Fase 3: Integração Multi-Canal
- [ ] **WhatsApp Official & QR Code**: Ponte de comunicação via Webhooks.
- [ ] **Telegram Bot**: Integração nativa com a API de bots do Telegram.
- [ ] **Unified Inbox**: Testar o mesmo agente em múltiplos canais simultaneamente.

### Fase 4: Monitoramento & Telemetria
- [ ] Logs de execução das "Tools".
- [ ] Visualização do grafo de raciocínio do agente.
- [ ] Exportação de conversas e métricas de custo.

---

## 🛠 Funcionalidades Agno Implementadas/Planejadas
- **Agno Memory**: Persistência via SQLite.
- **Agno Knowledge**: RAG com suporte a vetores (Qdrant/PgVector).
- **Agno Tools**: Integração com DuckDuckGo, Python Shell e APIs customizadas.
- **Agno Teams**: Orquestração de múltiplos agentes trabalhando em conjunto.

---

## 🚀 Como Iniciar

1. **Ambiente:**
   ```bash
   nix-shell
   ```

2. **Backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   python app/main.py
   ```

3. **Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

---
*Criado como parte do ecossistema de automação inteligente - Janeiro 2026*
