from pydantic import BaseModel, field_validator


class VehicleCreate(BaseModel):
    brand: str
    model: str
    mileage: int

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