import pytest
from src.api.jsonplaceholder import JsonPlaceholderAPI
from src.config import Config


@pytest.fixture
def json_placeholder_api() -> JsonPlaceholderAPI:
    return JsonPlaceholderAPI(Config.BASE_URL, Config.TIMEOUT)
