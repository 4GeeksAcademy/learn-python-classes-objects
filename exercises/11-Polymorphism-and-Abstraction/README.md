# 11 Polymorphism and applied abstraction

## Goal

In this exercise, you will apply polymorphism using a common interface across different classes.

## Key concept

Polymorphism allows different objects to be used uniformly when they share the same method contract.

## Instructions

Work in `app.py` and complete exactly the following:

1. Create a base class `Animal` with a `speak()` method that raises `NotImplementedError`.
2. Create a `Dog(Animal)` class that implements `speak()` and returns `"Woof"`.
3. Create a `Cat(Animal)` class that implements `speak()` and returns `"Meow"`.
4. Create a `make_it_speak(animal)` function that returns `animal.speak()`.
5. Create two global instances:
   - `dog = Dog()`
   - `cat = Cat()`

## Success criteria

The exercise is correct when:

- `make_it_speak(dog)` returns `"Woof"`.
- `make_it_speak(cat)` returns `"Meow"`.
- The same flow works for different types without type-based conditionals.
