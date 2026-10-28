# Crop Recommendation API

An end-to-end machine learning project that recommends a crop based on soil nutrients and environmental conditions.

## Dataset

[Kaggle Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

## Technologies

- Python
- Pandas and NumPy
- Scikit-learn
- Joblib
- FastAPI
- Pytest
- Docker
- GitHub Actions

## Input Features

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Health check |
| POST | `/predict` | Predict a recommended crop |

## Run Locally

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to test the endpoints.

## Run Tests

```bash
python -m pytest -v
```

## Run with Docker

Build the image:

```bash
docker build -t crop-recommendation-api:latest .
```

Start the container:

```bash
docker run --rm -p 8000:8000 crop-recommendation-api:latest
```

## Model Artifacts

The `artifacts/` directory contains the trained model and its metadata.

## Continuous Integration

GitHub Actions runs the automated tests and builds the Docker image when code is pushed or a pull request is opened.

## Disclaimer

This model learns from the supplied dataset. Its predictions should not be treated as a substitute for local agronomic expertise or soil testing.