class Person:
    def __init__(self, name, age):
        if name is None or name.strip() == "":
            raise ValueError("Name cannot be empty.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.name = name
        self.age = age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.age = age
        

student = Person("John", 21)   