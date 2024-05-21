# pet_animal_definitions.py

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


class Dog(Pet):
    def bark(self):
        print(f"{self.name} says woof!")


class Cat(Pet):
    def meow(self):
        print(f"{self.name} says meow!")


