import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Person, student


def test_person_class_exists():
    assert Person is not None
    assert isinstance(Person, type)


def test_person_constructor_assigns_attributes():
    person = Person("Alice", 30)
    assert hasattr(person, "name")
    assert hasattr(person, "age")
    assert person.name == "Alice"
    assert person.age == 30


def test_student_instance_values():
    assert student is not None
    assert isinstance(student, Person)
    assert student.name == "John"
    assert student.age == 21
