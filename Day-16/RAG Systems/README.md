# Financial RAG System

A production-style Retrieval-Augmented Generation (RAG) pipeline for financial document analysis using Azure OpenAI, LangChain, FAISS, Hugging Face Embeddings, and RAGAS Evaluation.

This project demonstrates how enterprise AI applications retrieve relevant information from financial filings and generate grounded responses while evaluating retrieval and generation quality.

---

## Project Overview

This notebook builds an end-to-end Financial RAG system that:

- Loads financial documents (SEC 10-K filings)
- Splits documents into optimized chunks
- Generates vector embeddings using Hugging Face models
- Stores embeddings in a FAISS vector database
- Retrieves relevant financial context using MMR retrieval
- Generates answers using Azure OpenAI GPT models
- Evaluates RAG performance using RAGAS metrics
- Compares chunking strategies for quality vs latency trade-offs

---

## Architecture

```text
Financial Documents
        │
        ▼
Document Chunking
        │
        ▼
HuggingFace Embeddings
(all-MiniLM-L6-v2)
        │
        ▼
FAISS Vector Store
        │
        ▼
MMR Retriever
        │
        ▼
Azure OpenAI GPT-4o
        │
        ▼
Generated Answer
        │
        ▼
RAGAS Evaluation
```

---

## Features

### Document Processing

- SEC 10-K filing ingestion
- Recursive text chunking
- Configurable chunk sizes

### Vector Search

- Hugging Face sentence embeddings
- FAISS vector indexing
- Semantic similarity search

### Retrieval

- Maximal Marginal Relevance (MMR)
- Reduced duplicate contexts
- Better answer diversity

### LLM Integration

- Azure OpenAI GPT-4o
- Prompt engineering
- Context-grounded responses

### Evaluation

- Faithfulness
- Answer Relevancy
- Context Precision
- Context Recall

### Experimentation

- Chunk-size benchmarking
- Latency comparison
- Retrieval quality analysis

---

## Technology Stack

| Component | Technology |
|------------|------------|
| LLM | Azure OpenAI GPT-4o |
| Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | all-MiniLM-L6-v2 |
| Evaluation | RAGAS |
| Dataset | SEC 10-K Financial Filings |
| Environment | Google Colab |

---

## Project Workflow

### Step 1: Configure Azure OpenAI Credentials

Store credentials securely:

```python
AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_API_KEY
AZURE_OPENAI_DEPLOYMENT
AZURE_OPENAI_API_VERSION
```

---

### Step 2: Load Financial Documents

Sample SEC 10-K filings are loaded as source documents.

Example information:

- Revenue
- Cash holdings
- Operating expenses
- Business risks
- Financial performance

---

### Step 3: Chunk Documents

Documents are split using:

```python
RecursiveCharacterTextSplitter
```

Example:

```python
chunk_size = 512
chunk_overlap = 50
```

---

### Step 4: Generate Embeddings

Embedding model:

```python
all-MiniLM-L6-v2
```

Characteristics:

- 384-dimensional vectors
- Fast inference
- Open-source
- Optimized for semantic search

---

### Step 5: Create FAISS Index

Embeddings are stored in FAISS:

```python
vectorstore = FAISS.from_documents(...)
```

Benefits:

- Fast similarity search
- Scalable retrieval
- Low latency

---

### Step 6: Configure Retriever

MMR Retriever:

```python
retriever = vectorstore.as_retriever(
    search_type="mmr"
)
```

Advantages:

- Higher diversity
- Less duplicate context
- Better answer grounding

---

### Step 7: Generate Answers

Pipeline:

```text
Question
    ↓
Retriever
    ↓
Context
    ↓
Azure GPT-4o
    ↓
Answer
```

Example Questions:

```text
What was Apple's total revenue in fiscal year 2023?

How much cash did Apple have at the end of fiscal 2023?

What risks does Apple mention related to competition?
```

---

## RAG Evaluation

The notebook evaluates system performance using RAGAS.

### Metrics

| Metric | Purpose |
|----------|----------|
| Faithfulness | Measures hallucination risk |
| Answer Relevancy | Checks if answer addresses question |
| Context Precision | Relevance of retrieved chunks |
| Context Recall | Coverage of required information |

Example:

```python
evaluate(
    dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall
    ]
)
```

---

## Chunk Size Experiment

The notebook compares:

- 256
- 512
- 1024

Measured attributes:

- Retrieval Quality
- Faithfulness
- Response Latency
- Cost Efficiency

### Sample Results

| Chunk Size | Chunks | Avg Latency |
|------------|---------|------------|
| 256 | 13 | 1.43s |
| 512 | 7 | 1.84s |
| 1024 | 4 | 1.86s |

### Key Observation

Smaller chunks generally:

- Improve retrieval granularity
- Increase chunk count
- May improve context precision

Larger chunks generally:

- Reduce index size
- Lower retrieval operations
- May increase context noise

---

## Expected Learning Outcomes

By completing this project, you will understand:

- Retrieval-Augmented Generation (RAG)
- Vector databases and embeddings
- Financial document retrieval
- Azure OpenAI integration
- Retrieval optimization techniques
- Enterprise evaluation frameworks
- Cost vs performance trade-offs

---

## Extension Tasks

### Hybrid Retrieval

Combine:

- Semantic Search (FAISS)
- Keyword Search (BM25)

Using:

```python
EnsembleRetriever
```

Benefits:

- Improved recall
- Better factual grounding
- More robust retrieval

---

## Common Issues

### Azure Authentication Errors

Verify:

```python
AZURE_OPENAI_API_KEY
AZURE_OPENAI_ENDPOINT
```

### Embedding Dimension Mismatch

Ensure:

```python
all-MiniLM-L6-v2
```

is used consistently for index creation and querying.

### RAGAS Dependency Conflicts

Recommended versions:

```bash
ragas==0.1.21
langchain==0.2.17
langchain-core==0.2.43
langchain-community==0.2.19
langchain-openai==0.1.25
```

---

## Key Concepts Covered

- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Search
- FAISS Indexing
- MMR Retrieval
- Prompt Engineering
- Azure OpenAI
- RAG Evaluation
- Financial AI Systems
- Enterprise AI Architecture

---

## Future Improvements

- Multi-document financial analysis
- Hybrid Search (BM25 + Vector Search)
- Azure AI Search integration
- Metadata filtering
- Real SEC PDF ingestion
- Agentic financial assistants
- Multi-hop retrieval
- Production deployment on Azure

---

## Repository Structure

```text
Financial-RAG-System/
│
├── Financial_RAG_System.ipynb
├── README.md
├── requirements.txt
└── sample_data/
```

---

## Author

**Kapil Suthraye**

AI & Data Engineer | GenAI Developer | Data Engineer

### Skills

- Generative AI
- LangChain
- Azure OpenAI
- FAISS
- RAGAS
- Python
- Data Engineering
- Vector Databases

---

## Project Outcome

This project demonstrates a complete enterprise-grade Financial RAG workflow covering:

- Document Ingestion
- Embedding Generation
- Vector Search
- Context Retrieval
- GPT-Powered Answer Generation
- RAG Quality Evaluation
- Performance Benchmarking

making it an excellent foundation for building production-ready financial AI assistants.