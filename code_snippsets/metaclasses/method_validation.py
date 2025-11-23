class RequireSpeak(type):
    def __new__(cls, name, bases, dct):
        if 'speak' not in dct:
            raise TypeError(f"Class {name} should contains method speak()")
        return super().__new__(cls, name, bases, dct)

class Animal(metaclass=RequireSpeak):
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    speak = "hello"