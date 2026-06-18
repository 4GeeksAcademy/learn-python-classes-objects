import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Person, student


def test_person_class_exists():
    assert Person is not None
    assert isinstance(Person, type)


def test_student_is_instance_of_person():
    assert student is not None
    assert isinstance(student, Person)


def test_greet_method_returns_expected_message():
    assert hasattr(student, "greet")
    assert callable(student.greet)
    assert student.greet() == "Hi, my name is John"


def test_have_birthday_increases_age_by_one():
    assert hasattr(student, "have_birthday")
    assert callable(student.have_birthday)
    previous_age = student.age
    student.have_birthday()
    assert student.age == previous_age + 1
