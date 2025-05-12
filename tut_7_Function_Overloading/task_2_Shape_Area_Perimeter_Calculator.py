"""Build a calculator using singledispatch to compute both area and perimeter for shape
objects.
📐 Supported Shapes:
• Circle(radius)
• Rectangle(width, width)
• Triangle(a, b, c) – assume it forms a valid triangle
shapes = [
Circle(5),
Rectangle(4, 6),
Triangle(3, 4, 5),
Circle(2.5),
Rectangle(10, 3)
]"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5),
    Circle(2.5),
    Rectangle(10, 3)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} area is {shape.area():.2f}")
    print(f"{shape.__class__.__name__} perimeter is {shape.perimeter():.2f}")