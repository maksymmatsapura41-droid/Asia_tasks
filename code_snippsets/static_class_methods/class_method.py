class Cat:
    count = 0

    def __init__(self):
        Cat.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


    def meow(self):
        return "meow"

c1 = Cat()
c2 = Cat()
print(c1.meow())
print(Cat.get_count())  # 2


class Cat:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, text):
        name = text.split("-")[0]
        return cls(name)

cat = Cat.from_string("Barsik-3-years")
print(cat.name)