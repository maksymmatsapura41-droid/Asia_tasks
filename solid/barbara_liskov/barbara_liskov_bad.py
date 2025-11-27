class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height


def resize_rectangle(rect: Rectangle, width, height):
    rect.set_width(width)
    rect.set_height(height)
    print(f"Expected area: {width * height}, got: {rect.area()}")

rect = Rectangle(2, 3)
resize_rectangle(rect, 4, 5)

sq = Square(5, 5)
resize_rectangle(sq, 4, 5)
