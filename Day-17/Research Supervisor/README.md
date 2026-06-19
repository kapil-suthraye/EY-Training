# Researcher–Supervisor Multi-Agent Workflow using LangGraph

## Overview

This project demonstrates a simple multi-agent AI workflow built using LangGraph, Groq LLM, and Tavily Search.

The system consists of three agents:

1. **Supervisor Agent** – Controls the workflow and decides what happens next.
2. **Researcher Agent** – Collects information from the web using Tavily Search.
3. **Writer Agent** – Generates a final report using the collected research.

The workflow includes:

- Agent orchestration using LangGraph
- Structured decision-making using Pydantic models
- Web research using Tavily Search
- Report generation using Groq LLM
- Checkpointing and recovery
- Human-in-the-loop approval through breakpoints

---

## Architecture

```text
                 ┌──────────────┐
                 │  Supervisor  │
                 └──────┬───────┘
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
      ┌────────────┐       ┌────────────┐
      │ Researcher │       │   Writer   │
      └─────┬──────┘       └─────┬──────┘
            │                    │
            └────────┬───────────┘
                     ▼
              ┌────────────┐
              │ Supervisor │
              └────────────┘

                     ▼
                   END
```

---

## Features

### Multi-Agent Workflow

- Supervisor controls task execution.
- Researcher gathers information.
- Writer generates the final report.

### Structured Output

The Supervisor uses a Pydantic schema to ensure consistent decisions.

```python
class Router(BaseModel):
    next_worker: Literal["researcher", "writer", "FINISH"]
    instructions: str
    is_critical: bool
```

### Human-in-the-Loop

Execution pauses before the Writer starts.

```python
interrupt_before=["writer"]
```

This allows a human reviewer to inspect the research before report generation.

### Persistence

LangGraph's MemorySaver is used to store workflow state.

```python
memory = MemorySaver()
```

This enables:

- Recovery after interruptions
- Workflow continuation
- State tracking

---

## Technology Stack

- Python
- LangGraph
- LangChain
- Groq LLM (Llama 3.3 70B Versatile)
- Tavily Search API
- Pydantic

---

## Installation

### Install Dependencies

```bash
pip install -U langchain-groq
pip install -U langchain-community
pip install -U tavily-python
pip install -U langgraph
```

---

## API Keys

Set the following API keys:

```python
os.environ["GROQ_API_KEY"] = "your_groq_api_key"
os.environ["TAVILY_API_KEY"] = "your_tavily_api_key"
```

For Google Colab:

```python
from google.colab import userdata

os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
os.environ["TAVILY_API_KEY"] = userdata.get("TAVILY_API_KEY")
```

---

## Workflow Execution

### Step 1: Supervisor

Receives the task and decides which worker should execute next.

Example:

```text
Task:
Impact of LPU architecture on AI inference speeds
```

Supervisor Decision:

```text
Research required → Researcher
```

---

### Step 2: Researcher

Uses Tavily Search to collect information.

```python
results = search_tool.invoke(query)
```

Output:

```text
Research notes collected
```

---

### Step 3: Supervisor Review

Checks the current state.

```text
Research Available?
YES
```

Decision:

```text
Send to Writer
```

---

### Step 4: Pause for Human Approval

The graph pauses before the Writer runs.

```text
SYSTEM PAUSED
Next Step: Writer
```

Human can review findings and approve continuation.

---

### Step 5: Writer

Generates the report using Groq LLM.

```python
res = llm.invoke(
    f"Write a report on {task} using: {context}"
)
```

Output:

```text
Final report generated
```

---

### Step 6: Completion

Supervisor evaluates the final result and ends the workflow.

```text
FINISH
```

---

## State Management

The workflow state is maintained through:

```python
class AgentState(TypedDict):
    task: str
    research_notes: List[str]
    draft: str
    next_node: str
    retry_count: int
    revision_feedback: str
```

### State Variables

| Variable | Description |
|-----------|-------------|
| task | User query |
| research_notes | Collected search results |
| draft | Generated report |
| next_node | Next agent to execute |
| retry_count | Retry tracking |
| revision_feedback | Supervisor instructions |

---

## LangGraph Flow

```python
builder.add_conditional_edges(
    "supervisor",
    lambda x: x["next_node"],
    {
        "researcher": "researcher",
        "writer": "writer",
        "FINISH": END
    }
)
```

Routing decisions are dynamically determined by the Supervisor.

---

## Sample Execution

```text
STARTING GRAPH

Supervisor reviewing state...
Moving to: researcher

Researcher is digging...
Research results collected

Supervisor reviewing state...
Moving to: writer

SYSTEM PAUSED
Next Step: writer

RESUMING GRAPH

Writer is composing...

FINAL DRAFT:
Impact of LPU architecture on AI inference speeds...
```

---

## Learning Outcomes

This project demonstrates:

- Agent-based AI systems
- Multi-agent orchestration
- Supervisor-worker architecture
- Human-in-the-loop AI
- State management with LangGraph
- Structured LLM outputs
- Web search integration
- Workflow recovery and checkpointing

---

## Future Enhancements

- Add Critic/Reviewer Agent
- Add Retry Logic
- Implement Reflection Loop
- Support Multiple Research Agents
- Add Vector Database Retrieval
- Integrate RAG Pipelines
- Add Streaming Responses
- Deploy using FastAPI or Streamlit

---

## Author

Developed as a LangGraph Multi-Agent Workflow demonstrating Supervisor–Researcher–Writer collaboration using Groq and Tavily Search.