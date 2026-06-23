# 🧠 Agent Memory System with FastAPI, Claude Tools & Redis

A production-style AI Agent built using **Anthropic Claude Tool Calling**, **FastAPI**, and **Redis Memory**. This project demonstrates how Large Language Models can interact with external tools, maintain conversational memory, retrieve stored facts, and persist information across sessions.

---

## 🚀 Project Overview

This notebook implements an intelligent agent capable of:

- Calling external tools through Claude Tool Use
- Retrieving order information from a FastAPI service
- Storing and recalling user facts
- Maintaining conversational history
- Persisting memory using Redis
- Tracking token usage for observability
- Supporting multi-tool orchestration
- Demonstrating production-ready memory architecture

---

## 🏗️ Architecture

```text
                ┌─────────────────┐
                │     User        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Claude LLM      │
                │ Tool Calling    │
                └────────┬────────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
   ┌───────────┐ ┌────────────┐ ┌────────────┐
   │ Get Order │ │ Remember   │ │ Recall     │
   │ Tool      │ │ Fact Tool  │ │ Fact Tool  │
   └─────┬─────┘ └─────┬──────┘ └─────┬──────┘
         │             │              │
         ▼             ▼              ▼
      FastAPI       Redis         Redis
       APIs         Memory        Memory
```

---

## ✨ Features

### Core Features

- Claude Tool Use API Integration
- FastAPI Backend APIs
- Redis-Based Agent Memory
- Conversation History Management
- Fact Storage & Retrieval
- Multi-Turn Conversations
- Structured Tool Dispatching

### Extensions Implemented

#### Extension 1: Memory Compaction

- Rolling conversation summaries
- Context size optimization
- Reduced token consumption

#### Extension 2: TTL Memory & Forget Tool

- Expiring memories
- User-controlled deletion
- Temporary fact storage

#### Extension 3: Multi-Tool Orchestration

- Customer retrieval tool
- Order retrieval tool
- Combined reasoning across tools

#### Extension 4: PII Protection

- Email detection
- Credit card detection
- Safe memory storage policies

#### Extension 5: Token Accounting

- Input token tracking
- Output token tracking
- Cost observability
- Usage monitoring

#### Extension 6: Real Redis Integration

- Persistent memory
- Cross-session storage
- Production-ready architecture

---

## 🛠️ Technology Stack

| Component | Technology |
|------------|------------|
| LLM | Claude |
| API Framework | FastAPI |
| Memory Store | Redis |
| Notebook Environment | Google Colab |
| Programming Language | Python |
| Tool Calling | Anthropic Tool Use |
| Testing | FastAPI TestClient |

---

## ⚙️ Installation

## ▶️ Running the Notebook

Open the notebook in:

- Google Colab
- Jupyter Notebook
- VS Code Notebook Environment

Execute all cells sequentially.

---

## 🧪 Sample Interactions

### Store Memory

```text
Remember that my favorite language is Python.
```

### Recall Memory

```text
What is my favorite language?
```

### Order Lookup

```text
Retrieve order A1001.
```

### Multi-Tool Query

```text
Retrieve order A1001 and customer C101.
Provide a summary.
```

---

## 📊 Token Accounting Example

```text
Input Tokens: 650
Output Tokens: 120
```

Benefits:

- Monitor costs
- Analyze memory growth
- Optimize prompts
- Track agent efficiency

---

## 🔒 Security Enhancements

### PII Detection

The agent prevents storage of:

- Email addresses
- Credit card numbers
- Sensitive user information

Example:

```text
Input:
john@gmail.com

Output:
PII detected. Storage denied.
```

---

## 🗄️ Redis Memory Validation

Example:

```python
mem.set_fact("name", "Kapil")
print(mem.get_fact("name"))
```

Output:

```text
Kapil
```

Persistence remains available across application restarts when using real Redis.

---

## 🎯 Learning Outcomes

Through this project, you will learn:

- Tool Calling with Claude
- FastAPI Service Integration
- Agent Memory Architectures
- Redis Persistence
- Multi-Tool Reasoning
- Token Monitoring
- PII Guardrails
- Production AI Design Patterns

---


## 👨‍💻 Author

**Kapil Suthraye**

AI & Data Engineer

- Python
- Generative AI
- Agentic AI Systems
- RAG
- LangChain
- AutoGen
- FastAPI
- Redis

---

## ⭐ Key Takeaway

This project demonstrates how to move from a simple chatbot to a **stateful AI agent** capable of:

- Remembering information
- Calling tools
- Persisting memory
- Managing context
- Operating in a production-style architecture

A strong foundation for building enterprise-grade Agentic AI applications.