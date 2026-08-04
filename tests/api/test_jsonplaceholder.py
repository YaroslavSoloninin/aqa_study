from http import HTTPStatus

import pytest

from src.api.jsonplaceholder import JsonPlaceholderAPI
from src.models.post import Post
from tests.test_data.test_data import TestData


@pytest.mark.api
class TestJsonplaceholder:
    def test_get_post_by_id(self, json_placeholder_api: JsonPlaceholderAPI):
        get_post_response = json_placeholder_api.get_post_by_id(
            TestData.GET_POST_ID
        )
        assert get_post_response.status_code == HTTPStatus.OK
        assert get_post_response.data.id == TestData.GET_POST_ID

    def test_get_posts_by_user_id(self, json_placeholder_api: JsonPlaceholderAPI):
        get_posts_response = json_placeholder_api.get_posts_by_user_id(
            TestData.GET_POSTS_USER_ID
        )
        assert get_posts_response.status_code == HTTPStatus.OK
        for post in get_posts_response.data:
            assert post.userId == TestData.GET_POSTS_USER_ID

    def test_create_post(self, json_placeholder_api: JsonPlaceholderAPI):
        post = Post(
            userId=TestData.CREATE_POST_USER_ID,
            title=TestData.CREATE_POST_TITLE,
            body=TestData.CREATE_POST_BODY
        )
        create_post_response = json_placeholder_api.create_post(post)
        assert create_post_response.status_code == HTTPStatus.CREATED
        assert create_post_response.data.userId == TestData.CREATE_POST_USER_ID
        assert create_post_response.data.title == TestData.CREATE_POST_TITLE
        assert create_post_response.data.body == TestData.CREATE_POST_BODY

    def test_delete_post(self, json_placeholder_api: JsonPlaceholderAPI):
        delete_post_response = json_placeholder_api.delete_post(
            TestData.DELETE_POST_ID
        )
        assert delete_post_response.status_code == HTTPStatus.OK
