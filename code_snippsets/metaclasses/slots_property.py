class Shape:
    __slots__ = ("x1", "x2", "__length")
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.__length = lambda __length: x2 - x1

    @property
    def length(self):
        return self.__length(self)

    @length.setter
    def length(self, length):
        self.__length = length



shape1 = Shape(2, 777)
print(shape1.length)
