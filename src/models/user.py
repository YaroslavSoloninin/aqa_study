from pydantic import BaseModel, EmailStr, Field, field_validator

from src.models.address import Address
from src.models.company import Company


class User(BaseModel):  # type: ignore[misc]
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1, max_length=150)
    username: str = Field(..., min_length=1, max_length=50)
    email: EmailStr = Field(...)
    address: Address
    phone: str = Field(..., min_length=1, max_length=50)
    website: str = Field(..., min_length=1, max_length=200)
    company: Company

    @field_validator("name", "username")
    @classmethod
    def not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Поле не может быть пустым или состоять из пробелов")
        return v.strip()

    @field_validator("username")
    @classmethod
    def username_format(cls, v: str) -> str:
        if " " in v:
            raise ValueError("username не должен содержать пробелы")
        return v
