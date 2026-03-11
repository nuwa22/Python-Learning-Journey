# Parent class
class Animal:
    def eat(self):
        print("I can eat food!")
    def sleep(self):
        print("I am sleeping...")

# Child class
class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")


# Create an object of the Dog class
my_dog = Dog()

my_dog.eat() # Inherited method from the Animal class
my_dog.sleep() # Inherited method from the Animal class
my_dog.bark() # Method defined in the Dog class
