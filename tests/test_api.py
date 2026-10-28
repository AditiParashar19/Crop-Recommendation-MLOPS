from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# 1. Test home endpoint
def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == (
        "Crop Recommendation API is running"
    )


# 2. Test health endpoint
def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["model_loaded"] is True


# 3. Test successful crop prediction
def test_predict_crop():
    payload = {
        "N": 90,
        "P": 42,
        "K": 43,
        "temperature": 20.87,
        "humidity": 82.0,
        "ph": 6.5,
        "rainfall": 202.93,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "recommended_crop" in data
    assert isinstance(data["recommended_crop"], str)
    assert data["recommended_crop"] != ""


# 4. Test prediction confidence
def test_prediction_confidence():
    payload = {
        "N": 90,
        "P": 42,
        "K": 43,
        "temperature": 20.87,
        "humidity": 82.0,
        "ph": 6.5,
        "rainfall": 202.93,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "confidence" in data
    assert isinstance(data["confidence"], (int, float))
    assert 0 <= data["confidence"] <= 1


# 5. Test missing input field
def test_missing_input():
    payload = {
        "N": 90,
        "P": 42,
        "K": 43,
        "temperature": 20.87,
        "humidity": 82.0,
        "ph": 6.5,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


# 6. Test invalid negative nitrogen value
def test_invalid_nitrogen():
    payload = {
        "N": -1,
        "P": 42,
        "K": 43,
        "temperature": 20.87,
        "humidity": 82.0,
        "ph": 6.5,
        "rainfall": 202.93,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


# 7. Test invalid humidity value
def test_invalid_humidity():
    payload = {
        "N": 90,
        "P": 42,
        "K": 43,
        "temperature": 20.87,
        "humidity": 150,
        "ph": 6.5,
        "rainfall": 202.93,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


# 8. Test invalid pH value
def test_invalid_ph():
    payload = {
        "N": 90,
        "P": 42,
        "K": 43,
        "temperature": 20.87,
        "humidity": 82.0,
        "ph": 15,
        "rainfall": 202.93,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


# 9. Test prediction with boundary values
def test_boundary_values():
    payload = {
        "N": 0,
        "P": 0,
        "K": 0,
        "temperature": 0,
        "humidity": 0,
        "ph": 0,
        "rainfall": 0,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data["recommended_crop"], str)


# 10. Test prediction response confidence range
def test_prediction_response_format():
    payload = {
        "N": 50,
        "P": 50,
        "K": 50,
        "temperature": 25,
        "humidity": 70,
        "ph": 6.0,
        "rainfall": 100,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert set(data.keys()) == {
        "recommended_crop",
        "confidence",
    }