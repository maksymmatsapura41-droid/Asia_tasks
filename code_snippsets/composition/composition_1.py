class Engine:
    def __init__(self, name):
        self.name = name

    def start(self):
        print("Engine started!")

class Car:
    def __init__(self, name):
        self.engine = Engine(name)

    def drive(self):
        self.engine.start()
        print("Car is moving")

car = Car(name="ferrari")
car.drive()


#has-a
#is-a