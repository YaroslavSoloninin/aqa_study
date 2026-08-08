from src.models import Car, Lead, Student
from src.tools.changer import Changer
from tests.test_data.test_data import TestData as TD


def test_car():
    car1 = Car(TD.CAR1_BRAND, TD.CAR1_MODEL, TD.CAR1_YEAR)
    car2 = Car(TD.CAR2_BRAND, TD.CAR2_MODEL, TD.CAR2_YEAR)
    car3 = Car(TD.CAR3_BRAND, TD.CAR3_MODEL, TD.CAR3_YEAR)
    car1.print_car_info()
    car2.print_car_info()
    car3.print_car_info()
    assert car1.brand == TD.CAR1_BRAND
    assert car2.model == TD.CAR2_MODEL
    assert car3.year == TD.CAR3_YEAR


def test_change_lead_name():
    lead = Lead(TD.LEAD_NAME)
    assert lead.name == TD.LEAD_NAME
    Changer.change_lead_name(lead, TD.NEW_LEAD_NAME)
    assert lead.name == TD.NEW_LEAD_NAME


def test_student():
    students = [
        Student(TD.STUDENT1_NAME, TD.STUDENT1_AGE, TD.STUDENT1_GRADES),
        Student(TD.STUDENT2_NAME, TD.STUDENT2_AGE, TD.STUDENT2_GRADES),
        Student(TD.STUDENT3_NAME, TD.STUDENT3_AGE, TD.STUDENT3_GRADES),
    ]
    good_students = [s for s in students if s.get_avg_grade() > TD.AVG_GRADE]
    assert len(good_students) == TD.EXPECTED_STUDENTS_COUNT
