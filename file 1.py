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

my_dog1 = Dog("Rex", 5)
my_dog1.bark()           
print(my_dog1.get_age()) 
my_dog1.set_age(6)
print(my_dog1.get_age()) 

my_dog2 = Dog("Odi", 9)
my_dog2.bark()           
print(my_dog2.get_age()) 
my_dog2.set_age(6)
print(my_dog2.get_age())
