# class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name}")
    
    def say_age(self):
        print(f"I am {self.age} years old")

student1 = Student("Suresh", 26)

print(student1.name)
print(student1.age)

student1.say_hello()
student1.say_age()