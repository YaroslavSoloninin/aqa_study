from pydantic import BaseModel


class EmptyResponse(BaseModel):  # type: ignore[misc]
    pass
