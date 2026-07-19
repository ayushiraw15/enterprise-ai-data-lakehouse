from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(
    title="Enterprise AI Data Lakehouse API",
    version="1.0"
)

# Load model and encoders
model = joblib.load("ml/model.pkl")
encoders = joblib.load("ml/encoder.pkl")


class Shipment(BaseModel):
    Origin_Port: str
    Destination_Port: str
    Transport_Mode: str
    Product_Category: str
    Distance_km: float
    Weight_MT: float
    Fuel_Price_Index: float
    Geopolitical_Risk_Score: float
    Weather_Condition: str
    Carrier_Reliability_Score: float
    Lead_Time_Days: float


@app.get("/")
def home():
    return {
        "message": "Enterprise AI Data Lakehouse API is running!"
    }


@app.post("/predict")
def predict(shipment: Shipment):

    data = pd.DataFrame([shipment.dict()])

    categorical_columns = [
        "Origin_Port",
        "Destination_Port",
        "Transport_Mode",
        "Product_Category",
        "Weather_Condition"
    ]

    for column in categorical_columns:

        value = data[column][0]

        if value not in encoders[column].classes_:
            return {
                "error": f"Unknown value '{value}' for {column}"
            }

        data[column] = encoders[column].transform(data[column])

    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "High Risk Shipment"
    else:
        result = "Normal Shipment"

    return {
        "prediction": result
    }