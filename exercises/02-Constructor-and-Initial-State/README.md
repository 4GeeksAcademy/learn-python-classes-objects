# 02 Constructor and initial state

## Goal

In this exercise, you will learn how to initialize an object's state using the `__init__` constructor method.

## Key concept

In OOP, a class defines structure and behavior.

The `__init__` constructor runs automatically when you create an instance and is used to store the object's initial data.

## Instructions

Work in `app.py` and complete exactly the following:

1. Create a class named `Person`.
2. Add a `__init__` constructor that receives two parameters: `name` and `age`.
3. Store those values in instance attributes with the same names: `self.name` and `self.age`.
4. Create an instance named `student` with these values:
   - `name`: `"John"`
   - `age`: `21`

## Success criteria

The exercise is correct when:

- The `Person` class exists.
- `Person` has a constructor that stores `name` and `age`.
- `student` exists.
- `student.name` is `"John"`.
- `student.age` is `21`.
