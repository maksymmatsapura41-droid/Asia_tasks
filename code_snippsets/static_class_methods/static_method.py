class Cat:
    def meow(self):
        return "Meow!"

c = Cat()
print(c.meow())
# -----------------------------------------------------------

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(3, 4))  # 7

