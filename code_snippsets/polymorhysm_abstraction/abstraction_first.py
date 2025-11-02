import math

class Shape:
    def area(self):
        raise NotImplementedError("Method area should be implemented")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def half_of_perimeter(self):
        return (self.a + self.b + self.c) / 2

    def area(self):
        p = self.half_of_perimeter()
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi


shapes = [
    Rectangle(4, 5),
    Circle(3),
    Square(6),
    Triangle(3, 4, 5),
]

shape_1 = Shape()

for shape in shapes:
    print(shape.area())