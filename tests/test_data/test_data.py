from src.models.post import Post


class TestData:
    GET_POST_ID = 1
    GET_FIRST_POST_URL = "https://jsonplaceholder.typicode.com/posts/1"
    FAKE_POST = Post(userId=1, id=1, title="Mocked", body="Test")
    GET_POSTS_USER_ID = 1
    CREATE_POST_TITLE = "title"
    CREATE_POST_BODY = "body"
    CREATE_POST_USER_ID = 10
    DELETE_POST_ID = 1
    URL_AFTER_LOGIN = "https://www.saucedemo.com/inventory.html"
    WRONG_USERNAME = "dpsaiofj"
    WRONG_PASSWORD = "dspaoifjsdf"
    PARTIAL_ERROR_MESSAGE = "Epic sadface"
    PRODUCT_ID = 1
    PRODUCTS_COUNT = 1
    KEY_PRODUCTS_NAMES = {"Blue Top", "Men Tshirt", "Stylish Dress"}
