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
