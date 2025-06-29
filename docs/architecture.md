# Architecture Overview

## System Diagram
- Modular, agentic architecture
- Backend (FastAPI, Python): AI agents, trading strategies, Gist management, journaling, API
- Frontend (React, TypeScript): Dashboard, wallet integration, Gist/task UI
- Database: (planned) for journaling, logs, and user data

## Module Interactions
- AI agents and strategies interact with trading APIs and Gist management
- Gist management syncs tasks with GitHub and updates dashboard
- Wallet integration enables secure user authentication and trade execution
- Journaling logs all trades and AI actions for audit and improvement

## Extensibility
- Designed for easy addition of new asset classes (Options, Futures, Forex, etc.)
- Agentic modules can be extended or replaced

## Next Steps
- [ ] Add detailed diagrams
- [ ] Document API endpoints and data flows
- [ ] Update as modules are implemented

---
See other docs for security, testing, and Gist management details.
