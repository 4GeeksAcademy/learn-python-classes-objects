import os
import sys

import pytest

sys.path.append(os.path.dirname(__file__))

from app import Animal, Cat, Dog, cat, dog, make_it_speak


def test_animal_base_contract():
    with pytest.raises(NotImplementedError):
        Animal().speak()


def test_dog_and_cat_instances():
    assert isinstance(dog, Dog)
    assert isinstance(cat, Cat)


def test_polymorphic_function_for_different_types():
    assert make_it_speak(dog) == "Woof"
    assert make_it_speak(cat) == "Meow"
