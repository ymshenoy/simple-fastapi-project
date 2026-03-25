from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Start session
db = SessionLocal()

# Query all vehicles
vehicles = db.query(models.Vehicle).all()

# Print nicely
for v in vehicles:
    print(f"ID: {v.id}, Brand: {v.brand}, Model: {v.model}, Mileage: {v.mileage}")

db.close()