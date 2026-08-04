from urllib.parse import urljoin
from src.api.base import BaseAPI
from src.models.post import Post
from src.utils.response import ApiResponse
from src.models.empty_response import EmptyResponse


class JsonPlaceholderAPI(BaseAPI):

    __POSTS_ENDPOINT = "posts/"
    
    def get_post_by_id(self, id: int) -> ApiResponse[Post]:
        endpoint = urljoin(self.__POSTS_ENDPOINT, str(id))
        return self._get(endpoint, Post | EmptyResponse)

    def create_post(self, post: Post) -> ApiResponse[Post]:
        return self._post(self.__POSTS_ENDPOINT, Post, post.model_dump())
    