class Person:
    population = 0  # Class attribute to keep track of the population

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population
    
    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False

student = Person("John", 21)