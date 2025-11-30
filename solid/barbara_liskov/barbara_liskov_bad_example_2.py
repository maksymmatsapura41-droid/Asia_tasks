class Vehicle:
    def start_engine(self):
        print("Engine started")

class Bicycle(Vehicle):
    def start_engine(self):
        raise Exception("Bicycle has no engine!")

vehicles = [Vehicle(), Bicycle()]

for v in vehicles:
    v.start_engine()
