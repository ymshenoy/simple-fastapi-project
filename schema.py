from pydantic import BaseModel, field_validator, Field
from datetime import datetime, timedelta
import random

def random_registration_date(start_year=2015, end_year=datetime.now().year):
    """
    Returns a random datetime.date between Jan 1 of start_year and today.
    """
    start = datetime(start_year, 1, 1)
    end = datetime.now()
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)

class VehicleCreate(BaseModel):
    brand: str
    model: str
    mileage: int
    registration_date: datetime = Field(default_factory= random_registration_date)

    @field_validator("mileage")
    @classmethod
    def validate_mileage(cls, v):
        if v < 0:
            raise ValueError("Mileage cannot be negative")
        return v

class VehicleResponse(BaseModel):
    id: str
    brand: str
    model: str
    mileage: int

    class Config:
        from_attributes = True

# Service record schemas
class ServiceRecordBase(BaseModel):
    service_type: str
    service_date: datetime
    mileage: int
    next_service_due: datetime | None = None

class ServiceRecordCreate(ServiceRecordBase):
    vehicle_id: str  # link service record to a vehicle

class ServiceRecordResponse(ServiceRecordBase):
    id: str
    vehicle_id: str

    class Config:
        from_attributes = True

class VehicleWithService(BaseModel):
    vehicle: VehicleResponse
    service_records: list[ServiceRecordResponse]

    class Config:
        from_attributes = True
