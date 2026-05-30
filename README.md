# IoT-Based Healthcare Monitoring System

## Overview

This project implements an IoT-Based Healthcare Monitoring System that simulates real-time patient monitoring using IoT communication, database storage, REST APIs, and graphical visualization.

The system generates patient health parameters such as heart rate, body temperature, and SpO2 levels, transmits the data using MQTT, stores it in a database, and provides APIs and visualizations for monitoring patient health trends.

The project demonstrates the integration of IoT technologies with backend development and healthcare analytics in a complete end-to-end workflow.

---

## Technologies Used

* Python
* MQTT
* Mosquitto Broker
* FastAPI
* SQLite
* SQLAlchemy
* Matplotlib

---

## System Architecture

The system follows a real-time healthcare monitoring workflow.

1. Simulated IoT devices generate patient health data.
2. The generated sensor readings are transmitted through the MQTT protocol using the Mosquitto broker.
3. The subscriber service receives incoming sensor data and performs anomaly detection.
4. The processed data is stored in an SQLite database.
5. FastAPI provides REST APIs for accessing patient records.
6. Matplotlib generates visualizations for health monitoring and trend analysis.

Overall Workflow:

Device Simulator → MQTT Broker → Subscriber Service → SQLite Database → FastAPI APIs → Graph Visualization

---

## Features

* Real-time simulation of patient healthcare data.
* MQTT-based publish-subscribe communication architecture.
* Storage of healthcare records using SQLite and SQLAlchemy.
* Automated anomaly detection for abnormal health conditions.
* RESTful API development using FastAPI.
* Swagger/OpenAPI documentation support.
* Generation of health monitoring visualizations.
* Time-series analysis of patient vital signs.

---

## Project Workflow

### Step 1: Device Simulation

The `device.py` module acts as a simulated IoT healthcare device.

It continuously generates healthcare parameters for multiple patients, including:

* Heart Rate
* Body Temperature
* SpO2 (Oxygen Saturation)

The generated data mimics real-world healthcare sensor readings.

---

### Step 2: MQTT Communication

The project uses MQTT (Message Queuing Telemetry Transport) for communication between devices and backend services.

Mosquitto Broker acts as the message broker.

Patient health data is published to the topic:

```text
health/sensors
```

This enables efficient and lightweight communication commonly used in IoT systems.

---

### Step 3: Data Processing and Storage

The `subscriber.py` module subscribes to the MQTT topic and receives incoming healthcare data.

The received records are processed and stored in an SQLite database using SQLAlchemy.

Stored information includes:

* Patient ID
* Heart Rate
* Temperature
* SpO2

The system also performs anomaly detection by monitoring abnormal healthcare conditions such as:

* High heart rate
* Elevated body temperature
* Low oxygen saturation levels

Alert messages are generated whenever abnormal values are detected.

---

### Step 4: REST API Development

FastAPI is used to develop backend APIs for accessing healthcare records.

Available API endpoints include:

#### Get Application Status

```http
GET /
```

#### Retrieve All Patient Records

```http
GET /data
```

#### Retrieve Latest Patient Records

```http
GET /latest
```

Interactive API documentation is automatically generated using Swagger UI and can be accessed through:

```text
http://127.0.0.1:8000/docs
```

---

### Step 5: Data Visualization

The `graph.py` module generates visualizations using Matplotlib.

Patient health data is retrieved from the database and used to create graphs for:

* Heart Rate
* Temperature
* SpO2

Generated output files:

* heart_rate.png
* temperature.png
* spo2.png

These visualizations help monitor patient health trends and identify abnormal patterns.

---

## Future Enhancements

Possible future improvements include:

* Machine Learning-based health risk prediction
* Predictive healthcare analytics
* Integration with physical IoT sensors

---

## Author

**Kolla Taruni Venkata Ruchita**

B.Tech in Artificial Intelligence
Mahindra University



