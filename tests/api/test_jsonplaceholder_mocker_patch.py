from http import HTTPStatus
from typing import Any
from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from src.api.jsonplaceholder import JsonPlaceholderAPI
from tests.test_data.test_data import TestData


@pytest.mark.api
class TestJsonplaceholder:
    @staticmethod
    def _make_mock_response(json_data: dict[str, Any], status_code: int) -> MagicMock:
        mock_response = MagicMock()
        mock_response.status_code = status_code
        mock_response.json.return_value = json_data
        return mock_response

    @pytest.mark.mock
    def test_get_post_mocked(
        self, json_placeholder_api: JsonPlaceholderAPI, mocker: MockerFixture
    ) -> None:
        mock_response = self._make_mock_response(
            TestData.FAKE_POST.model_dump(), HTTPStatus.OK
        )
        mocker.patch("requests.Session.request", return_value=mock_response)
        get_post_response = json_placeholder_api.get_post_by_id(TestData.GET_POST_ID)
        assert get_post_response.status_code == HTTPStatus.OK
        assert get_post_response.data is not None
        assert get_post_response.data.title == TestData.FAKE_POST.title

    @pytest.mark.mock
    def test_get_post_mocked_404(
        self, json_placeholder_api: JsonPlaceholderAPI, mocker: MockerFixture
    ) -> None:
        mock_response = self._make_mock_response(
            TestData.FAKE_POST.model_dump(), HTTPStatus.NOT_FOUND
        )
        mocker.patch("requests.Session.request", return_value=mock_response)
        get_post_response = json_placeholder_api.get_post_by_id(TestData.GET_POST_ID)

        assert get_post_response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.mock
    def test_get_post_mocked_500(
        self, json_placeholder_api: JsonPlaceholderAPI, mocker: MockerFixture
    ) -> None:
        mock_response = self._make_mock_response(
            TestData.FAKE_POST.model_dump(), HTTPStatus.INTERNAL_SERVER_ERROR
        )
        mocker.patch("requests.Session.request", return_value=mock_response)
        get_post_response = json_placeholder_api.get_post_by_id(TestData.GET_POST_ID)
        assert get_post_response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
