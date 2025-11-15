class ValidAttrMeta(type):
    def __new__(cls, name, bases, dct):
        if 'name' not in dct:
            raise TypeError(f"Class {name} should have attribute 'name'")
        return super().__new__(cls, name, bases, dct)

class User(metaclass=ValidAttrMeta):
    name = "Alice"

class Product(metaclass=ValidAttrMeta):
    price = 100
