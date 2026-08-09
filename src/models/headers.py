from pydantic import BaseModel, ConfigDict, Field

from src.constants.content_type import ContentType


class Headers(BaseModel):  # type: ignore[misc]
    content_type: ContentType | str = Field(default=ContentType.JSON, alias="Content-Type")
    accept: ContentType | str = Field(default=ContentType.JSON, alias="Accept")
    model_config = ConfigDict(extra="allow")
