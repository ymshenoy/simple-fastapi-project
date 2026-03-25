# 🚗 Vehicle Service Tracker API

A simple and practical **FastAPI** project for tracking vehicle information, mileage, and service history.
This project demonstrates **FastAPI**, **Pydantic**, and **SQLite database integration** using **SQLAlchemy**.

This is a beginner-friendly **automotive-related backend project** with clean architecture and real-world use cases.

---

# 📌 Features

* Add vehicles
* Track mileage
* Store vehicle data in database
* Input validation using Pydantic
* SQLite database (free & lightweight)
* REST API endpoints
* Auto-generated API documentation

---

# 🛠️ Tech Stack

* FastAPI
* Pydantic
* SQLAlchemy
* SQLite
* Uvicorn

---

# 📁 Project Structure

```
vehicle-service-tracker/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

### 1. Clone Repository

```bash
git clone <this repository>
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Server

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API docs:

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📌 API Endpoints

## Add Vehicle

```
POST /vehicles
```

### Request

```json
{
  "brand": "Toyota",
  "model": "Corolla",
  "mileage": 50000
}
```

---

## Get All Vehicles

```
GET /vehicles
```

---

# 🧠 Pydantic Features Used

This project demonstrates:

* Pydantic Models
* Field Validators
* Response Models
* Data Serialization
* Input Validation

Example:

```python
@field_validator("mileage")
@classmethod
def validate_mileage(cls, v):
    if v < 0:
        raise ValueError("Mileage cannot be negative")
    return v
```

---

# 🗄️ Database

This project uses **SQLite**, a lightweight, file-based database.

Database file will be automatically created:

```
vehicles.db
```

No installation required.

---

# 📌 Example Response

```json
{
  "id": "d92d3f3c",
  "brand": "Toyota",
  "model": "Corolla",
  "mileage": 50000
}
```

---

# 🔮 Future Improvements

* Add service history
* Add service reminders
* Add vehicle owners
* Add maintenance alerts
* Add authentication
* Add pagination
* Add filtering

---

# 🎯 Learning Goals

This project helps practice:

* FastAPI fundamentals
* Pydantic validation
* SQLite database integration
* SQLAlchemy ORM
* REST API design

---

# 👨‍💻 Author

Madhavi Shenoy

---

# ⭐ If you found this helpful

Give the repo a star ⭐
