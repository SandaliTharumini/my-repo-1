class Pet:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_breed(self):
        return self.breed

    def set_breed(self, breed):
        self.breed = breed

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}")

class Dog(Pet):
    def bark(self):
        print(f"{self.name} says woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball!")

class Cat(Pet):
    def meow(self):
        print(f"{self.name} says meow!")

    def scratch(self):
        print(f"{self.name} is scratching the furniture!")


