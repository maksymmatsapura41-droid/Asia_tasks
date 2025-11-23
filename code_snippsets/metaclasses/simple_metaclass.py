class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Class creation {name}, ,{bases}, {dct}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    x = 5

class MyNewClass(metaclass=MyMeta):
    y = 8

# When Class creation method __new__ called
# obj = MyClass()
# obj1 = MyClass()
