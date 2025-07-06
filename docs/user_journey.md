# User Journey: AI-Powered Crypto Trading Platform (Jupiter Solana Perp Trading)

## Overview
This document describes the end-to-end user journey for the MVP, from onboarding to placing a successful order using the platform's AI-powered trading agent and Jupiter Solana Perp integration.

---

## 1. User Onboarding & Authentication
- User visits the platform and is prompted to connect their Solana wallet (Phantom, Solflare, etc.).
- Secure, non-custodial wallet connection (no private keys stored).
- User profile is created/linked to wallet address.

## 2. Dashboard & Account Overview
- After connecting, user sees a dashboard:
  - Wallet balance and available assets (fetched via Solana RPC).
  - Recent trades and PnL summary.
  - Status of AI agent(s) and current trading strategy.

## 3. AI Agent & Strategy Selection
- User can select or activate a basic AI trading agent (e.g., “Momentum Perp Trader”).
- Agent displays its current market view, suggested trades, and risk settings.
- User can review and optionally adjust risk parameters (e.g., max position size, leverage).
- **User can enable Auto-Trade mode:** When enabled, the AI agent will place trades automatically on the user's behalf, according to the selected strategy and risk settings.

## 4. Market Data & Trade Setup
- Real-time market data for Jupiter Solana Perp pairs is displayed.
- User can view AI agent’s recommended trade (e.g., “Buy SOL-PERP at $X, 2x leverage”).
- User can approve/reject the trade suggestion, or let the system auto-execute if Auto-Trade is enabled.

## 5. Trade Execution
- On approval or via Auto-Trade, the platform:
  - Prepares the transaction using the Jupiter Perp API.
  - Prompts the user to sign the transaction with their wallet (for manual trades), or signs automatically if pre-approved (Auto-Trade, with user consent).
  - Submits the signed transaction to the Solana network.
- User receives confirmation of successful order placement.

## 6. Journaling & Logging
- Every trade (suggested, approved, executed, or auto-executed) is automatically journaled.
- Daily summary and PnL are logged and available for review.
- All actions are auditable and can be exported.

## 7. Feedback & Task Management
- User can provide feedback on AI agent performance.
- Gist-based task management is available for feature requests, bug reports, and journaling.

---

## Example User Story
1. Alice visits the platform and connects her Phantom wallet.
2. She sees her SOL balance and recent trades on the dashboard.
3. The AI agent suggests a long trade on SOL-PERP with 2x leverage.
4. Alice enables Auto-Trade mode and sets her risk to 1.5x.
5. The platform detects an opportunity and automatically prepares and executes the order, with Alice’s pre-approval.
6. The trade is logged, and Alice can review it in her journal and dashboard.
7. At day’s end, Alice reviews her PnL and provides feedback to the AI agent.

---
This user journey will be updated as the platform evolves and new features are added.
