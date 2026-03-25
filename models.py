from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import uuid
from datetime import datetime


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    mileage = Column(Integer, default=0)
    registration_date = Column(DateTime, default=datetime.utcnow)

    # Relationship: one vehicle has many service records
    services = relationship("ServiceRecord", back_populates="vehicle", cascade="all, delete-orphan")



class ServiceRecord(Base):
    __tablename__ = "service_records"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    vehicle_id = Column(String, ForeignKey("vehicles.id"), nullable=False)
    service_type = Column(String, nullable=False)
    service_date = Column(DateTime, default=datetime.utcnow)
    mileage = Column(Integer, nullable=False)
    next_service_due = Column(DateTime, nullable=True)

    # Relationship back to vehicle
    vehicle = relationship("Vehicle", back_populates="services")