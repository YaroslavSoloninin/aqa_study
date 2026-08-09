import random
import time


def get_day_name(day: int) -> str:
    days = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье",
    }
    return days[day] if day in days else "Неверный день недели"


def get_max_value(nums: list) -> int | float:
    if not nums:
        return 0
    max_value = nums[0]
    for n in nums:
        if n > max_value:
            max_value = n
        if n == 5:
            break
    return max_value


def get_long_words_count(words: list, length: int) -> int:
    count = 0
    for w in words:
        if len(w) >= length:
            count += 1
    return count


def load_imitation() -> int:
    MIN_LOAD = 0
    MAX_LOAD = 100
    LOOP_COUNT = 10
    DELAY_SECONDS = 0.2
    for _ in range(LOOP_COUNT):
        messages_count = 0
        load = random.randint(MIN_LOAD, MAX_LOAD)
        if load > 85:
            messages_count += 1
            print("Нагрузка слишком высокая")
        time.sleep(DELAY_SECONDS)
    return messages_count
