from src.tools.loops_practice import (
    get_day_name,
    get_max_value,
    get_long_words_count,
    load_imitation,
)
from tests.test_data.test_data import TestData


def test_get_day_name():
    assert get_day_name(1) == TestData.MONDAY
    assert get_day_name(2) == TestData.TUESDAY
    assert get_day_name(7) == TestData.SUNDAY
    assert get_day_name(-3) == TestData.WORD_DAY_OF_WEEK


def test_get_max_value():
    numbers = list(range(TestData.LIST_MIN_VALUE, TestData.LIST_MAX_VALUE))
    assert get_max_value(numbers) == TestData.MAX_NUMBER


def test_get_long_words_count():
    words = [f"str{i}" for i in range(10)]
    assert (
        get_long_words_count(words, TestData.LONG_WORD_LENGTH)
        == TestData.LONG_WORDS_COUNT
    )


def test_load_imitation():
    assert load_imitation() <= 10
