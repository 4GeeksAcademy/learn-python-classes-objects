# 04 Basic encapsulation

## Goal

In this exercise, you will practice encapsulation using internal attributes and controlled access methods.

## Key concept

In OOP, encapsulation protects object state so direct changes do not break consistency.

## Instructions

Work in `app.py` and complete exactly the following:

1. Create a `Person` class.
2. In `__init__`, receive `name` and `age`.
3. Store those values in internal attributes: `self._name` and `self._age`.
4. Create a `get_name()` method that returns the name.
5. Create a `get_age()` method that returns the age.
6. Create a `set_age(new_age)` method that:
   - updates age if `new_age` is greater than or equal to 0 and returns `True`.
   - changes nothing if `new_age` is less than 0 and returns `False`.
7. Create an instance `student = Person("John", 21)`.

## Success criteria

The exercise is correct when:

- `Person` uses `_name` and `_age` as internal state.
- `get_name()` and `get_age()` return correct values.
- `set_age()` validates and updates according to the rule.
