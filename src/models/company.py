from pydantic import BaseModel, Field, field_validator


class Company(BaseModel):  # type: ignore[misc]
    name: str = Field(..., min_length=1, max_length=150)
    catchPhrase: str = Field(..., min_length=1, max_length=200)
    bs: str = Field(..., min_length=1, max_length=200)

    @field_validator("name", "catchPhrase", "bs")
    @classmethod
    def not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Поле не может быть пустым или состоять из пробелов")
        return v.strip()

    @field_validator("name")
    @classmethod
    def name_format(cls, v: str) -> str:
        if v[0].isdigit():
            raise ValueError("Название компании не должно начинаться с цифры")
        return v
