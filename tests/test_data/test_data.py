from src.models.post import Post


class TestData:
    GET_POST_ID = 1
    GET_FIRST_POST_URL = "https://jsonplaceholder.typicode.com/posts/1"
    FAKE_POST = Post(userId=1, id=1, title="Mocked", body="Test")            
