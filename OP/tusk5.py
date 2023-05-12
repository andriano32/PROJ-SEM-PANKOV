# задача 5
import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def type(self):
        if self.side1 == self.side2 == self.side3:
            return "Треугольник равносторонний"
        if self.side1 == self.side2 or self.side1 or self.side3 == self.side3 or self.side2 == self.side3:
            return "Треугольник равнобедренный"
        return "Треугольник обычный"
    def square(self):
        self.p = (self.side1 + self.side2 + self.side3)/2
        return math.sqrt(self.p * (self.p - self.side1) * (self.p - self.side2) * (self.p - self.side3))

TringleOne = Triangle(6, 4, 2)
print(TringleOne.type())
print(TringleOne.square())
