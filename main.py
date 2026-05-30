from fastapi import FastAPI
from db import Session, HealthData

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Health Monitoring API Running"}

@app.get("/data")
def get_data():
    session = Session()
    data = session.query(HealthData).all()

    result = []
    for row in data:
        result.append({
            "id": row.id,
            "device_id": row.device_id,
            "heart_rate": row.heart_rate,
            "temperature": row.temperature,
            "spo2": row.spo2
        })

    return result

@app.get("/latest")
def latest_data():
    session = Session()
    data = session.query(HealthData).order_by(HealthData.id.desc()).limit(5).all()

    result = []
    for row in data:
        result.append({
            "id": row.id,
            "device_id": row.device_id,
            "heart_rate": row.heart_rate,
            "temperature": row.temperature,
            "spo2": row.spo2
        })

    return result
