# Task 5
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"Point({self.x},{self.y})"
    
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Vector(Point):
    def __init__(self,x, y):
        super().__init__(x, y)
    def __repr__(self):
        return f"Vector({self.x},{self.y})"
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    

point1 = Point(5, 6)
point2 = Point(4, 8)
print(point1 == point2)
print(point1)
print(point1.distance_to (point2))

point3 = Vector(3, 9)
point4 = Vector(2, 4)
print(point3)
print(point3 + point4)