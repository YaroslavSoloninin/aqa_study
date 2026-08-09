from http import HTTPStatus

import pytest

from src.api.jsonplaceholder import JsonPlaceholderAPI
from src.models.post import Post
from tests.test_data.test_data import TestData


@pytest.mark.api
class TestJsonplaceholder:
    def test_get_post(self, json_placeholder_api: JsonPlaceholderAPI):
        get_post_response = json_placeholder_api.get_post_by_id(
            TestData.GET_POST_ID
        )
        print(get_post_response.data.title)
        assert get_post_response.status_code == HTTPStatus.OK

    def test_create_post(self, json_placeholder_api: JsonPlaceholderAPI):
        post = Post(
            userId=TestData.CREATE_POST_USER_ID,
            title=TestData.CREATE_POST_TITLE,
            body=TestData.CREATE_POST_BODY
        )
        create_post_response = json_placeholder_api.create_post(post)
        assert create_post_response.status_code == HTTPStatus.CREATED
