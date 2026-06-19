# README.md

# CrewAI + Groq Multi-Agent Supply Chain Pipeline

## Extension 1: Financial Analyst Agent Integration

### Project Overview

This project extends an existing CrewAI-based multi-agent supply chain disruption management system by introducing a new specialized agent: **Supply Chain Financial Analyst**.

The original system was designed to detect logistics disruptions, optimize routes, coordinate supplier communications, verify compliance requirements, and generate executive reports. Extension 1 enhances the decision-making process by adding a financial impact assessment layer that quantifies the business consequences of supply chain disruptions.

The Financial Analyst Agent calculates potential financial exposure resulting from disruptions, helping stakeholders understand the economic impact before implementing recovery actions.

---

## Business Problem

Global logistics organizations face significant financial risks when disruptions occur due to:

* Port closures
* Weather events
* Customs delays
* Supplier failures
* Transportation bottlenecks

While operational teams can identify and mitigate disruptions, executives also need visibility into:

* Additional rerouting costs
* SLA penalty risks
* Insurance implications
* Revenue impact due to delayed deliveries

This extension addresses that gap by providing automated financial analysis alongside operational recommendations.

---

## Objective of Extension 1

The goal of this extension is to:

1. Introduce a dedicated financial analysis agent.
2. Calculate total EUR exposure caused by logistics disruptions.
3. Generate multiple financial scenarios.
4. Provide business leaders with quantitative risk assessments.
5. Improve executive decision-making during supply chain incidents.

---

# Architecture

## Existing Agents

### Agent 1: Supply Chain Disruption Monitor

Responsible for identifying and analyzing disruptions across supply chain networks.

### Agent 2: Logistics Route Optimiser

Generates alternative shipment routes and evaluates trade-offs.

### Agent 3: Supplier Communications Specialist

Drafts communication plans for affected suppliers and stakeholders.

### Agent 4: Trade Compliance Officer

Ensures alternative routes comply with customs and regulatory requirements.

### Agent 5: Executive Communications Writer

Produces executive-level incident reports.

---

## New Agent Added

### Agent 6: Supply Chain Financial Analyst

This is the core contribution of Extension 1.

#### Responsibilities

* Estimate financial exposure caused by disruptions.
* Calculate rerouting cost increases.
* Assess SLA penalty risks.
* Estimate insurance-related costs.
* Model financial outcomes under different scenarios.
* Provide business impact visibility.

#### Agent Configuration

```python
financial_analyst = Agent(
    role="Supply Chain Financial Analyst",
    goal=(
        "Calculate total EUR exposure: rerouting cost delta, "
        "SLA penalty clauses triggered, insurance deductible, "
        "and opportunity cost of delayed deliveries."
    ),
    backstory=(
        "CFA-qualified financial analyst specialising in logistics cost modelling. "
        "Always presents base case, worst case, and best case scenarios."
    ),
    llm=GROQ_SMART,
    verbose=True,
    max_iter=3,
)
```

---

# Financial Analysis Logic

The Financial Analyst Agent evaluates four major cost components.

## 1. Rerouting Cost Delta

Measures additional transportation costs resulting from alternative shipment routes.

Examples:

* Longer routes
* Additional fuel costs
* Higher carrier charges
* Emergency logistics arrangements

---

## 2. SLA Penalty Exposure

Calculates penalties incurred when delivery commitments are violated.

Examples:

* Delayed customer deliveries
* Contractual penalties
* Service-level agreement breaches

---

## 3. Insurance Deductibles

Estimates costs that must be borne by the company before insurance coverage applies.

Examples:

* Cargo delay claims
* Shipment damage claims
* Force majeure impacts

---

## 4. Opportunity Cost

Estimates indirect business losses.

Examples:

* Lost customer confidence
* Delayed revenue realization
* Missed sales opportunities

---

# Financial Scenarios Generated

The agent produces three financial scenarios.

## Base Case

Most likely outcome under current conditions.

Example:

```text
Base Case Exposure: €2.5M
```

---

## Worst Case

Assumes maximum disruption duration and highest penalties.

Example:

```text
Worst Case Exposure: €8.2M
```

---

## Best Case

Assumes rapid recovery and minimal penalties.

Example:

```text
Best Case Exposure: €1.1M
```

---

# Task Added

## Task 6: Financial Impact Assessment

A new CrewAI task was introduced.

```python
task_financial = Task(
    description=
        "Calculate total EUR exposure: rerouting, SLA penalties, insurance.",
    expected_output=
        "Financial exposure table: base / worst / best case in EUR.",
    agent=financial_analyst,
    context=[task_monitor, task_route],
)
```

---

# Task Dependencies

The Financial Analyst Agent depends on outputs from:

### Task 1 – Disruption Monitoring

Provides:

* Severity level
* Duration estimates
* Affected shipments

### Task 2 – Route Optimization

Provides:

* Alternative routes
* Cost changes
* Delay estimates
* Risk scores

These outputs are automatically passed through CrewAI's context-sharing mechanism.

```python
context=[task_monitor, task_route]
```

This ensures that financial calculations are based on operational realities identified by previous agents.

---

# Crew Modification

The Financial Analyst Agent was added to the crew.

## Agent Registration

```python
agents=[
    disruption_monitor,
    route_optimiser,
    supplier_comms,
    compliance_officer,
    report_writer,
    financial_analyst
]
```

---

## Task Registration

```python
tasks=[
    task_monitor,
    task_route,
    task_comms,
    task_compliance,
    task_report,
    task_financial
]
```

---

# Workflow Execution

The complete workflow now follows this sequence:

```text
Disruption Monitor
        ↓
Route Optimiser
        ↓
Supplier Communications
        ↓
Compliance Officer
        ↓
Executive Report Writer
        ↓
Financial Analyst
```

---

# Sample Input

```text
ALERT: Port of Rotterdam has declared force majeure
due to severe North Sea storm surge.

Expected closure: 18-24 hours.

340 containers affected.

12 vessels diverted.

SLA breach window opens in 6 hours.
```

---

# Expected Output

The Financial Analyst Agent generates a structured report similar to:

```text
FINANCIAL EXPOSURE ANALYSIS

Base Case
-----------
Rerouting Cost: €1.2M
SLA Penalties: €0.8M
Insurance Cost: €0.3M
Opportunity Cost: €0.2M

Total Exposure: €2.5M

Worst Case
-----------
Total Exposure: €8.2M

Best Case
-----------
Total Exposure: €1.1M

Recommendation:
Proceed with Route Option 2 to minimize financial impact.
```

---

# Technologies Used

* CrewAI
* Groq LLM
* LiteLLM
* Python
* Pydantic

### Models

```python
GROQ_FAST
= groq/llama-3.1-8b-instant

GROQ_SMART
= groq/llama-3.3-70b-versatile

GROQ_MANAGER
= groq/llama-3.3-70b-versatile
```

---

# Key Learning Outcomes

After implementing Extension 1, the following concepts were demonstrated:

* Multi-agent orchestration using CrewAI
* Context sharing between dependent tasks
* Financial risk modeling within AI workflows
* Business impact analysis using LLM agents
* Integration of specialized domain experts into agent systems
* End-to-end supply chain incident management

---

# Extension 1 Contribution Summary

### Added Components

✅ Financial Analyst Agent

✅ Financial Assessment Task

✅ Context Dependency on Monitoring and Routing Tasks

✅ EUR Exposure Calculation

✅ Scenario-Based Financial Modeling

### Business Value

* Improved executive visibility
* Faster disruption response
* Better financial decision-making
* Quantified operational risk
* Reduced uncertainty during logistics incidents

---

## Author

**Kapil Suthraye**
AI & Data Engineer | Multi-Agent Systems | CrewAI | GenAI | Supply Chain Intelligence Systems
