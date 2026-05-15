"""
Integration tests for SmartBin API
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_create_user_success():
    response = client.post("/api/users", json={
        "user_id": "U001",
        "email": "john@university.edu",
        "name": "John Doe",
        "role": "student"
    })
    assert response.status_code == 201
    assert response.json()["user_id"] == "U001"


def test_create_user_invalid_email():
    response = client.post("/api/users", json={
        "user_id": "U002",
        "email": "john@gmail.com",
        "name": "John Doe",
        "role": "student"
    })
    assert response.status_code == 400


def test_get_user_not_found():
    response = client.get("/api/users/NONEXISTENT")
    assert response.status_code == 404


def test_create_reward_success():
    response = client.post("/api/rewards", json={
        "reward_id": "R001",
        "name": "Coffee Voucher",
        "point_cost": 50,
        "inventory": 100
    })
    assert response.status_code == 201


def test_create_bin_success():
    response = client.post("/api/bins", json={
        "bin_id": "B001",
        "location": "Library"
    })
    assert response.status_code == 201