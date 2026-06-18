import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Person, student


def test_person_class_exists():
    assert Person is not None
    assert isinstance(Person, type)


def test_internal_attributes_exist():
    assert hasattr(student, "_name")
    assert hasattr(student, "_age")


def test_getters_return_expected_values():
    assert student.get_name() == "John"
    assert student.get_age() == 21


def test_set_age_with_valid_value_updates_age():
    result = student.set_age(22)
    assert result is True
    assert student.get_age() == 22


def test_set_age_with_invalid_value_keeps_previous_age():
    previous_age = student.get_age()
    result = student.set_age(-1)
    assert result is False
    assert student.get_age() == previous_age
