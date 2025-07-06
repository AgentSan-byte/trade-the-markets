# User Onboarding & Wallet Connection (Frontend) — Progress Checklist

**Linked Kanban Task:** [User Onboarding & Wallet Connection](../docs/gist_tracking_board.md)

## Checklist
- [ ] Design and implement custom wallet connect UI (Phantom, Solflare, etc.)
- [ ] Integrate wallet adapter libraries (no deprecated UI)
- [ ] Implement onboarding flow: connect wallet, show status, handle errors
- [ ] UI for user to set risk/trade preferences and enable auto-trade
- [ ] Log all wallet actions (connect, disconnect, error) to backend
- [ ] Unit tests for wallet connect and onboarding components (jest, react-testing-library)
- [ ] Document onboarding flow in `docs/`

## Acceptance Criteria
- [ ] Secure, non-custodial wallet connection
- [ ] User can set preferences and enable auto-trade
- [ ] All actions logged and auditable
- [ ] Code passes static analysis and 90%+ test coverage
- [ ] Documentation and tests are complete
- [ ] Gist ID is referenced in code, PRs, and docs

---

> Update this checklist as you make progress. When all items are checked, move the task to Review or Done in the Kanban board.
