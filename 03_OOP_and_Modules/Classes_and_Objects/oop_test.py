# Class is a blueprint for creating objects.
# It defines a set of attributes and methods that the created objects will have.

# Object is an instance of a class.It is created using the class as a template
# and can have its own unique values for the attributes defined in the class.

# Attributes are variables that hold data associated with an object.
# They can be defined in the class and accessed or modified using the object.
# E.g. name, age, color, etc.

# Methods are functions that are defined within a class and can be called on objects of that class.
# They define the behavior of the objects and can manipulate the attributes of the object.
# E.g. Drive(), Eat(), Sleep(), etc.

# 1. Create class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

        def drive(self):
            print(self.brand + " is driving...")
        
        def stop(self):
            print(self.brand + " has stopped.")

# 2. Create object
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print(car1.brand)
print(car2.color)

car1.drive()
car2.stop()