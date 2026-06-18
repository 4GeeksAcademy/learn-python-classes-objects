import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Person, student, student_clone


def test_string_representation():
    assert str(student) == "Person: John (21 years old)"


def test_repr_representation():
    assert repr(student) == "Person(name='John', age=21)"


def test_equality_between_instances():
    assert student == student_clone


def test_inequality_when_data_changes():
    another = Person("John", 22)
    assert student != another
