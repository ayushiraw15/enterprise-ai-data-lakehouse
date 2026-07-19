import joblib
import pandas as pd

# Load model and encoders
model = joblib.load("ml/model.pkl")
encoders = joblib.load("ml/encoder.pkl")

# Sample shipment
shipment = {
    "Origin_Port": "Shanghai",
    "Destination_Port": "Singapore",
    "Transport_Mode": "Sea",
    "Product_Category": "Electronics",
    "Distance_km": 8500,
    "Weight_MT": 30,
    "Fuel_Price_Index": 105,
    "Geopolitical_Risk_Score": 4.2,
    "Weather_Condition": "Clear",
    "Carrier_Reliability_Score": 8.8,
    "Lead_Time_Days": 22
}

# Convert to DataFrame
df = pd.DataFrame([shipment])

# Encode categorical columns
categorical_columns = [
    "Origin_Port",
    "Destination_Port",
    "Transport_Mode",
    "Product_Category",
    "Weather_Condition"
]

for column in categorical_columns:
    if df[column][0] in encoders[column].classes_:
        df[column] = encoders[column].transform(df[column])
    else:
        print(f"Unknown value found in {column}: {df[column][0]}")
        exit()

# Prediction
prediction = model.predict(df)[0]

print("=" * 60)
print("SHIPMENT RISK PREDICTION")
print("=" * 60)

if prediction == 1:
    print("Prediction : HIGH RISK SHIPMENT")
else:
    print("Prediction : NORMAL SHIPMENT")