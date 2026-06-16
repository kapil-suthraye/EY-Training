
# CreditLens – Production Pipeline Extensions

## Overview
This notebook extends a credit-policy RAG assistant ("CreditLens") with production-oriented capabilities focused on retrieval quality, governance, compliance, deployment, and cost optimization.

The project demonstrates:
- RAG retrieval evaluation using LlamaIndex and LangChain
- Human-in-the-loop approval workflows
- LLM cost benchmarking
- FastAPI deployment patterns
- DPDP-compliant audit logging

---

## Extension 1: LlamaIndex RAG – Retrieval Faithfulness Comparison

### Purpose
Evaluate whether a second retrieval framework (LlamaIndex) returns similar policy documents as the existing LangChain + FAISS retriever.

### What it does
1. Creates a LlamaIndex knowledge base.
2. Uses BAAI/bge-small-en-v1.5 embeddings.
3. Chunks documents using SentenceSplitter.
4. Retrieves top matching documents for several policy questions.
5. Compares retrieved document titles from:
   - LangChain + FAISS
   - LlamaIndex

### Why this task is useful
- Validates retrieval quality.
- Detects retrieval drift.
- Increases confidence that answers are grounded in the same source documents.

### Output Explanation
Example output:

- Query: "What is the minimum credit score for a loan?"
- LangChain returns top matching policy documents.
- LlamaIndex returns its top matching documents.
- Overlap score shows how many documents both systems selected.

Higher overlap generally indicates retrieval consistency.

---

## Extension 2: LangGraph-Style Human-in-the-Loop (HITL)

### Purpose
Prevent fully automated handling of high-risk or high-value loan decisions.

### What it does
Defines:
- LoanRequest
- ReviewDecision
- HITLWorkflow

Routing logic:

Human review required when:
- Loan amount >= INR 10,00,000
OR
- Risk score >= 0.70

### Why this task is useful
Financial systems often require human oversight for:
- Regulatory compliance
- Model-risk management
- Large financial exposure

### Output Explanation

AUTO_PROCESS:
- Request continues automatically.

HUMAN_REVIEW:
- Request enters review queue.
- Human reviewer must approve, reject, or escalate.

Example:

- INR 500,000 + risk 0.25 -> AUTO_PROCESS
- INR 1,500,000 + risk 0.62 -> HUMAN_REVIEW
- INR 200,000 + risk 0.82 -> HUMAN_REVIEW

---

## Extension 3: Cost Benchmarking

### Purpose
Estimate operational cost at production scale.

### What it does
Compares:

- GPT-4o
- GPT-4o-mini
- Gemini Flash
- Llama-3 API variants
- Self-hosted Llama-3

Assumptions:
- 80,000 queries/day
- 200 input tokens/query
- 300 output tokens/query

### Why this task is useful
Helps choose the most cost-effective model while balancing:
- Quality
- Latency
- Operating cost

### Output Explanation

Generated table includes:

- Model name
- Latency
- Daily cost
- Monthly cost

Example insight:

Llama-3-8B may reduce monthly cost dramatically compared with GPT-4o for high-volume workloads.

---

## Extension 4: FastAPI Production Wrapper

### Purpose
Expose CreditLens as a production-ready REST API.

### What it does

Features:
- FastAPI application
- CORS configuration
- Request validation
- Response validation
- Rate limiting
- Health endpoints

Rate limits:
- 30 requests
- Per 60-second window
- Per client IP

### Why this task is useful

Provides:
- Controlled access
- Protection against abuse
- Easy integration with frontend applications

### Output Explanation

Generated code can be saved as:

app.py

and run using:

uvicorn app:app --reload

Expected API behavior:
- Valid requests return answers.
- Excessive traffic returns HTTP 429.

---

## Extension 5: DPDP-Compliant Audit Logging

### Purpose
Meet governance and compliance requirements.

### What it does

Creates an audit schema containing:

- Event ID
- Timestamp
- Model version
- Officer ID
- Query hash
- Application hash
- Guardrail metadata
- PII handling metadata

### Why this task is useful

Supports:
- DPDP Act 2023 compliance
- RBI model governance
- Traceability
- Incident investigation

### Output Explanation

Sample audit event demonstrates:

- Immutable event tracking
- SHA-256 references instead of raw PII
- Audit retention readiness

---

## Architecture Summary

User Query
    |
    v
PII Redaction
    |
    v
Guardrails
    |
    v
Retriever (FAISS)
    |
    v
LLM
    |
    v
Safety Validation
    |
    +------> Audit Log
    |
    +------> Human Review (if required)
    |
    v
Final Response

---

## Key Production Benefits

### Reliability
- Retrieval benchmarking
- Consistent knowledge access

### Safety
- Guardrails
- PII protection
- Human review escalation

### Compliance
- DPDP-ready logging
- Auditability
- Governance controls

### Scalability
- FastAPI deployment
- Rate limiting
- Cost optimization

---

## Technologies Used

- LangChain
- LlamaIndex
- FAISS
- HuggingFace Embeddings
- FastAPI
- Python
- Pandas
- Matplotlib

---

## Notebook Outputs Summary

| Extension | Primary Output |
|------------|----------------|
| LlamaIndex Comparison | Retrieval overlap metrics |
| HITL Workflow | Auto-process vs human-review routing |
| Cost Benchmark | Monthly cost comparison table and chart |
| FastAPI Wrapper | Production API source code |
| DPDP Audit Log | Compliance-ready audit schema and sample event |

---

## Future Improvements

- Pinecone/Qdrant deployment
- LangSmith tracing
- Kubernetes autoscaling
- Object-lock audit storage
- Automated bias monitoring
- Production observability dashboards

