from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car drives with engine")

class Bicycle(Vehicle):
    def move(self):
        print("Bicycle pedals forward")

vehicles = [Car(), Bicycle()]

def start_journey(vehicle: Vehicle):
    vehicle.move()


start_journey(Car())
start_journey(Bicycle())
