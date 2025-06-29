npm install winstonnpm install winston<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Copilot Instructions for AI-Powered Crypto Trading Quant Application

- This project is modular, agentic, and cloud-ready.
- Backend: Python (FastAPI), Frontend: React (TypeScript, Vite).
- Key modules: AI agents, trading strategies, wallet integration, dashboards, journaling, Gist management.
- Security is a top priority: follow best practices for API keys, wallet connections, and audit logging.
- Document all tasks and architecture in the `docs/` directory and GitHub Gists.
- Ensure all code is extensible for future support of Options, Futures, Forex, and other asset classes.
- Use agentic and AI-driven approaches for portfolio management and trading.
- All code must pass static code analysis (Python: flake8, mypy, bandit; TypeScript: eslint, tsc) before merging.
- All modules must have unit tests with at least 90% code coverage (Python: pytest, coverage.py; TypeScript: jest, ts-jest, react-testing-library).
- Coverage reports must be generated and reviewed for every PR. Block merges if coverage < 90% or static analysis fails.
- Use `uv` for all Python dependency management and installation. Always update `requirements.txt` and resolve dependencies with `uv pip install -r requirements.txt --upgrade` whenever the AI or a developer adds or updates a package.
- Implement a robust logging framework for all application events (backend and frontend).
- All logs must be structured and support integration with Splunk or other SIEM tools in the future.
- Ensure every module and API logs key actions, errors, and security events for audit and traceability.

# Gist Template for All New Tasks/Features

```
# [Feature/Module Name] ([Backend/Frontend/Other])

**Module:** [backend|frontend|wallet_integration|ai_agents|trading_strategies|journaling|dashboard|gist_management|docs], [other relevant tags]  
**Status:** [status: pending|in progress|done]  
**Gist ID:** [auto-generated or paste after creation]

## Description
[Briefly describe the purpose and scope of this task, feature, or module.]

## Tasks
- [ ] [Task 1: e.g., Design API contract or UI component]
- [ ] [Task 2: e.g., Integrate with library or service]
- [ ] [Task 3: e.g., Implement security, session, or error handling]
- [ ] [Task 4: e.g., Logging for audit/Splunk]
- [ ] [Task 5: e.g., Unit tests (90%+ coverage)]
- [ ] [Task 6: e.g., Documentation]

## Acceptance Criteria
- [ ] Feature meets all requirements and is secure
- [ ] All actions are logged and auditable
- [ ] Code passes static analysis and 90%+ test coverage
- [ ] Documentation and tests are complete
- [ ] Gist ID is referenced in code, PRs, and docs

## Collaboration & Traceability
- [ ] Copilot/AI agents use MCP context to generate code, tests, and docs for this Gist
- [ ] Developers review, refine, and merge code, updating Gist status as work progresses
- [ ] Reference this Gist ID in all related commits, PRs, and documentation

## Continuous Improvement
- [ ] Regularly review this Gist for blockers or improvements
- [ ] Use AI to suggest refactoring, new features, or documentation updates based on Gist history

---

**References:**  
- [Link to relevant library, standard, or documentation]
- [Any additional notes or links]
```

Always use this template for every new Gist in the GistPad workspace to ensure consistency, traceability, and compliance with project standards.
