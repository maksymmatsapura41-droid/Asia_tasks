class Engine:
    def __init__(self, name):
        self.name = name

    def start(self):
        print("Engine v2 started!")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()

car = Car(Engine(name="ferrari"))
car.drive()

#easy to change type of engine