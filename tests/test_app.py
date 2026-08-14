from app import app
import pytest

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Loadout" in response.data

def test_vaild_form(client):
    response = client.post("/", data={"credits": "5000", "agent": "Jett", "offensive": 25, "defensive": 25, "utility": 25, "versatility": 25})
    assert response.status_code == 200
    assert b"Recommended Loadout" in response.data

def test_invalid_credits(client):
    response = client.post("/", data={"credits": "abc", "agent": "Jett", "offensive": 25, "defensive": 25, "utility": 25, "versatility": 25})
    assert response.status_code == 200
    assert b"Invalid credits." in response.data

def test_negative_credits(client):
    response = client.post("/", data={"credits": "-100", "agent": "Jett", "offensive": 25, "defensive": 25, "utility": 25, "versatility": 25})
    assert response.status_code == 200
    assert b"Credits cannot be negative." in response.data

def test_over_credits(client):
    response = client.post("/", data={"credits": "10000", "agent": "Jett", "offensive": 25, "defensive": 25, "utility": 25, "versatility": 25})
    assert response.status_code == 200
    assert b"Credits cannot be over 9,000." in response.data

def test_missing_agent(client):
    response = client.post("/", data={"credits": "5000", "agent": "abc", "offensive": 25, "defensive": 25, "utility": 25, "versatility": 25})
    assert response.status_code == 200
    assert b"Invalid agent." in response.data

def test_missing_agent(client):
    response = client.post("/", data={"credits": "5000", "agent": "", "offensive": 25, "defensive": 25, "utility": 25, "versatility": 25})
    assert response.status_code == 200
    assert b"Invalid agent." in response.data

def test_invalid_weights(client):
    response = client.post("/", data={"credits": "5000", "agent": "", "offensive": 1, "defensive": 25, "utility": 25, "versatility": 25})
    assert response.status_code == 200
    assert b"Weights must add up to 100%." in response.data