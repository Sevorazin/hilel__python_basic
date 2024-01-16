"""
Для класу Circle, розглянутому на уроці, додати метод віднімання двох кіл. Віднімання радіусов зробити по модулю.
Якщо два кола з однаковим значенням радіуса віднімаються, то результатом віднімання буде об'єкт классу Point.
"""

import math

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __str__(self):
        return f'Point({self.x}, {self.y})'


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f'Circle(x={self.x}, y={self.y}, radius={self.radius})'

    def __eq__(self, other):
        return self.radius == other.radius

    def __add__(self, other):
        new_obj = super().__add__(other)
        radius = self.radius + other.radius
        return Circle(radius, new_obj.x, new_obj.y)

    def __sub__(self, other):
        new_obj = super().__sub__(other)
        radius = abs(self.radius - other.radius)
        if radius == 0:
            return Point(new_obj.x, new_obj.y)
        return Circle(radius, new_obj.x, new_obj.y)

    def area(self):
        return round(math.pi * (self.radius ** 2), 3)

# Приклад використання:
circle1 = Circle(5, 1, 2)
circle2 = Circle(3, 4, 5)
circle3 = Circle(4,5,6)
circle4 = Circle(4,1,2)

result_circle = circle1 - circle2
result_circle1 = circle3 - circle4
print(result_circle)
print(result_circle1)
