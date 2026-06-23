# Design Decision By Domain 

| Domain                      | Design Decision                                  | Reasoning                                                                                             |
| --------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| **Topology**                | MCP-centric multi-server architecture            | Amazon Ads and SP-API are separate systems. One orchestrating agent connects to multiple MCP servers. |
| **Discovery**               | Static server discovery (pinned servers)         | Avoid dynamic registration to reduce security risks and prevent rogue tool injection.                 |
| **Authorization**           | Least-privilege access                           | Grant only required SP-API roles and use Restricted Data Tokens only when PII access is needed.       |
| **Authentication**          | Separate credentials per service/account         | Maintain isolation between Amazon Ads and SP-API access.                                              |
| **Trust Boundary**          | Separate Amazon-hosted and Seller-hosted systems | Ads data remains in Amazon boundary; Orders, Inventory, and PII remain within seller boundary.        |
| **Human Approval**          | Human-in-the-loop for money-impacting actions    | Price changes, budget increases, campaign launches require approval before execution.                 |
| **State Management**        | Support asynchronous jobs                        | SP-API reports are long-running and require job tracking instead of synchronous calls.                |
| **Transport Protocol**      | JSON-RPC over HTTPS + SSE                        | Consistent with Amazon Ads MCP implementation.                                                        |
| **Rate Limiting**           | Quota-aware throttling                           | Prevent SP-API rate-limit violations.                                                                 |
| **Event Handling**          | Event-driven notifications                       | Lost Buy Box, low inventory, ad spikes should trigger events instead of continuous polling.           |
| **Security**                | Treat reviews/messages as untrusted input        | Prevent prompt injection attacks from customer-generated content.                                     |
| **Data Governance**         | Separate PII and business data                   | Minimize exposure of customer information.                                                            |
| **Profitability Analytics** | Join Amazon data with private COGS               | Amazon APIs do not provide product cost information.                                                  |
| **Auditability**            | Log every tool invocation                        | Required for compliance, troubleshooting, and approvals.                                              |
| **Agency Support**          | Per-client credential isolation                  | Prevent cross-client data access.                                                                     |

# Thinking Process

# Thinking Process

## Step 1: Understand Business Objective

Amazon seller wants an AI agent to automate:

- Inventory Management
- Pricing Optimization
- Advertising Management
- Order Processing
- Profitability Tracking
- Customer Communication

---

## Step 2: Identify Required Systems

The agent needs data from:

1. Amazon Ads MCP Server
2. SP-API MCP Server
3. Seller's Private Cost (COGS) Database

---

## Step 3: Define Trust Boundaries

### Amazon-Hosted Boundary
- Amazon Ads MCP Server
- Advertising Data
- Campaign Management

### Seller-Controlled Boundary
- SP-API MCP Server
- Orders
- Inventory
- Listings
- Customer Information (PII)

---

## Step 4: Design Security Controls

### Authentication
- Separate credentials for each service

### Authorization
- Least-privilege access
- Restricted Data Tokens for PII operations

### Governance
- Audit logging
- Tool access control
- Prompt injection protection

---

## Step 5: Define Agent Behavior

### Autonomous Actions
- Read inventory levels
- Generate reports
- Analyze profitability
- Monitor advertising performance

### Human Approval Required
- Price changes
- Campaign launches
- Budget increases
- Inventory commitments

---

## Step 6: Design Communication Flow

- Agent communicates with MCP servers
- JSON-RPC over HTTPS
- SSE for streaming responses
- Event-driven notifications preferred over polling

---

## Step 7: Monitoring and Compliance

Monitor:

- Low inventory
- Lost Buy Box
- Advertising spikes
- Failed API calls
- Rate limit violations

Maintain:

- Audit logs
- Approval history
- Security controls

---

## Final Architecture Principle

One Orchestrating Agent + Multiple MCP Servers + Strong Trust Boundaries + Human Approval for High-Risk Actions
 
# Block Diagram 

flowchart TD

    A[Orchestrating AI Agent]

    A --> B[Amazon Ads MCP Server]
    A --> C[SP-API MCP Server]
    A --> D[Seller Cost/COGS Database]

    B --> E[Ads Campaigns]
    B --> F[Ad Reports]

    C --> G[Orders]
    C --> H[Inventory]
    C --> I[Listings]
    C --> J[Returns]

    A --> K[Human Approval Gateway]

    K --> L[Price Changes]
    K --> M[Budget Changes]
    K --> N[Inventory Commitments]

    A --> O[Event Monitor]

    O --> P[Low Stock Alert]
    O --> Q[Lost Buy Box Alert]
    O --> R[Ad Spend Spike Alert]

    A --> S[Audit Logs]

    T[Customer Reviews & Messages]
    T --> U[Input Validation / Prompt Injection Filter]
    U --> A