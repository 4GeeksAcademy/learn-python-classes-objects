class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, cohort):
        super().__init__(name, age)
        self.cohort = cohort

    def describe(self):
        return f"Name: {self.name}, Age: {self.age}, Cohort: {self.cohort}"


student = Student(name="John", age=21, cohort="42")