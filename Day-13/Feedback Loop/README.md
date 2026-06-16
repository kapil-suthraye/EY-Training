# 🔁 Lab 2 — Prompt Feedback Loop with Automatic Iteration

**Day 13 · Module 5 · FinSight AI Credit Risk Scenario**

This lab demonstrates how to build an end-to-end prompt improvement workflow for LLM-powered applications. Using a simulated credit risk analysis system, you will log model interactions, evaluate output quality at scale, identify failure patterns, and iteratively improve prompts using evidence-driven feedback loops.

---

## 🎯 Learning Objectives

By the end of this lab, you will be able to:

- Build structured logging for LLM applications
- Store inference data in a persistent SQLite database
- Track prompt versions and prompt hashes
- Run automated quality checks on generated outputs
- Detect common failure modes across large batches of responses
- Categorize and quantify model failures
- Use failure evidence to improve prompt design
- Establish a repeatable prompt evaluation and optimization workflow
- Integrate observability platforms such as LangSmith

---

## 🏢 Business Scenario

You are working as an AI Engineer at **FinSight AI**, a company building AI-assisted credit risk analysis tools.

The system generates credit risk memos for borrowers using an LLM. Management has noticed inconsistent output quality, incomplete analyses, and occasional hallucinations.

Your task is to:

1. Instrument the system with structured logging.
2. Simulate production traffic.
3. Evaluate output quality automatically.
4. Identify recurring failure patterns.
5. Improve the prompt based on observed evidence.

---

## 📋 Lab Workflow

### Step 0 — Environment Setup

Install required libraries and configure API credentials.

**Key Packages**

- OpenAI
- Groq
- Anthropic
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- BERTScore

---

### Step 1 — Design the Logging Layer

Create a structured logging schema using a Python dataclass and SQLite.

Logged attributes include:

- Request ID
- Timestamp
- Prompt version
- Prompt hash
- Model name
- Borrower ID
- Token counts
- Latency
- Response text
- Evaluation metadata

The lab demonstrates production-style observability practices that enable traceability and debugging.

---

### Step 2 — Define Prompt Variants

Multiple prompt versions are created to compare performance.

#### Prompt v1.0
A minimal baseline prompt that simulates a rushed production deployment.

#### Prompt v1.1
A more structured prompt that:

- Defines analyst responsibilities
- Specifies required memo sections
- Encourages consistent formatting
- Reduces omission errors

Prompt versioning allows systematic comparison of prompt quality over time.

---

### Step 3 — Simulate Production Traffic

Generate approximately **50 borrower requests** using synthetic borrower profiles.

For each request:

1. Build borrower context
2. Send request to the selected LLM
3. Capture response
4. Measure latency
5. Store logs in SQLite

This produces a realistic evaluation dataset for later analysis.

---

### Step 4 — Run Automated Quality Probes

A quality evaluation suite automatically checks generated memos.

Example checks include:

#### Required Section Validation

Verify presence of critical sections such as:

- Borrower Overview
- Financial Performance
- Risk Assessment
- Recommendation

#### Completeness Checks

Detect missing content and incomplete analyses.

#### Consistency Checks

Identify formatting issues and structural deviations.

#### Scoring

Generate quantitative quality metrics for each response.

---

### Step 5 — Failure Pattern Analysis

Aggregate results across all logged requests.

Failure categories may include:

- Missing sections
- Insufficient risk analysis
- Weak recommendations
- Formatting inconsistencies
- Hallucinated information
- Generic responses

The notebook categorizes and counts failures to identify the most impactful quality issues.

---

### Step 6 — Evidence-Based Prompt Improvement

Review the worst-performing outputs and extract failure examples.

Use those findings to:

1. Understand root causes.
2. Identify prompt weaknesses.
3. Design improved instructions.
4. Create a revised prompt version.

This forms a closed-loop prompt optimization process.

---

## 📊 Architecture Overview

```text
Borrower Profiles
        │
        ▼
Prompt Template
        │
        ▼
LLM Inference
        │
        ▼
Structured Logging
(SQLite Database)
        │
        ▼
Quality Evaluation
        │
        ▼
Failure Categorization
        │
        ▼
Prompt Revision
        │
        ▼
Improved Outputs
```

---

## 🗂 Project Structure

```text
Feedback_Loop.ipynb
│
├── Step 0: Environment Setup
├── Step 1: Logging Schema & SQLite
├── Step 2: Prompt Variants
├── Step 3: Production Simulation
├── Step 4: Quality Probes
├── Step 5: Failure Analysis
├── Step 6: Prompt Improvement
└── Extension: LangSmith Integration
```

---

## 🔍 Key Concepts Demonstrated

### Prompt Versioning

Track changes to prompts over time and measure their impact.

### Observability

Capture inference metadata for auditing and debugging.

### Evaluation at Scale

Assess dozens of outputs automatically instead of manual review.

### Failure Analysis

Use quantitative methods to discover recurring model weaknesses.

### Continuous Improvement

Create a repeatable cycle:

```text
Prompt
  ↓
Generate
  ↓
Evaluate
  ↓
Analyze
  ↓
Improve
  ↓
Repeat
```

---

## 🚀 Extension Task

### LangSmith Integration

The notebook includes optional LangSmith integration to enable:

- Prompt tracing
- Experiment tracking
- Run comparison
- Evaluation dashboards
- Production monitoring

Suggested workflow:

1. Install LangSmith packages.
2. Configure API credentials.
3. Enable tracing.
4. Capture prompt and response metadata.
5. Analyze experiments through LangSmith dashboards.

---

## 📈 Expected Outcomes

After completing this lab, you will have:

- A fully logged LLM application workflow
- A persistent evaluation database
- Automated quality scoring
- Failure categorization pipelines
- Prompt improvement methodology
- Production-grade prompt engineering practices

---

## 💡 Real-World Applications

The techniques in this notebook can be applied to:

- Credit risk assessment
- Financial report generation
- Compliance review systems
- Customer support assistants
- Healthcare documentation
- Legal document analysis
- Enterprise AI copilots

---

## 🏆 Takeaway

Prompt engineering is not a one-time activity. High-performing AI systems rely on:

- Structured observability
- Automated evaluation
- Failure analysis
- Continuous iteration

This lab demonstrates how to build a feedback-driven improvement loop that transforms prompt engineering from trial-and-error into a measurable engineering discipline.

---
**Module:** Prompt Feedback Loop with Automatic Iteration  
**Domain:** Credit Risk Analysis  
**Focus Areas:** Prompt Engineering, Evaluation, Observability, LLMOps, Continuous Improvement