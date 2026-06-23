class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def greet(self):
        return f"Hello, my name is {self._name} and I am {self._age} years old."
    
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0:
            self._age = age
            return True
        else:
            return False

student = Person("John", 21)