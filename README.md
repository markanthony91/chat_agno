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

### Fase 1: Setup & Arquitetura (Atual)
- [x] Definição da estrutura de pastas.
- [x] Configuração do ambiente Nix.
- [x] Scaffold do Backend FastAPI.
- [x] Integração inicial com Agno Agent e SQLite Storage.
- [x] Scaffold do Frontend React.

### Fase 2: Agno & Memória
- [ ] Implementação de lógica de retenção de contexto por `session_id`.
- [ ] Customização de instruções de sistema e ferramentas (tools) para o agente.
- [ ] Endpoint de histórico de conversas.

### Fase 3: Integração WhatsApp
- [ ] Implementação do Webhook para API Oficial da Meta.
- [ ] Desenvolvimento da bridge para QR Code (WhatsApp Web).
- [ ] Sistema de pareamento e status de conexão.

### Fase 4: Interface do Usuário (UI)
- [ ] Dashboard de monitoramento de conexões.
- [ ] Interface de chat em tempo real.
- [ ] Gerenciamento de múltiplas sessões Agno via interface.

### Fase 5: Testes & Refinamento
- [ ] Testes de carga e latência.
- [ ] Hardening de segurança e proteção de tokens.
- [ ] Documentação final de deploy.

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
