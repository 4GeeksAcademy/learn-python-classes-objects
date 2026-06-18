import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Address, Person, student


def test_student_is_person_instance():
    assert isinstance(student, Person)


def test_student_address_is_address_instance():
    assert isinstance(student.address, Address)


def test_full_address_format():
    assert student.full_address() == "Miami, USA"
