"""
Tests for PandA server functionality
"""

import pytest
from fastapi.testclient import TestClient

from panda_mcp import PandaServer

@pytest.fixture
def client():
    """Create a test client."""
    server = PandaServer()
    return TestClient(server.app)

def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_metrics(client):
    """Test the metrics endpoint."""
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "active_sessions" in data
    assert "total_requests" in data
    assert "active_tools" in data 