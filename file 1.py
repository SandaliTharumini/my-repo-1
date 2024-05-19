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

my_dog = Dog("Rex", 5)

my_dog.bark()           
print(my_dog.get_age()) 

my_dog.set_age(6)
print(my_dog.get_age()) 
