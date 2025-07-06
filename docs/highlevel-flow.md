graph TD
    A[Frontend (React + Vite)]
    B[Backend (FastAPI)]
    C[Solana Wallet Integration]
    D[AI Agents]
    E[Trading Strategies]
    F[Wallet Actions Logging]
    G[Journaling Module]
    H[Dashboard & Analytics]
    I[Gist-based Task Management]
    J[Audit & Security Logging]
    K[Unit Tests & Coverage]
    L[Cloud/Local Deployment]
    M[SIEM/Splunk Integration Ready]

    A -->|Connects via API| B
    A --> C
    A --> F
    A --> H
    A --> I
    A --> K
    A --> L

    C -->|User Connects Wallet| F
    F -->|Logs Actions| B
    B --> J
    B --> G
    B --> D
    B --> E
    B --> H
    B --> I
    B --> K
    B --> L
    B --> M

    D -->|Suggests/Executes Trades| E
    E -->|Executes Orders| C
    G -->|User Journals| H
    I -->|Task Tracking| H
    J -->|Audit Logs| M
    K -->|90%+ Coverage| L