# 08 Composition (has-a)

## Goal

In this exercise, you will practice composition by modeling an object that contains another object.

## Key concept

Composition allows richer models by combining small objects with clear responsibilities.

## Instructions

Work in `app.py` and complete exactly the following:

1. Create an `Address` class with `city` and `country`.
2. Create a `Person` class with `name` and `address`.
3. In `Person`, create a `full_address()` method that returns: `"<city>, <country>"`.
4. Create an instance `student` with:
   - `name`: `"John"`
   - `address`: `Address("Miami", "USA")`

## Success criteria

The exercise is correct when:

- `student.address` is an instance of `Address`.
- `student.full_address()` returns `"Miami, USA"`.
