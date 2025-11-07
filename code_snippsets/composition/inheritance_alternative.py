# class FlyingCar(Car):
#     def fly(self):
#         print("Flying!")
#  Bad cause collision occurs Car and FlyingCar are one 1 level

class FlyModule:
    def fly(self):
        print("Flying!")

class FlyingCar:
    def __init__(self, engine, fly_module):
        self.engine = engine
        self.fly_module = fly_module

    def drive(self):
        self.engine.start()

    def fly(self):
        self.fly_module.fly()


class DefaultCar:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()