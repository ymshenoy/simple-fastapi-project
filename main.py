from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import models
import schema
from database import engine, SessionLocal

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vehicle Service Tracker")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Server is running!"}


# ---------------- Vehicles ----------------
@app.post("/vehicles", response_model=schema.VehicleResponse)
def create_vehicle(vehicle: schema.VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = models.Vehicle(**vehicle.model_dump())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


@app.get("/vehicles", response_model=list[schema.VehicleResponse])
def get_vehicles(db: Session = Depends(get_db)):
    return db.query(models.Vehicle).all()


@app.put("/vehicles/{vehicle_id}", response_model=schema.VehicleResponse)
def update_vehicle(vehicle_id: str, vehicle_update: schema.VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    db_vehicle.brand = vehicle_update.brand
    db_vehicle.model = vehicle_update.model
    db_vehicle.mileage = vehicle_update.mileage
    db_vehicle.registration_date = vehicle_update.registration_date

    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


# ---------------- Service Records ----------------
@app.post("/service", response_model=schema.ServiceRecordResponse)
def add_service(record: schema.ServiceRecordCreate, db: Session = Depends(get_db)):
    # Automatically calculate next_service_due: 10 days after service_date
    record_data = record.model_dump()
    record_data['next_service_due'] = record_data['service_date'] + timedelta(days=10)

    db_record = models.ServiceRecord(**record_data)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@app.get("/service", response_model=list[schema.ServiceRecordResponse])
def get_service_records(vehicle_id: str | None = Query(None), db: Session = Depends(get_db)):
    query = db.query(models.ServiceRecord)
    if vehicle_id:
        query = query.filter(models.ServiceRecord.vehicle_id == vehicle_id)
    return query.all()

###Update the service record
@app.put("/service/{service_id}", response_model=schema.ServiceRecordResponse)
def update_service_records(service_id: str, service_record_update: schema.ServiceRecordCreate, db: Session = Depends(get_db)):
    db_record = db.query(models.ServiceRecord).filter(models.ServiceRecord.id == service_id).first()
    if not db_record:
        raise HTTPException(status_code=404, detail="Service Record for this vehicle not found")

    db_record.service_type = service_record_update.service_type
    db_record.service_date = service_record_update.service_date
    db_record.mileage = service_record_update.mileage
    db_record.next_service_due = service_record_update.service_date + timedelta(days=10)

    db.commit()
    db.refresh(db_record)
    return db_record

@app.get("/vehicles/model/{model}", response_model=list[schema.VehicleWithService])
def get_details(model: str, db: Session = Depends(get_db)):

    results = (
        db.query(models.Vehicle, models.ServiceRecord)
        .join(
            models.ServiceRecord,
            models.Vehicle.id == models.ServiceRecord.vehicle_id
        )
        .filter(models.Vehicle.model == model)
        .all()
    )

    response = []

    for vehicle, service in results:
        response.append({
            "vehicle": vehicle,
            "service_records": [service]   # ← MUST be plural
        })

    return response