# Создать абстрактный класс Shape с метаклассом ABCMeta, имеющий абстрактный метод area()
# и __slots__ с атрибутом name. Создать класс Rectangle, наследующий Shape, с __slots__
# для атрибутов width и height, реализовать конструктор и метод area(). Проверить,
# что добавление атрибута вне слотов вызывает AttributeError.

from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    __slots__ = ("name",)

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    __slots__ = ("width", "height", "name")

    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle("Myrect", 100, 150)
print(rectangle.area())