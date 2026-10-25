class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts with self-start.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start.")

c = Car()
c.start()

b = Bike()
b.start()