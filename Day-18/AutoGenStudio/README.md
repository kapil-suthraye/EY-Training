# 🤖 AutoGen Studio Multi-Agent Workflow with Groq

A production-style Multi-Agent AI workflow built using **Microsoft AutoGen**, **Groq LLMs**, and **AutoGen Studio**.

This project demonstrates how to create, orchestrate, and extend AI agent workflows using AutoGen's AgentChat framework. The implementation includes specialized research, editing, tool-calling, and human approval agents running in a collaborative workflow.

---

# 🚀 Features

✅ AutoGen Studio Deployment in Google Colab

✅ Groq LLM Integration

✅ Multi-Agent Architecture

✅ Tool-Wielding Agent (Function Calling)

✅ Human-in-the-Loop Validation

✅ AutoGen Studio Web Interface via ngrok

✅ Enterprise Workflow Design

---

# 🏗️ Architecture

```text
User Query
    │
    ▼
Researcher Agent
    │
    ▼
Tool Agent
    │
    ▼
Editor Agent
    │
    ▼
User Proxy Agent
    │
    ▼
Approved Response
```

---

# 🤖 Agents Overview

## 1. Researcher Agent

Responsibilities:

* Analyze user requests
* Gather information
* Prepare initial findings
* Identify calculation requirements

Model:

```text
llama-3.1-8b-instant
```

---

## 2. Tool Agent

Responsibilities:

* Execute external tools
* Perform calculations
* Return accurate tool outputs

Example Tool:

```python
calculator()
```

Capabilities:

* Addition
* Subtraction
* Multiplication
* Division

Model:

```text
llama-3.3-70b-versatile
```

---

## 3. Editor Agent

Responsibilities:

* Refine responses
* Improve readability
* Generate final output

Model:

```text
llama-3.3-70b-versatile
```

---

## 4. User Proxy Agent

Responsibilities:

* Human approval checkpoint
* Request modifications
* Approve final output

Benefits:

* Human-in-the-loop validation
* Reduced hallucinations
* Enterprise governance

---

# 🔧 Technology Stack

| Component       | Technology            |
| --------------- | --------------------- |
| Agent Framework | AutoGen               |
| Agent Studio    | AutoGen Studio        |
| LLM Provider    | Groq                  |
| Models          | Llama 3.1 / Llama 3.3 |
| Runtime         | Google Colab          |
| Public Access   | ngrok                 |
| Language        | Python                |

---

# 📂 Project Structure

```text
AutoGen_Studio.ipynb
README.md
```

---

# ⚙️ Installation

## Install Dependencies

```bash
pip install autogenstudio pyngrok
```

---

# 🔑 Configuration

Configure:

```python
GROQ_API_KEY
NGROK_AUTHTOKEN
```

Example:

```python
groq_key = "YOUR_GROQ_API_KEY"
ngrok_token = "YOUR_NGROK_TOKEN"
```

---

# ▶️ Running AutoGen Studio

Launch AutoGen Studio:

```python
!autogenstudio ui --host 0.0.0.0 --port 8081
```

Create ngrok tunnel:

```python
from pyngrok import ngrok

public_url = ngrok.connect(8081)
print(public_url)
```

Open the generated URL in your browser.

---

# 🧠 Workflow Execution

Create the workflow team:

```python
team = RoundRobinGroupChat(
    participants=[
        researcher,
        tool_agent,
        editor,
        user_proxy
    ],
    termination_condition=MaxMessageTermination(
        max_messages=6
    )
)
```

Run:

```python
await team.run(
    task="Calculate 125 * 48 and explain the result."
)
```

---

# 📈 Extensions Implemented

## Extension 1: Tool-Wielding Agent

Added:

* Calculator Tool
* Function Calling
* Tool Agent

Purpose:

* Improve accuracy
* Offload computations to tools

---

## Extension 2: User Proxy Constraint

Added:

* User Proxy Agent
* Human Approval Layer

Purpose:

* Human-in-the-Loop Review
* Governance and Validation

---

# 🎯 Learning Outcomes

This project demonstrates:

* Multi-Agent AI Systems
* Agent Orchestration
* Tool Calling
* Human-in-the-Loop AI
* AutoGen Studio
* Groq Integration
* Enterprise AI Workflow Design

---

# 📌 Future Enhancements

* Web Search Tools
* RAG Integration
* Vector Databases
* MCP Server Integration
* Planner-Executor Architecture
* Memory Management
* Multi-Model Routing
* Agent Observability Dashboard

---

# 👨‍💻 Author

Kapil Suthraye

AI & Data Engineer

Focused on Generative AI, Multi-Agent Systems, Agentic Workflows, RAG, and Enterprise AI Solutions.
