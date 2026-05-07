# Product Requirements Document (PRD): The Zanime Agentic Enterprise

> **Constitutional Reference:** See [VISION.md](./VISION.md) for the foundational laws, product philosophy, and end-state definition that govern all decisions in this PRD.

## 1. Product Overview
**Product Name:** Zanime Agentic Enterprise Engine (Z-EAOM)
**Product Type:** Autonomous Corporate Operating System
**Primary Objective:** To build a fully autonomous, zero-recurring-cost digital product empire orchestrated entirely by 128 specialized AI agents interacting via deterministic GitHub Action workflows.

**Core Philosophy (The Z-EAOM Framework):** Optimize for Orchestration Efficiency (Outcome per Token Ratio). The system must process 80% of tasks deterministically without invoking expensive reasoning models. All models utilize free-tier endpoints (NVIDIA NIM, Google Gemini). AI models are treated as capital expenditures; GitHub actions are treated as the corporate nervous system.

## 2. System Architecture
The enterprise is structured into three distinct processing layers to prevent LLM hallucination and manage token limits:

### Layer 1: The Managing Agents (Reasoning Layer)
*   **Location:** `/Chief Executive Officer (CEO)/[Division Name]/Managing_Agent_[Role].md`
*   **Engine:** `meta/llama-3.3-70b-instruct` via NVIDIA NIM (confirmed ✅). Primary reasoning and strategic synthesis model.
*   **Function:** Strategic analysis, cross-functional alignment, and generating strict requirement documents (PRDs, Creative Briefs). Every output is audited against the **5-Gate Validation** (Zero-Cost, Sovereign, High-Ticket, Scalable, Viral).
*   **Key Nodes:** CEO, CDO, CPO, CTO, CMO, COO, CFO, VP Legal, VP Content, VP Design, VP QA.

### Layer 2: The Worker Agents (Execution Layer)
*   **Location:** Nested sub-directories under each Division (e.g., `/CTO/SaaS & App Development/Worker_Backend_Engineer.md`).
*   **Engine:** `meta/llama-3.3-70b-instruct` / `qwen/qwen3-next-80b-a3b-instruct` via NVIDIA NIM (confirmed ✅). Gemini 2.5 Flash Lite for high-volume parsing tasks (500 RPD confirmed ✅).
*   **Function:** Execution of linear, scoped tasks based strictly on the Managing Agent's payload. Employs expert frameworks like **P.R.E.M.I.U.M.** for OS/Dashboard design and the **44 Master Skills** for product high-fidelity.

### Layer 3: The Connection Agents (Data Bus Layer)
*   **Location:** `.github/workflows/` (Conceptualized in Connection_Agents_Data_Bus.md).
*   **Engine:** Zero-token scripts (Bash, Python 3.11, Node.js 24, GitHub Actions).
*   **Function:** Intercepts payloads, validates JSON schemas, and routes files to the next Agent. Prevents lateral "agent chatter" and enforces the Hub-and-Spoke communication model.

## 3. Operational Workflows (The Data Flow)
The company operates on deterministic, file-based trigger loops.

### Primary Workflow: The Daily Intel Execution Loop
1.  **Ingestion:** External Intel Gatherer commits `daily_intel.json`.
2.  **Filter (CDO/CEO):** Triggers `Managing_Agent_CDO` to evaluate against KPIs. If actionable, outputs `Strategic_Directive.md`.
3.  **Routing (Data Bus):** Connection Agent splits the directive to CPO and CMO.
4.  **Strategy Generation (CPO):** `Managing_Agent_CPO` outputs strict `PRD.json` based on the 44 Master Skills.
5.  **Parallel Execution:**
    *   **Engineering Branch:** CTO reads `PRD.json` → Triggers `Worker_Backend` & `Worker_Frontend` → Opens PR with code.
    *   **Marketing Branch:** CMO reads `PRD.json` → Triggers `Worker_Paid_Media` & `Worker_Content_Designer` → Opens PR with ad copy and landing page SEO.
6.  **Governance Gate:** `Managing_Agent_VP_QA` runs an LLM-as-a-judge check against the original `PRD.json`. `Managing_Agent_Legal` checks copy for compliance.
7.  **Deployment:** Connection Agent auto-merges and deploys to Cloudflare Pages / Fly.io.

## 4. Technical Specifications & Infrastructure
The infrastructure adheres strictly to the Global Toolkit (Sell Forever) mandate. No capped freemium SaaS allowed.

| Function | Approved Tooling | Purpose in Agentic Stack |
| :--- | :--- | :--- |
| **Orchestration** | GitHub Actions | The Data Bus; triggers agents on file commits. |
| **Version Control** | GitHub / Gitea | The shared "memory" and workspace of all Agents. |
| **Agent Runtimes** | NVIDIA NIM / Gemini API | Free-tier, elite-level inference environments (Llama 3.3 70B, Llama 3.3). |
| **Deployment** | Cloudflare Pages / Fly.io | Automated CI/CD targets for Agent-generated code. |
| **Project Tracking** | Obsidian (Local + Git) | Markdown-based knowledge graph for cross-agent context. |

## 5. System Constraints & Risk Mitigation
To prevent cascading failures or runaway API costs, the system enforces the following constraints:

*   **The "No Chat" Protocol:** Agents do not communicate via open-ended conversational threads. They communicate exclusively by reading and writing structured files (e.g., `payload.json`) via Git commits.
*   **Strict Schema Validation:** If a Managing Agent outputs a PRD that fails the `PRD_Schema.json` validation, the GitHub Action will fail the build and prevent the Worker Agents from executing.
*   **Token Budget Enforcement:** Complex reasoning tasks are routed to `meta/llama-3.3-70b-instruct`. Routine tasks are explicitly routed to Gemini 2.5 Flash Lite.
*   **Pre-Mortem Failure Modes:** Every one of the 128 Agent `.md` files contains a hardcoded `<failure_modes>` XML tag and catch-logic for "thinking" model latency.

## 6. Definition of Done (DoD) for Phase 1
Phase 1 is complete when:
- All 11 Division Managing Agents are configured.
- All 59 Worker Agents are generated and placed in their respective divisional directories.
- The Connection Agent (Data Bus) architecture is documented.
- The first `action.yml` file is deployed to GitHub to test the CDO -> CPO handoff.