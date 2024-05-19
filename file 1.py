class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")
        
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} says meow!")

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

