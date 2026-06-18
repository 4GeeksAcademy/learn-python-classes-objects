# 05 Data validation

## Goal

In this exercise, you will practice validating data to keep objects in a valid state.

## Key concept

In OOP, validating in constructors and update methods prevents inconsistent objects.

## Instructions

Work in `app.py` and complete exactly the following:

1. Create a `Person` class.
2. In `__init__`, receive `name` and `age`.
3. Validate that:
   - `name` is a non-empty string.
   - `age` is an integer greater than or equal to 0.
4. If any value is invalid, raise `ValueError`.
5. Create a `set_age(new_age)` method that applies the same age validation and updates the value.
6. Create one valid instance: `student = Person("John", 21)`.

## Success criteria

The exercise is correct when:

- Valid people can be created.
- Invalid inputs raise `ValueError`.
- `set_age()` updates only when age is valid.
