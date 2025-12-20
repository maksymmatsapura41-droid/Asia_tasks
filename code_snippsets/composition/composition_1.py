from loguru import logger
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
logger.info("This is the info message")
car.drive()


#has-a
#is-a