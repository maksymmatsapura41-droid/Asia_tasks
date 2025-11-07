class Person:
    default_name = []

    def __init__(self, name="Undefined"):
        if name:
            self.name = name
        else:
            self.name = Person.default_name


tom = Person("Tom")
bob = Person("")
print(tom.name)  # Tom
print(bob.name)  # Undefined