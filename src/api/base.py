import requests
from abc import ABC
from typing import Any, Type
from http import HTTPMethod
from src.utils.response import ApiResponse
from src.models.headers import Headers


class BaseAPI[T](ABC):
    def __init__(
            self, 
            base_url: str, 
            timeout: int,
            headers: Headers | None = None,
        ):
        self.__session = requests.Session()
        self.__base_url = base_url
        self.__headers = headers or Headers()
        self.__session.headers.update(self.__headers)
        self.__timeout = timeout
    
    def _get(
            self, 
            endpoint: str, 
            response_model: Type[T] | None = None,
            params: dict[str, Any] | None = None,
        ) -> ApiResponse[T]:
        return self.__request(HTTPMethod.GET, endpoint, response_model, params=params)

    def _post(
            self,
            endpoint: str,
            response_model: Type[T] | None = None,
            data: dict[str, Any] | None = None
        ) -> ApiResponse[T]:
        return self.__request(HTTPMethod.POST, endpoint, response_model, json=data)
    
    def __request(
            self,
            method: HTTPMethod,
            endpoint: str,
            response_model: Type[T] | None = None,
            **kwargs
        ) -> ApiResponse[T]:
        url = f"{self.__base_url}/{endpoint}"
        try:
            response = self.__session.request(
                method, 
                url, 
                timeout=self.__timeout, 
                **kwargs
            )
        except requests.exceptions.Timeout:
            raise RuntimeError("Сервер не ответил за 10 секунд") from None
        return ApiResponse.from_response(response, response_model)
