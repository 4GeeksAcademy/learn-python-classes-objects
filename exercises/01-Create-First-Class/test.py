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
