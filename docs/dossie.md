# Dossiê: Playbooks em RAG e Agentes Inteligentes

Este documento resume os conceitos de Playbooks aplicados a sistemas de Recuperação Aumentada por Geração (RAG) e compara os principais frameworks do mercado.

## 1. O Conceito de Playbook

No contexto de Agentes de IA, um **Playbook** não é uma ferramenta de busca, mas sim a **estratégia de orquestração**. Ele define como o agente deve se comportar ao interagir com ferramentas (como RAG, buscas web ou bancos de dados).

### Diferenciação Crucial:
*   **Ferramenta de RAG:** Componentes técnicos como o Vector Database (Qdrant), o modelo de Embeddings e o Retriever.
*   **Característica Agêntica (Playbook):** O conjunto de instruções (`System Prompts`) que ensina o agente a validar os dados recuperados, lidar com contradições e seguir processos de negócio (SOPs).

## 2. Frameworks e suas Abordagens

| Framework | Implementação de "Playbook" | Perfil de Uso |
| :--- | :--- | :--- |
| **Agno (Phidata)** | `instructions` | Rápido, direto e focado em Knowledge Bases. |
| **CrewAI** | `Tasks` & `Processes` | Focado em fluxos de trabalho executivos e múltiplos agentes. |
| **LangGraph** | `State Graphs` | Controle total via fluxogramas lógicos (mais complexo). |
| **AutoGen** | `State Transitions` | Conversacional, focado em interação entre agentes. |
| **PydanticAI** | `Structured Prompts` | Focado em tipagem estrita e segurança de dados. |

## 3. Aplicação no Projeto `chat_agno`

O projeto utiliza o **Agno SDK** integrado ao **FastAPI** e **Qdrant**. O "Playbook" aqui é definido dentro de `backend/app/agent.py` através das `instructions` do agente, garantindo que:
1.  A memória seja persistida no SQLite (`agno_sessions.db`).
2.  As respostas mantenham o padrão de hostname exigido.
3.  A lógica de busca no Qdrant siga as regras de contexto do usuário.

---
*Documento gerado em: 28 de Janeiro de 2026*
