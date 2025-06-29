from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .logging_config import logger

app = FastAPI(title="AI-Powered Crypto Trading Quant Backend")

# CORS setup for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    logger.info("Health check endpoint called", extra={"event": "health_check"})
    return {"status": "Backend is running"}

# Placeholder routers for modularity
# from .routers import agents, strategies, wallet, journaling, gist_management
# app.include_router(agents.router)
# app.include_router(strategies.router)
# app.include_router(wallet.router)
# app.include_router(journaling.router)
# app.include_router(gist_management.router)
