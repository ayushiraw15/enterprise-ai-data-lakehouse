# 🚀 Enterprise AI Data Lakehouse

An end-to-end Enterprise AI Data Lakehouse solution for Supply Chain Risk Prediction using **Python, Machine Learning, FastAPI, Docker, and AWS**.

This project demonstrates how modern enterprises can build a scalable data pipeline, clean and validate data, train machine learning models, expose predictions through REST APIs, and prepare the solution for cloud deployment.

---

# 📌 Project Overview

Supply chain disruptions can significantly impact business operations. This project predicts whether a shipment is **Normal** or **High Risk** based on logistics, transportation, and environmental factors.

The solution includes:

- Data Ingestion Pipeline
- Data Quality Profiling
- Data Cleaning & Validation
- Machine Learning Model Training
- FastAPI Prediction API
- Docker Containerization
- AWS Integration (S3, Athena)
- Interactive API Documentation (Swagger UI)

---

# 🏗️ Architecture

```
                CSV Dataset
                     │
                     ▼
           Data Ingestion Pipeline
                     │
                     ▼
      Data Cleaning & Validation
                     │
                     ▼
         Feature Engineering
                     │
                     ▼
      Random Forest ML Model
                     │
                     ▼
           FastAPI REST API
                     │
                     ▼
             Docker Container
                     │
                     ▼
             AWS Cloud Services
             (S3 • Athena)
```

---

# ⚙️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| API | FastAPI |
| API Documentation | Swagger UI |
| Model Serialization | Joblib |
| Cloud | AWS S3, AWS Athena |
| Containerization | Docker |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
enterprise-ai-data-lakehouse/

├── api/
├── athena/
├── data/
├── docker/
├── docs/
├── generator/
├── glue/
├── lambda/
├── ml/
├── pipeline/
├── preprocessing/
├── terraform/
├── tests/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🚀 Features

- End-to-End Data Pipeline
- Automated Data Cleaning
- Data Validation
- Machine Learning Risk Prediction
- REST API using FastAPI
- Dockerized Deployment
- Health Monitoring Endpoint
- Interactive Swagger Documentation
- Cloud Ready Architecture

---

# 🤖 Machine Learning

Model Used:

- Random Forest Classifier

Prediction Classes:

- ✅ Normal Shipment
- ⚠️ High Risk Shipment

---

# 🌐 API Endpoints

## Home

```
GET /
```

Response

```json
{
  "message": "Enterprise AI Data Lakehouse API is running!"
}
```

---

## Health Check

```
GET /health
```

Response

```json
{
  "status": "healthy",
  "api": "running",
  "model": "loaded",
  "version": "1.0"
}
```

---

## Prediction

```
POST /predict
```

Example Request

```json
{
  "Origin_Port": "Shanghai",
  "Destination_Port": "Singapore",
  "Transport_Mode": "Sea",
  "Product_Category": "Electronics",
  "Distance_km": 2500,
  "Weight_MT": 20,
  "Fuel_Price_Index": 105,
  "Geopolitical_Risk_Score": 2,
  "Weather_Condition": "Clear",
  "Carrier_Reliability_Score": 9,
  "Lead_Time_Days": 12
}
```

Example Response

```json
{
  "prediction": "Normal Shipment"
}
```

---

# 🐳 Docker

Build Image

```bash
docker build -t enterprise-ai-data-lakehouse .
```

Run Container

```bash
docker run -p 8000:8000 enterprise-ai-data-lakehouse
```

Swagger UI

```
http://localhost:8000/docs
```

---

# ☁️ AWS Services

- Amazon S3
- Amazon Athena
- AWS Glue *(Project Structure Included)*
- Terraform *(Infrastructure Folder Included)*

---

# 📸 Project Screenshots

Add the following screenshots:

- Swagger UI
- Prediction API Response
- Docker Running
- GitHub Repository
- AWS Athena Queries
- QuickSight Dashboard *(Optional)*

---

# 🎯 Future Improvements

- CI/CD using GitHub Actions
- Cloud Deployment (AWS ECS/App Runner)
- Model Monitoring
- Automated Retraining Pipeline
- Authentication & Authorization
- Logging & Metrics

---

# 👩‍💻 Author

**Ayushi Raizada**

GitHub:
https://github.com/ayushiraw15

---

# ⭐ If you found this project useful, don't forget to star the repository!
