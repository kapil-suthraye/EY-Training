```text
                    +------------------+
                    |   Orchestrator   |
                    +------------------+
                             |
                             v
      +---------+ -> +-------------+ -> +--------+ -> +----------+
      | Planner |    | Researcher  |    | Writer |    | Reviewer |
      +---------+    +-------------+    +--------+    +----------+
             \             |               |               /
              \            |               |              /
               \           |               |             /
                +--------------------------------------+
                |      Telemetry / Observability       |
                +--------------------------------------+
                               |
          +--------------------+--------------------+
          |                    |                    |
          v                    v                    v
    Trace & Span IDs     Metrics Engine      Failure Tracking
                              |
                              v
                    Structured JSON Events
                              |
                              v
                    Console + trace.jsonl
```
