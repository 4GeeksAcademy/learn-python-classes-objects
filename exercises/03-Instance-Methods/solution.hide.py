class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, my name is {self.name}"
    
    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! I am now {self.age} years old."
    
student = Person("John", 21)