from pydantic import BaseModel, Field, field_validator


class Geo(BaseModel):  # type: ignore[misc]
    lat: str = Field(..., description="Широта")
    lng: str = Field(..., description="Долгота")

    @field_validator("lat")
    @classmethod
    def validate_lat(cls, v: str) -> str:
        try:
            value = float(v)
        except ValueError:
            raise ValueError("lat должен быть числом (в виде строки)")
        if not -90 <= value <= 90:
            raise ValueError("lat должен быть в диапазоне от -90 до 90")
        return v

    @field_validator("lng")
    @classmethod
    def validate_lng(cls, v: str) -> str:
        try:
            value = float(v)
        except ValueError:
            raise ValueError("lng должен быть числом (в виде строки)")
        if not -180 <= value <= 180:
            raise ValueError("lng должен быть в диапазоне от -180 до 180")
        return v
