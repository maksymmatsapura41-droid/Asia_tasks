class Point:
    class_attribute = 'class_attribute'

    def __init__(self, x, y):
        self.x = x
        self.y = y
# print(dir(Point))
# print(p1.__dict__)
p1 = Point(1, 2)
p1.z = 3
# print(p1.__slots__)


# print(p1.class_attribute)
#
#
class Point2:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


p2 = Point2(1, 2)
print(p2.__slots__)
print(dir(Point2))
# print(p2.__dict__)