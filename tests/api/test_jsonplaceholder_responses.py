from http import HTTPStatus

import pytest
import responses

from src.api.jsonplaceholder import JsonPlaceholderAPI
from tests.test_data.test_data import TestData


@pytest.mark.api
@pytest.mark.mock
class TestJsonplaceholder:
    @responses.activate
    def test_get_post_mocked(self, json_placeholder_api: JsonPlaceholderAPI) -> None:
        responses.add(
            responses.GET,
            TestData.GET_FIRST_POST_URL,
            json=TestData.FAKE_POST.model_dump(),
            status=HTTPStatus.OK,
        )
        get_post_response = json_placeholder_api.get_post_by_id(TestData.GET_POST_ID)
        assert get_post_response.status_code == HTTPStatus.OK
        assert get_post_response.data is not None
        assert get_post_response.data.title == TestData.FAKE_POST.title

    @responses.activate
    def test_get_post_mocked_404(self, json_placeholder_api: JsonPlaceholderAPI) -> None:
        responses.add(
            responses.GET,
            TestData.GET_FIRST_POST_URL,
            json=TestData.FAKE_POST.model_dump(),
            status=HTTPStatus.NOT_FOUND,
        )
        get_post_response = json_placeholder_api.get_post_by_id(TestData.GET_POST_ID)
        assert get_post_response.status_code == HTTPStatus.NOT_FOUND

    @responses.activate
    def test_get_post_mocked_500(self, json_placeholder_api: JsonPlaceholderAPI) -> None:
        responses.add(
            responses.GET,
            TestData.GET_FIRST_POST_URL,
            json=TestData.FAKE_POST.model_dump(),
            status=HTTPStatus.INTERNAL_SERVER_ERROR,
        )
        get_post_response = json_placeholder_api.get_post_by_id(TestData.GET_POST_ID)
        assert get_post_response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
