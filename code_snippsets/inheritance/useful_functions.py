class Animal:
    def eat(self):
        print("Eating")

class Mammal(Animal):
    def feed_milk(self):
        print("milk feeding")

class Dog(Mammal):
    def bark(self):
        print("dog barks")


dog = Dog()
dog.eat()
dog.feed_milk()
dog.bark()

# print(isinstance(dog, Dog))
print(issubclass(Mammal, Animal))

# isinstance(obj, Class)
# issubclass(Sub, Base)