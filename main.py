from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schema
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/vehicles", response_model=schema.VehicleResponse)
def create_vehicle(
    vehicle: schema.VehicleCreate,
    db: Session = Depends(get_db)
):

    db_vehicle = models.Vehicle(**vehicle.model_dump())

    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)

    return db_vehicle


@app.get("/add_vehicles", response_model=list[schema.VehicleResponse])
def get_vehicles(db: Session = Depends(get_db)):
    return db.query(models.Vehicle).all()