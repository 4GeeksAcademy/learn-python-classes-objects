import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Classroom, Person, bootcamp


def test_bootcamp_is_classroom_instance():
    assert isinstance(bootcamp, Classroom)


def test_add_and_total_students():
    classroom = Classroom()
    initial = classroom.total_students()
    classroom.add_student(Person("Ana", 20))
    assert classroom.total_students() == initial + 1


def test_find_student_by_name():
    classroom = Classroom()
    classroom.add_student(Person("Luis", 23))
    found = classroom.find_student_by_name("Luis")
    assert found is not None
    assert found.name == "Luis"


def test_remove_student_by_name():
    classroom = Classroom()
    classroom.add_student(Person("Eva", 22))
    removed = classroom.remove_student_by_name("Eva")
    assert removed is True
    assert classroom.find_student_by_name("Eva") is None
