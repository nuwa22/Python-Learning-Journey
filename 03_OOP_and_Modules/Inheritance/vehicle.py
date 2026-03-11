class Vehicle:
    def start(self):
        print("Engine started.")
    

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

my_car = Car()

my_car.start() # Inherited method from the Vehicle class
my_car.drive() # Method defined in the Car class