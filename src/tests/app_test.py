"""
Module used for testing simple server module
"""

from fastapi.testclient import TestClient
import pytest

from application.app import app

client = TestClient(app)

class TestSimpleServer:
    """
    TestSimpleServer class for testing SimpleServer
    """
    @pytest.mark.asyncio
    async def read_health_test(self):
        """Tests the health check endpoint"""
        response = client.get("health")

        assert response.status_code == 200
        assert response.json() == {"health": "ok"}

    @pytest.mark.asyncio
    async def read_main_test(self):
        """Tests the main endpoint"""
        response = client.get("/")

        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}

    @pytest.mark.asyncio
    async def bye_test(self):
        """Tests the bye endpoint"""
        response = client.get("bye")

        assert response.status_code == 200
        assert response.json() == {"msg": "Bye Bye"}

    @pytest.mark.asyncio
    async def info_test(self):
        """Tests the info endpoint"""
        response = client.get("info")

        assert response.status_code == 200
        data = response.json()

        assert data["app_name"] == "Práctica de Juan Arillo"
        assert data["version"] == "1.0.0"
        assert "server_time" in data
        assert "total_requests" in data
        assert isinstance(data["total_requests"], float)
