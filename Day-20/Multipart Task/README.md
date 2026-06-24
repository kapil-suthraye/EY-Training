# Observability for a Multi-Agent System

A Python-based observability layer for a multi-agent workflow that demonstrates distributed tracing concepts such as **trace correlation**, **span correlation**, **structured telemetry**, **progress tracking**, **throughput monitoring**, **failure localization**, and **run summaries**.

This project transforms a simple agent pipeline into an observable system that emits structured JSON events similar to what would be consumed by OpenTelemetry, Datadog, Splunk, Grafana, or CloudWatch.

---

## Overview

The workflow consists of four agents executed sequentially:

```text
Planner → Researcher → Writer → Reviewer
```

Each agent performs a configurable number of steps while the observability layer captures:

- Agent lifecycle events
- Pipeline progress
- Throughput metrics
- Agent execution durations
- Failure details
- Run summaries

---

## Features

### 1. Distributed Trace Correlation

Every workflow execution receives a unique:

- `trace_id` → identifies the entire workflow run
- `span_id` → identifies an individual agent execution

Example:

```json
{
  "trace_id": "3f3ab7f0-c2fd-4d7a-a6f6-0a1e34b9a00a",
  "span_id": "71e0e6b5-b02b-4d57-aebd-d53e58f9163a"
}
```

---

### 2. Structured JSON Telemetry

Instead of unstructured console logs, the application emits JSON events.

Example:

```json
{
  "timestamp": "2026-06-24T09:14:02Z",
  "trace_id": "3f3ab7f0-c2fd-4d7a-a6f6-0a1e34b9a00a",
  "span_id": "71e0e6b5-b02b-4d57-aebd-d53e58f9163a",
  "event": "agent_started",
  "agent": "Planner"
}
```

---

### 3. Progress Monitoring

Pipeline-level metrics include:

#### Pipeline Completion %

```python
completed_steps / total_steps * 100
```

#### Throughput

```python
completed_steps / elapsed_time
```

#### Agent Duration

```python
agent_end_time - agent_start_time
```

---

### 4. Progress Event Throttling

To reduce telemetry noise, progress events are emitted only at:

- 25%
- 50%
- 75%
- 100%

rather than every step.

---

### 5. Failure Localization

When an agent fails:

- Failed agent name is captured
- Failed step is identified
- Error message is logged
- Current pipeline progress is recorded

Example:

```json
{
  "event": "agent_failed",
  "agent": "Writer",
  "error": "Writer failed at step 3",
  "pipeline_percent_complete": 73.33
}
```

---

### 6. Run Summary

At the end of execution a summary event is emitted:

```json
{
  "event": "run_summary",
  "status": "success",
  "duration_seconds": 2.41,
  "agents_completed": 4
}
```

---

## Architecture

```text
+--------------------------------------------------+
|                  Orchestrator                    |
+--------------------------------------------------+
                      |
                      |
                      v
      +-----------------------------------+
      |          Telemetry Layer          |
      +-----------------------------------+
                      |
                      |
                      v

Planner --> Researcher --> Writer --> Reviewer
   |            |             |           |
   |            |             |           |
   +------------+-------------+-----------+
                    |
                    v

           Structured JSON Events
                    |
                    v

      +-----------------------------+
      | trace_id / span_id Tracking |
      +-----------------------------+
                    |
                    v

      Progress | Throughput | Errors
                    |
                    v

             Run Summary Event
```

---

## Event Lifecycle

```text
agent_started
      ↓
agent_progress (25%)
      ↓
agent_progress (50%)
      ↓
agent_progress (75%)
      ↓
agent_progress (100%)
      ↓
agent_completed
```

Failure path:

```text
agent_started
      ↓
agent_progress
      ↓
agent_failed
      ↓
run_summary
```

---

## Project Structure

```text
.
├── agents.py
├── README.md
└── trace.jsonl (optional stretch goal)
```

---

## Requirements

- Python 3.9+
- Standard Library Only

No external dependencies required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/multi-agent-observability.git
```

Navigate into the project:

```bash
cd multi-agent-observability
```

---

## Running the Application

Execute:

```bash
python agents.py
```

---

## Sample Output

```json
{
  "timestamp": "2026-06-24T09:14:02Z",
  "trace_id": "6b1d74a7-85db-48ff-a8a1-5c537f598d8d",
  "span_id": "7fb03fef-9ef6-46a4-b1bc-f89634e9d60e",
  "event": "agent_started",
  "agent": "Planner"
}
```

```json
{
  "event": "agent_progress",
  "agent": "Planner",
  "agent_percent_complete": 50.0,
  "pipeline_percent_complete": 20.0,
  "throughput_steps_per_sec": 8.52
}
```

```json
{
  "event": "agent_completed",
  "agent": "Planner",
  "duration_seconds": 0.42
}
```

---

## Testing Failure Scenarios

Modify the Writer agent:

```python
Agent("Writer", 4, fail_at_step=3)
```

Run again:

```bash
python agents.py
```

Expected output:

```json
{
  "event": "agent_failed",
  "agent": "Writer",
  "error": "Writer failed at step 3"
}
```

---

## Stretch Goal – Trace Persistence

Persist all telemetry events:

```python
with open("trace.jsonl", "a") as file:
    file.write(json.dumps(payload) + "\n")
```

Example:

```text
trace.jsonl
```

```json
{"event":"agent_started","agent":"Planner"}
{"event":"agent_progress","agent":"Planner"}
{"event":"agent_completed","agent":"Planner"}
```

---

## Observability Concepts Demonstrated

- Distributed Tracing
- Trace Correlation
- Span Correlation
- Structured Logging
- Telemetry Pipelines
- Agent Lifecycle Monitoring
- Throughput Measurement
- Failure Localization
- Run Health Monitoring
- Event Throttling

---

## Future Enhancements

Potential production-grade additions:

- OpenTelemetry Integration
- Grafana Dashboards
- Datadog Exporter
- CloudWatch Integration
- Parent/Child Span Relationships
- Parallel Agent Execution
- Stall Detection Alerts
- Retry Monitoring
- Cost & Token Tracking
- Agent Quality Metrics

---

## Learning Outcomes

This project demonstrates how to evolve a basic multi-agent workflow from simple console logging into an observable system capable of supporting:

- Debugging
- Monitoring
- Performance Analysis
- Failure Investigation
- Distributed Tracing

using only Python's standard library.

---

## Author

Kapil Suthraye

AI & Data Engineer | GenAI Developer
