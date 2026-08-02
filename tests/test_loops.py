from src.tools.loops_practice import (
    get_day_name,
    get_max_value,
    get_long_words_count,
    load_imitation,
)


def test_get_day_name():
    assert get_day_name(1) == "Понедельник"
    assert get_day_name(2) == "Вторник"
    assert get_day_name(7) == "Воскресенье"
    assert get_day_name(-3) == "Неверный день недели"


def test_get_max_value():
    numbers = list(range(1, 8))
    assert get_max_value(numbers) == 5


def test_get_long_words_count():
    words = [f"str{i}" for i in range(11)]
    assert get_long_words_count(words, 5) == 1


def test_load_imitation():
    assert load_imitation() <= 10
