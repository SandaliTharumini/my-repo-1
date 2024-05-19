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

my_cat1 = Cat("Whiskers", 3)
my_cat1.meow()            
print(my_cat1.get_age()) 
my_cat.set_age(4)
print(my_cat1.get_age())

my_cat2 = Cat("Garfild", 9)
my_cat2.meow()            
print(my_cat2.get_age()) 
