from pydantic import BaseModel, Field, field_validator

from src.models.geo import Geo


class Address(BaseModel):  # type: ignore[misc]
    street: str = Field(..., min_length=1, max_length=200)
    suite: str = Field(..., min_length=1, max_length=50)
    city: str = Field(..., min_length=1, max_length=100)
    zipcode: str = Field(..., description="Почтовый индекс")
    geo: Geo

    @field_validator("street", "suite", "city")
    @classmethod
    def not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Поле не может быть пустым или состоять из пробелов")
        return v.strip()
