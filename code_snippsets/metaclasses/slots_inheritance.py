class Shape:
    __slots__ = ("x1", "x2")
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2


class Shape2(Shape):
    super.__slots__ = ("x1", "x2")


shape1 = Shape(1, 2)
shape1.z = 9

shape2 = Shape2(1, 2)
shape2.z = 9