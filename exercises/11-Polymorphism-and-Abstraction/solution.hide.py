class Animal:
    def __init__(self):
        pass

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    def speak(self):
        return "Woof"
    
class Cat(Animal):
    def speak(self):
        return "Meow"


def make_it_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()