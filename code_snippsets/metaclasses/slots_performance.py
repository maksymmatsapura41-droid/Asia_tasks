import timeit

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        for i in range(100):
            self.x += 1
            del self.y
            self.y = 0

# print(dir(Point))
# print(p1.__dict__)
p1 = Point(1, 2)


class Point2:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        for i in range(100):
            self.x += 1
            del self.y
            self.y = 0

p2 = Point2(1, 2)
# print(p2.__slots__)
# print(dir(Point2))
# print(p2.__dict__)


# print(p1.__sizeof__() + p1.__dict__.__sizeof__())
# print(p2.__sizeof__() + p2.__slots__.__sizeof__())


t1 = timeit.timeit(p1.calc)
t2 = timeit.timeit(p2.calc)
print(t1, t2)