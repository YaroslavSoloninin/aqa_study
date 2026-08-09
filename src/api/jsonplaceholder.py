from urllib.parse import urljoin

from src.api.base import BaseAPI
from src.models.empty_response import EmptyResponse
from src.models.post import Post
from src.utils.response import ApiResponse


class JsonPlaceholderAPI(BaseAPI):

    __POSTS_ENDPOINT = "posts/"

    def get_post_by_id(self, id: int) -> ApiResponse[Post]:
        endpoint = urljoin(self.__POSTS_ENDPOINT, str(id))
        return self._get(endpoint, Post | EmptyResponse)

    def get_posts_by_user_id(self, user_id: int) -> ApiResponse[list[Post]]:
        return self._get(self.__POSTS_ENDPOINT, list[Post], params={"userId": user_id})

    def create_post(self, post: Post) -> ApiResponse[Post]:
        return self._post(self.__POSTS_ENDPOINT, Post, post.model_dump())

    def delete_post(self, id: int) -> ApiResponse[None]:
        endpoint = urljoin(self.__POSTS_ENDPOINT, str(id))
        return self._delete(endpoint)
