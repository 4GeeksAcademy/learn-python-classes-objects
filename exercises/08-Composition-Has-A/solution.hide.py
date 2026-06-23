class Address:
    def __init__(self, city, country):
        self.city = city
        self.country = country


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def full_address(self):
        return f"{self.address.city}, {self.address.country}"
    
student = Person(name="John", address=Address(city="Miami", country="USA"))