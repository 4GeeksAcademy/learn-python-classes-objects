# 09 Object collections

## Goal

In this exercise, you will practice managing collections of objects inside another class.

## Key concept

When a problem involves multiple objects of the same type, a container class helps centralize operations.

## Instructions

Work in `app.py` and complete exactly the following:

1. Create a `Person` class with `name` and `age`.
2. Create a `Classroom` class with an internal students list.
3. In `Classroom`, implement:
   - `add_student(person)`
   - `remove_student_by_name(name)` that returns `True` if removed, `False` otherwise.
   - `find_student(name)` that returns the object or `None`.
   - `total_students()` that returns the number of students.
4. Create an instance `bootcamp = Classroom()`.

## Success criteria

The exercise is correct when:

- Students can be added and removed correctly.
- Students can be found by name.
- `total_students()` reflects the real collection size.
