# Architecture Overview

## System Diagram
- Modular, agentic architecture
- Backend (FastAPI, Python): AI agents, trading strategies, Gist management, journaling, API
- Frontend (React, TypeScript): Dashboard, wallet integration, Gist/task UI
- Database: (planned) for journaling, logs, and user data

```mermaid
flowchart TD
    F[Frontend (React + Vite)]
    B[Backend (FastAPI, Python)]
    W[Wallet Integration]
    A[AI Agents]
    T[Trading Strategies]
    J[Journaling]
    G[Gist Management]
    D[Dashboard]
    DB[(Database - planned)]
    L[Logging & Audit]

    F -->|API| B
    F --> W
    F --> D
    F --> G
    F --> L
    W -->|User Auth & Trade| B
    B --> W
    B --> A
    B --> T
    B --> J
    B --> G
    B --> D
    B --> L
    B --> DB
    A -->|Suggest/Execute| T
    T -->|Order| W
    G -->|Sync| D
    J -->|Logs| L
    L --> DB
```

## Module Interactions
- AI agents and strategies interact with trading APIs and Gist management
- Gist management syncs tasks with GitHub and updates dashboard
- Wallet integration enables secure user authentication and trade execution
- Journaling logs all trades and AI actions for audit and improvement

## Core Modular Agents
- News & Macro Analyst Agent
- Charting Agent
- Market Correlation Analyst
- Risk Manager Agent
- Strategy Generator Agent
- Trade Executor Agent
- Logging Agent
- User Management Agent
- Scheduler Agent
- Feedback Agent

## Auto-Trade Feature: Technical Flow
1. **User Opt-In & Configuration**
   - User enables “Auto-Trade” in the frontend and sets risk/trade parameters (e.g., max position size, leverage, allowed pairs).
   - Preferences are saved in the backend, linked to the user’s wallet address.
2. **AI Agent Monitoring**
   - Backend AI agent(s) continuously monitor market data (Jupiter API, etc.).
   - Agent evaluates trading opportunities based on user-configured strategies and risk settings.
3. **Opportunity Detection**
   - When an opportunity matches user criteria, the agent prepares a trade order.
   - Agent checks if auto-trade is enabled and within risk parameters.
4. **Transaction Preparation & Signing**
   - Backend prepares the transaction using the Jupiter Perp API.
   - For non-custodial security, the user’s wallet must sign:
     - (A) Session-Based Signing: Frontend prompts user for signature when trade is ready.
     - (B) Delegated/Pre-Approved Signing: User pre-approves trades or grants a session key for backend to sign (advanced, must be revocable and limited).
5. **Trade Execution**
   - Once signed, backend submits transaction to Solana network.
   - Trade is logged, dashboard updated, and action journaled.
6. **Logging, Journaling, and Feedback**
   - Every auto-trade is logged with full details.
   - User can review, provide feedback, and adjust settings at any time.

> This flow will be refined as implementation progresses, especially around secure, user-friendly signing for auto-trades.

## Extensibility
- Designed for easy addition of new asset classes (Options, Futures, Forex, etc.)
- Agentic modules can be extended or replaced

## Technical Infrastructure & Deployment
- Cloud vs. Local Deployment Architecture
- Inter-Agent Communication & Data Flows
- AI-Driven Development Pipeline

## Feedback, Iteration, & Future Enhancements
- Post-Launch Evaluation & Iterations
- Additional Features
- Bug Tracking & Issues

## Next Steps
- [ ] Add detailed diagrams
- [ ] Document API endpoints and data flows
- [ ] Update as modules are implemented

---
See other docs for security, testing, and Gist management details.
