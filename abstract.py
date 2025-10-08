# abstract class and method example

from abc import ABC

class Shape(ABC):  # abstract base class
    def area(self):   # abstract method
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    

# Create instances
r = Rectangle(5, 10)
c = Circle(7)
print("Rectangle Area:", r.area())
print("Circle Area:", c.area())