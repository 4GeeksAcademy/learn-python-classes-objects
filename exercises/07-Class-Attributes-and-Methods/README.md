# 07 Class attributes and class methods

## Goal

In this exercise, you will differentiate shared class state from instance behavior.

## Key concept

A class attribute is shared by all instances.

Class methods work with class-wide data, and static methods are related utility behavior.

## Instructions

Work in `app.py` and complete exactly the following:

1. Create a `Person` class.
2. Add a class attribute `population = 0`.
3. In `__init__(name, age)`, store `name` and `age`, and increment `Person.population` by 1.
4. Create a class method `get_population()` that returns `population`.
5. Create a static method `is_adult(age)` that returns `True` if `age >= 18`, otherwise `False`.
6. Create a global instance `student = Person("John", 21)`.

## Success criteria

The exercise is correct when:

- `population` increases when new instances are created.
- `get_population()` reflects the total number of created instances.
- `is_adult()` works for adult and non-adult ages.
