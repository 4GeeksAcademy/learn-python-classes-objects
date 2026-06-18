import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Person, Student, student


def test_student_inherits_from_person():
    assert isinstance(student, Student)
    assert isinstance(student, Person)


def test_describe_in_person():
    person = Person("Ana", 20)
    assert person.describe() == "Name: Ana, Age: 20"


def test_describe_in_student():
    assert student.describe() == "Name: John, Age: 21, Cohort: 42"
