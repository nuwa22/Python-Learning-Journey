class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")

animal = Animal()
animal.speak() 

dog = Dog()
dog.speak()

cat = Cat()
cat.speak() 