import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Person, student


def test_population_starts_with_existing_instance():
    assert isinstance(student, Person)
    assert Person.get_population() >= 1


def test_population_increases_with_new_instances():
    previous = Person.get_population()
    Person("Alice", 30)
    assert Person.get_population() == previous + 1


def test_static_method_is_adult():
    assert Person.is_adult(21) is True
    assert Person.is_adult(17) is False
