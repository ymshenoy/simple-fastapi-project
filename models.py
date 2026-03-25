from sqlalchemy import Column, String, Integer
from database import Base
import uuid


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    brand = Column(String)
    model = Column(String)
    mileage = Column(Integer)