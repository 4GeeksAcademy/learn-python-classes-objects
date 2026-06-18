# 03 Instance methods

## Goal

In this exercise, you will practice how to add behavior to an object using instance methods.

## Key concept

In OOP, attributes represent the object's state and methods represent what the object can do.

An instance method always receives `self`, which refers to the current object.

## Instructions

Work in `app.py` and complete exactly the following:

1. Create a class named `Person`.
2. Add a `__init__` constructor that receives `name` and `age`.
3. Store those values in `self.name` and `self.age`.
4. Add an instance method named `greet` that returns this text:
   - `"Hi, my name is <name>"`
5. Add an instance method named `have_birthday` that increases age by 1.
6. Create an instance named `student` with:
   - `name`: `"John"`
   - `age`: `21`

## Success criteria

The exercise is correct when:

- The `Person` class exists.
- `student` is an instance of `Person`.
- `student.greet()` returns `"Hi, my name is John"`.
- After calling `student.have_birthday()`, age increases by 1.
