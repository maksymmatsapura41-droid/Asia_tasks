class AutoIDMeta(type):
    def __new__(cls, name, bases, dct):
        dct['id'] = 0
        return super().__new__(cls, name, bases, dct)

class User(metaclass=AutoIDMeta):
    name: str

class Product(metaclass=AutoIDMeta):
    name: str

print(User.id)
print(Product.id)
