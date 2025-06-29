import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.logging_config import logger

def test_read_root():
    client = TestClient(app)
    logger.info("Testing health check endpoint", extra={"event": "test_health_check"})
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "Backend is running"}
