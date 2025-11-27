from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



class Square(Shape):
    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def print_area(shape: Shape):
    print(f"Area: {shape.area()}")

rect = Rectangle(4, 5)
print_area(rect)

sq = Square(5)
print_area(sq)
