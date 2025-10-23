class Animal:
    def __init__(self, name="Generic_name"):
        self.name = name

    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

dog = Dog("Buddy")
cat = Cat("Misty")
fish = Fish("Misty")


for animal in [dog, cat, fish]:
    print(f"{animal.name}:", end=" ")
    animal.make_sound()
