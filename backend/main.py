from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from backend.logging_config import logger

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

@app.post("/api/log")
async def log_event(request: Request):
    data = await request.json()
    event = data.get("event")
    details = data.get("details", {})
    logger.info(f"{event}: {details}", extra={"event": event, **details})
    return JSONResponse({"status": "ok"}, status_code=status.HTTP_201_CREATED)

# Placeholder routers for modularity
# from .routers import agents, strategies, wallet, journaling, gist_management
# app.include_router(agents.router)
# app.include_router(strategies.router)
# app.include_router(wallet.router)
# app.include_router(journaling.router)
# app.include_router(gist_management.router)
