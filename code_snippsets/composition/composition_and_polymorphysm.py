class GasEngine:
    def start(self):
        print("Gas engine goes vroom!")

class ElectricEngine:
    def start(self):
        print("Silent electric start...")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Driving forward")


car1 = Car(GasEngine())
car2 = Car(ElectricEngine())

car1.drive()
car2.drive()

# Car works with any type of object which has method start() / duck typing