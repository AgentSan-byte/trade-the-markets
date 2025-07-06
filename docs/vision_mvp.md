# Vision, Purpose, and MVP for AI-Powered Crypto Trading Platform

## Problem Statement
Day by day, trading in stocks and cryptocurrency is getting harder due to algorithmic trading, news events, political events, and institutional activity. Manual trading performance is poor; portfolios may grow but are often crushed by drawdowns. Profitable trading is typically only possible for experts. This platform aims to make trading more efficient and accessible by leveraging AI for every step, from news analysis to trade execution.

## Requirements
- Automated trading platform with perpetual crypto trading, designed for future expansion to Options, Futures, Forex, and Spot Crypto.
- Performance dashboard and automated journaling of daily trades by AI.
- Retrospective analysis of failures and improvements with AI assistance.
- Daily logs and reviews for continuous improvement.
- Available to individuals and institutions on a subscription basis.
- Gist-based task and feature management for transparency and collaboration.
- Multi-agent, modular architecture (MCP-style) for adaptability and extensibility.
- Secure, non-custodial wallet integration; all actions logged and auditable.
- High test coverage, static analysis, and CI/CD pipeline.
- **Auto-Trade Feature:** Users can opt-in to allow the system to place trades automatically on their behalf, based on AI-detected opportunities, without manual intervention.

## Market Validation
- Personal use until goals are met, then target retail traders and institutions (colleges, small businesses, groups).

## Product & Features
- Automated, AI-powered trading: analysis, trade execution, daily PnL dashboard, journaling, strategy building.
- Agentic portfolio management and trading: Developer Agent, QA Agent, News Analyst, Charting Agent, Market Correlation Analyst, Risk Manager, Strategy Generator, Trade Executor, Logging Agent, User Management Agent, Scheduler Agent, Feedback Agent.
- Configurable risk and trade parameters; users can set preferences and provide feedback to AI agents.
- Performance dashboards for individuals and organizations.
- Multi-cloud/local deployment.
- **Auto-Trade Option:** Users can enable/disable auto-trading. When enabled, the AI agent will execute trades automatically according to user-defined risk and strategy settings.

## Business Model
- Subscription pricing for individuals and institutions.
- Target annual revenue with scalable SaaS model.

## Competitive Advantage
- No manual trading required; users can review, give feedback, and configure AI agents.
- Modular, multi-agent, and highly configurable platform.
- Transparent, auditable, and continuously improving with user and AI feedback.
- **Auto-Trade Convenience:** Users can let the system trade for them, maximizing opportunities 24/7.

## Team
- Anonymous, decentralized team (inspired by Satoshi Nakamoto).

## Technical Infrastructure & Deployment
- Modular, agentic backend (FastAPI/Python), frontend (React/TypeScript), and planned database.
- Inter-agent communication and data flows.
- Cloud and local deployment support.
- AI-driven development pipeline.

## Feedback, Iteration, & Future Enhancements
- Post-launch evaluation and iteration.
- Continuous feedback loop with users and AI.
- Bug tracking and issue management.

## MVP (Minimum Viable Product)

### User Flow & Features
1. **User Onboarding & Authentication**
   - User visits the platform and is prompted to connect their Solana wallet (Phantom, Solflare, etc.).
   - Secure, non-custodial wallet connection (no private keys stored).
   - User profile is created/linked to wallet address.
2. **Dashboard & Account Overview**
   - After connecting, user sees a dashboard:
     - Wallet balance and available assets (fetched via Solana RPC).
     - Recent trades and PnL summary.
     - Status of AI agent(s) and current trading strategy.
3. **AI Agent & Strategy Selection**
   - User can select or activate a basic AI trading agent (e.g., “Momentum Perp Trader”).
   - Agent displays its current market view, suggested trades, and risk settings.
   - User can review and optionally adjust risk parameters (e.g., max position size, leverage).
   - **User can enable Auto-Trade mode:** When enabled, the AI agent will place trades automatically on the user's behalf, according to the selected strategy and risk settings.
4. **Market Data & Trade Setup**
   - Real-time market data for Jupiter Solana Perp pairs is displayed.
   - User can view AI agent’s recommended trade (e.g., “Buy SOL-PERP at $X, 2x leverage”).
   - User can approve/reject the trade suggestion, or let the system auto-execute if Auto-Trade is enabled.
5. **Trade Execution**
   - On approval or via Auto-Trade, the platform:
     - Prepares the transaction using the Jupiter Perp API.
     - Prompts the user to sign the transaction with their wallet (for manual trades), or signs automatically if pre-approved (Auto-Trade, with user consent).
     - Submits the signed transaction to the Solana network.
   - User receives confirmation of successful order placement.
6. **Journaling & Logging**
   - Every trade (suggested, approved, executed, or auto-executed) is automatically journaled.
   - Daily summary and PnL are logged and available for review.
   - All actions are auditable and can be exported.
7. **Feedback & Task Management**
   - User can provide feedback on AI agent performance.
   - Gist-based task management is available for feature requests, bug reports, and journaling.

### Technical Features
- FastAPI backend with endpoints for:
  - Wallet connection/session management
  - Market data retrieval (Jupiter API integration)
  - Trade suggestion and execution (manual and auto-trade)
  - Journaling and logging
- React frontend with:
  - Custom wallet connect UI
  - Dashboard, trade review, and journaling components
  - Auto-Trade toggle and status display
  - Real-time updates and notifications
- Logging and audit trail for all user and agent actions
- Unit/integration tests and static analysis for all modules

### Example User Story
1. Alice visits the platform and connects her Phantom wallet.
2. She sees her SOL balance and recent trades on the dashboard.
3. The AI agent suggests a long trade on SOL-PERP with 2x leverage.
4. Alice enables Auto-Trade mode and sets her risk to 1.5x.
5. The platform detects an opportunity and automatically prepares and executes the order, with Alice’s pre-approval.
6. The trade is logged, and Alice can review it in her journal and dashboard.
7. At day’s end, Alice reviews her PnL and provides feedback to the AI agent.

## Iterative Development Plan
1. Core infrastructure: backend, frontend, agent framework, logging.
2. Wallet integration & user management.
3. Agent modules: News/Macro Analyst → Charting Agent → Strategy Generator → Trade Executor → Risk Manager.
4. Dashboard & journaling: real-time PnL, trade logs, daily AI-generated journal.
5. Gist-based task management.
6. Testing & CI/CD.
7. Feedback loop: user/AI feedback agent, post-launch iteration.

## Next Steps
- [ ] Finalize and document MVP scope
- [ ] Build and test wallet connect, dashboard, and journaling modules
- [ ] Implement basic AI agent and trading strategy
- [ ] Set up Gist-based task management
- [ ] Enforce testing, coverage, and static analysis in CI/CD
- [ ] Continuously document architecture, features, and decisions

---
This document will evolve as the project progresses. All major decisions, features, and architecture changes should be recorded here and in the `docs/` directory.
