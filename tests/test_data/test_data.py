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
    MONDAY = "Понедельник"
    TUESDAY = "Вторник"
    SUNDAY = "Воскресенье"
    WORD_DAY_OF_WEEK = "Неверный день недели"
    LIST_MIN_VALUE = 0
    LIST_MAX_VALUE = 9
    MAX_NUMBER = 5
    LONG_WORD_LENGTH = 5
    LONG_WORDS_COUNT = 0
    CAR1_BRAND = "Toyota"
    CAR1_MODEL = "Campy"
    CAR1_YEAR = 2022
    CAR2_BRAND = "BMW"
    CAR2_MODEL = "X5"
    CAR2_YEAR = 2023
    CAR3_BRAND = "Lada"
    CAR3_MODEL = "Vesta"
    CAR3_YEAR = 2021
    LEAD_NAME = "Иван"
    NEW_LEAD_NAME = "Петр"
    STUDENT1_NAME = "Анна"
    STUDENT1_AGE = 20
    STUDENT1_GRADES = [4.5, 5.0, 4.8]
    STUDENT2_NAME = "Борис"
    STUDENT2_AGE = 21
    STUDENT2_GRADES = [3.2, 4.0, 3.8]
    STUDENT3_NAME = "Вера"
    STUDENT3_AGE = 19
    STUDENT3_GRADES = [4.9, 5.0, 4.7]
    AVG_GRADE = 4.1
    EXPECTED_STUDENTS_COUNT = 2
    PRODUCT_ID = 1
    PRODUCTS_COUNT = 1
    KEY_PRODUCTS_NAMES = {"Blue Top", "Men Tshirt", "Stylish Dress"}
