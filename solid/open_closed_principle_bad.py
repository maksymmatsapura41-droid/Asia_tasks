class Shape:
    def __init__(self, type, width=0, height=0, radius=0):
        self.type = type
        self.width = width
        self.height = height
        self.radius = radius

class AreaCalculator:
    def calculate_area(self, shape):
        if shape.type == "rectangle":
            return shape.width * shape.height
        elif shape.type == "circle":
            return 3.14 * shape.radius ** 2


