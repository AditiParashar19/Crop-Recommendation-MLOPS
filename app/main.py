from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "artifacts" / "crop_model.joblib"

FEATURES = [
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall",
]

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="Crop Recommendation API",
    description="Predict a suitable crop using soil and weather parameters.",
    version="1.0.0",
)


class CropInput(BaseModel):
    N: float = Field(ge=0, le=200)
    P: float = Field(ge=0, le=200)
    K: float = Field(ge=0, le=300)
    temperature: float = Field(ge=-10, le=60)
    humidity: float = Field(ge=0, le=100)
    ph: float = Field(ge=0, le=14)
    rainfall: float = Field(ge=0, le=1000)


@app.get("/")
def home():
    return {
        "message": "Crop Recommendation API is running",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
    }


@app.post("/predict")
def predict_crop(data: CropInput):
    try:
        input_data = pd.DataFrame(
            [[
                data.N,
                data.P,
                data.K,
                data.temperature,
                data.humidity,
                data.ph,
                data.rainfall,
            ]],
            columns=FEATURES,
        )

        prediction = model.predict(input_data)[0]

        result = {
            "recommended_crop": str(prediction),
        }

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0]
            result["confidence"] = round(
                float(probabilities.max()), 4
            )

        return result

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed.",
        ) from exc
