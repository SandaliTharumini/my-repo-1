from Pet import Dog,Cat

my_dog1 = Dog("Rex", 5, "Labrador")
my_dog1.bark()           
print(my_dog1.get_age()) 
my_dog1.set_age(6)
print(my_dog1.get_age()) 
my_dog1.fetch()
my_dog1.display_info()

my_dog2 = Dog("Odi", 9, "Beagle")
my_dog2.bark()           
print(my_dog2.get_age()) 
my_dog2.set_age(6)
print(my_dog2.get_age())
my_dog2.fetch()
my_dog2.display_info()

my_cat1 = Cat("Whiskers", 3, "Siamese" )
my_cat1.meow()            
print(my_cat1.get_age()) 
my_cat1.set_age(4)
print(my_cat1.get_age())
my_cat1.scratch()
my_cat1.display_info()

my_cat2 = Cat("Garfild", 9, "Persian")
my_cat2.meow()            
print(my_cat2.get_age()) 
my_cat2.display_info()
my_cat2.scratch()
