import os
import sys

import pytest

sys.path.append(os.path.dirname(__file__))

from app import Person, student


def test_valid_instance_exists():
    assert isinstance(student, Person)
    assert student.name == "John"
    assert student.age == 21


def test_invalid_name_raises_value_error():
    with pytest.raises(ValueError):
        Person("", 20)


def test_invalid_age_raises_value_error():
    with pytest.raises(ValueError):
        Person("Alice", -1)


def test_set_age_with_valid_value():
    student.set_age(25)
    assert student.age == 25


def test_set_age_with_invalid_value_raises_value_error():
    with pytest.raises(ValueError):
        student.set_age(-10)
