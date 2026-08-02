from src.models import Car, Lead, Student
from src.tools.changer import Changer


def test_car():
    car1 = Car("Toyota", "Camry", 2022)
    car2 = Car("BMW", "X5", 2023)
    car3 = Car("Lada", "Vesta", 2021)
    car1.print_car_info()
    car2.print_car_info()
    car3.print_car_info()
    assert car1.brand == "Toyota"
    assert car2.model == "X5"
    assert car3.year == 2021


def test_change_lead_name():
    lead = Lead("Иван")
    assert lead.name == "Иван"
    Changer.change_lead_name(lead, "Пётр")
    assert lead.name == "Пётр"


def test_student():
    students = [
        Student("Анна", 20, [4.5, 5.0, 4.8]),
        Student("Борис", 21, [3.2, 4.0, 3.8]),
        Student("Вера", 19, [4.9, 5.0, 4.7]),
    ]
    good_students = [s for s in students if s.get_avg_grade() > 4.1]
    assert len(good_students) == 2
