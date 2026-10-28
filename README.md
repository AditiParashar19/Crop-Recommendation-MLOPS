# Crop Recommendation

An end-to-end Machine Learning application that predicts suitable crops based on soil nutrient levels and environmental conditions. The project integrates a trained Random Forest model with a FastAPI REST API, Docker containerization, automated testing, and GitHub Actions continuous integration.

## Overview

Selecting the right crop for specific soil and climatic conditions is an important aspect of agricultural planning. This project uses machine learning to analyze soil and environmental parameters and recommend a suitable crop.

The trained model is served through a RESTful API, allowing users and external applications to submit input parameters and receive crop predictions.

### Key Features

- **Machine Learning:** Random Forest classification for crop recommendation.
- **REST API:** FastAPI endpoints for predictions and health checks.
- **Input Validation:** Validates incoming data using Pydantic.
- **Model Persistence:** Stores the trained model and metadata for reuse.
- **Automated Testing:** Pytest-based tests for API functionality and input validation.
- **Docker Support:** Containerized application for consistent execution.
- **Continuous Integration:** GitHub Actions workflow for automated testing and Docker image builds.

## Dataset

The project uses the **Crop Recommendation Dataset** from Kaggle.

**Dataset source:** [Kaggle — Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

The dataset contains soil nutrient measurements and environmental attributes associated with different crop categories.

## Input Features

The model uses the following seven features:

| Feature | Description |
|---|---|
| `N` | Nitrogen content in the soil |
| `P` | Phosphorus content in the soil |
| `K` | Potassium content in the soil |
| `temperature` | Environmental temperature in °C |
| `humidity` | Relative humidity (%) |
| `ph` | Soil pH value |
| `rainfall` | Rainfall measurement |

**Target variable:** `label` — the crop category predicted by the model.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Pandas and NumPy | Data processing and numerical operations |
| Scikit-learn | Model training and prediction |
| Joblib | Model serialization and loading |
| FastAPI | REST API development |
| Uvicorn | ASGI server |
| Pydantic | Request validation |
| Pytest | Automated testing |
| Docker | Application containerization |
| GitHub Actions | Continuous integration |

## Project Structure

```text
crop-recommendation/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   └── main.py
├── artifacts/
│   ├── crop_model.joblib
│   └── model_metadata.json
├── tests/
│   └── test_api.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## Installation and Setup

### Prerequisites

Ensure the following tools are installed:

- Python 3.13
- pip
- Git
- Docker 

### 1. Clone the Repository

```bash
git clone https://github.com/AditiParashar19/Crop-Recommendation-MLOPS.git
```
### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv env-crop
.\env-crop\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn app.main:app --reload
```

The API will run locally at:

`http://127.0.0.1:8000`

### Available Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Returns the API welcome message |
| `GET` | `/health` | Checks API health |
| `POST` | `/predict` | Predicts a suitable crop |

### Example Prediction Request

Send a `POST` request to `/predict` with the following JSON payload:

```json
{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 20.8,
  "humidity": 82.0,
  "ph": 6.5,
  "rainfall": 202.9
}
```

## Model Training and Artifacts

The model is trained using the Crop Recommendation Dataset and a Random Forest Classifier.

### Training Configuration

| Parameter | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Number of estimators | 100 |
| Random state | 42 |
| Test set size | 20% |
| Stratified split | Enabled |

The trained model and associated metadata are stored in the `artifacts/` directory.

- `crop_model.joblib` — serialized machine learning model.
- `model_metadata.json` — model configuration and evaluation metadata.

The API loads the saved model at startup, avoiding the need to retrain it for each prediction request.

## Automated Testing

The project includes a Pytest test suite covering API behavior, prediction responses, and input validation.

Run the tests with:

```bash
python -m pytest -v
```

### Test Coverage

The current test suite includes checks for:

- Home endpoint response
- Health endpoint response
- Crop prediction
- Prediction confidence
- Missing required inputs
- Invalid nitrogen values
- Invalid humidity values
- Invalid pH values
- Boundary input values
- Prediction response structure

**Latest local test result:** 10 tests passed.

## Docker Deployment

Docker packages the application and its dependencies into a container, helping provide a consistent runtime environment.

### 1. Build the Docker Image

```bash
docker build -t crop-recommendation-api:latest .
```

### 2. Run the Container

```bash
docker run --rm -p 8000:8000 crop-recommendation-api:latest
```

### 3. Access the API

Open the interactive API documentation:

`http://127.0.0.1:8000/docs`

To stop the running container, press `Ctrl + C` in the terminal.

## Continuous Integration with GitHub Actions

The project includes a GitHub Actions workflow that runs when code is pushed to the `main` branch or a pull request targets `main`.

The workflow performs the following tasks:

1. Checks out the repository.
2. Sets up the Python environment.
3. Installs the required dependencies.
4. Executes the automated test suite.
5. Builds the Docker image.

The workflow helps identify application errors and integration issues before changes are merged.

**Workflow status:** Visit the repository's **Actions** tab to view the latest execution results.

## Author

**Aditi Parashar**

Machine Learning | Python | FastAPI | Docker | MLOps