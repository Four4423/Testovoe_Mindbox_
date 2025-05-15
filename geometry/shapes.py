import math

class Shape:
    def area(self):
        raise NotImplementedError("Метод 'area' должен быть переопределён в подклассах.")
    
    def is_right_triangle(self):
        return False

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        if not ((a + b > c) and (b + c > a) and (c + a > b)):
            raise ValueError("Невозможно построить треугольник с такими сторонами")
            
        self.a = a
        self.b = b
        self.c = c
        
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[-1]**2 - (sides[0]**2 + sides[1]**2)) < 1e-7