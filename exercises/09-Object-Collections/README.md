# 09 Object collections

## Goal

In this exercise, you will practice managing collections of objects inside another class.

## Key concept

When a problem involves multiple objects of the same type, a container class helps centralize operations.

## Instructions

Work in `app.py` and complete exactly the following:

1. Create a `Person` class with `name` and `age`.
2. Create a `Classroom` class and, inside `__init__`, initialize an empty list to store students (for example: `self.students = []`).
3. In `Classroom`, implement:
   - `add_student(person)` to append a `Person` instance to the end of the list.
   - `remove_student_by_name(name)` to remove the first matching student by name and return `True`; if not found, return `False`.
   - `find_student_by_name(name)` to return the first matching student by name or `None`.
   - `total_students()` that returns the number of students.
4. Create an instance `bootcamp = Classroom()`.

Note: for this exercise, no extra type validation is required; focus on collection logic.

## Success criteria

The exercise is correct when:

- Students can be added and removed correctly.
- Students can be found by name.
- `total_students()` reflects the real collection size.
- `Classroom` keeps its collection in an internal list initialized in `__init__`.
