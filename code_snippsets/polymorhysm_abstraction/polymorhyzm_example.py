import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def half_of_perimeter(self):
        return (self.a + self.b + self.c) / 2

    def area_for_triangle(self):
        p = self.half_of_perimeter()
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

shapes = [
    Rectangle(4, 5),
    Square(6),
    Triangle(3, 4, 5),
]

for shape in shapes:
    print(shape.area())

# what if some class does not implement method area ?
# how to be sure about implementation