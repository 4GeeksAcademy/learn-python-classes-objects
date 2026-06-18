# 10 Inheritance and reuse

## Goal

In this exercise, you will practice inheritance to reuse behavior across related classes.

## Key concept

Inheritance lets you define a base class with common behavior and extend it in subclasses.

## Instructions

Work in `app.py` and complete exactly the following:

1. Create a base class `Person` with `name` and `age`.
2. In `Person`, create a `describe()` method that returns: `"Name: <name>, Age: <age>"`.
3. Create a subclass `Student(Person)` with an extra `cohort` attribute.
4. In `Student`, override `describe()` to include cohort: `"Name: <name>, Age: <age>, Cohort: <cohort>"`.
5. Use `super()` to reuse `Person` initialization.
6. Create a global instance `student = Student("John", 21, "42")`.

## Success criteria

The exercise is correct when:

- `Student` inherits from `Person`.
- `student.describe()` returns the text with cohort.
- Base class behavior is properly reused.
