# 06 Special methods

## Goal

In this exercise, you will practice special methods to represent and compare objects.

## Key concept

Special methods help your classes integrate naturally with Python.

## Instructions

Work in `app.py` and complete exactly the following:

1. Create a `Person` class with `name` and `age`.
2. Implement `__str__` to return: `"Person: <name> (<age> years old)"`.
3. Implement `__repr__` to return: `"Person(name='<name>', age=<age>)"`.
4. Implement `__eq__` so two people are equal if they have the same `name` and `age`.
5. Create these instances:
   - `student = Person("John", 21)`
   - `student_clone = Person("John", 21)`

## Success criteria

The exercise is correct when:

- `str(student)` returns the expected format.
- `repr(student)` returns the expected format.
- `student == student_clone` is `True`.
