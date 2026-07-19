import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


# Load processed dataset
df = pd.read_csv("data/processed/clean_supply_chain.csv")


# Encode categorical columns
encoders = {}

categorical_columns = [
    "Origin_Port",
    "Destination_Port",
    "Transport_Mode",
    "Product_Category",
    "Weather_Condition"
]

for column in categorical_columns:
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    encoders[column] = encoder


# Features
X = df.drop(columns=[
    "Shipment_ID",
    "Date",
    "Disruption_Occurred"
])

# Target
y = df["Disruption_Occurred"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# Predictions
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("=" * 60)
print("MODEL TRAINED SUCCESSFULLY")
print("=" * 60)
print(f"Accuracy : {accuracy:.2%}")


# Save model
joblib.dump(model, "ml/model.pkl")
joblib.dump(encoders, "ml/encoder.pkl")

print("\nModel Saved Successfully!")