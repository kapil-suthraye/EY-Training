# Traces/Spans vs Audit Logs

## Overview

In GenAI and distributed systems, **Traces/Spans** and **Audit Logs** serve different purposes. While both record information about requests and system behavior, they answer different questions.

| Aspect            | Trace / Spans                           | Audit Log                        |
| ----------------- | --------------------------------------- | -------------------------------- |
| Purpose           | Debugging and observability             | Compliance and accountability    |
| Focus             | How a request flowed through the system | What decision or action occurred |
| Retention         | Usually short-term                      | Usually long-term                |
| Sampling          | Often sampled                           | Typically 100% recorded          |
| Audience          | Engineers, SREs, DevOps                 | Auditors, Compliance, Security   |
| Question Answered | "Why did it fail?"                      | "What happened and who did it?"  |

---

## What is a Trace?

A trace records the complete journey of a request through multiple services.

### Example

User submits a loan application:

User → API → Risk Model → Fraud Check → Decision Engine

The trace shows:

* Request path
* Service interactions
* Response times
* Errors and failures
* Model latency
* Token usage

### Use Trace/Spans When

* Debugging production issues
* Finding performance bottlenecks
* Investigating failures
* Monitoring LLM latency
* Tracking token consumption
* Observing multi-agent workflows

---

## What is an Audit Log?

An audit log is an immutable record of important actions and decisions.

### Example

Loan Application Decision:

* User: John Doe
* Action: Loan Approved
* Timestamp: 2026-06-24 10:30 UTC
* Decision ID: DEC-12345
* Approved By: Risk Engine v2.1

The audit log provides a permanent record of the decision.

### Use Audit Logs When

* Regulatory compliance
* Security investigations
* Tracking user actions
* Recording approvals/rejections
* Maintaining legal evidence
* Governance and accountability

---

## How They Work Together

A single request can generate both:

### Example: Fraud Detection

1. Customer submits a transaction.
2. Fraud Guardrail evaluates the request.
3. Transaction is blocked.

### Trace Contains

* Guardrail execution steps
* Model calls
* Latency information
* Reason for block

### Audit Log Contains

* Transaction blocked
* Timestamp
* Rule triggered
* User/Account ID
* Compliance record

---

## Decision Guide

### Use Trace/Spans if you ask:

* Why did this request fail?
* Which service is slow?
* Where is the bottleneck?
* How many tokens were consumed?
* Which agent caused the error?

### Use Audit Logs if you ask:

* Who performed this action?
* When was this decision made?
* Can we prove this happened?
* What was approved or rejected?
* Can auditors verify this later?

### Use Both if you need:

* Compliance + Debugging
* Security investigations
* Guardrail monitoring
* Financial transactions
* Critical GenAI decisions

---

## Simple Rule

**Trace/Spans = How the system behaved**

**Audit Logs = What decision or action happened**

**Both = Critical workflows requiring observability and compliance**
