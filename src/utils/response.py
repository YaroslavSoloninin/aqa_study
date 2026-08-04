import requests
from typing import Type

from pydantic import TypeAdapter


class ApiResponse[T]:
    def __init__(
        self,
        response: requests.Response,
        data: T | None,
    ):
        self.__data: T | None = data
        self.__response = response

    @property
    def url(self):
        return self.__response.url

    @property
    def data(self) -> T | None:
        return self.__data
    
    @property
    def status_code(self) -> int:
        return self.__response.status_code
    
    @classmethod
    def from_response(
        cls,
        response: requests.Response,
        model_type: Type[T]
    ) -> "ApiResponse[T]":
        try:
            raw_data = response.json()
            adapter = TypeAdapter(model_type)
            parsed_data = adapter.validate_python(raw_data)
        except ValueError:
            parsed_data = None
        return cls(response=response, data=parsed_data)
