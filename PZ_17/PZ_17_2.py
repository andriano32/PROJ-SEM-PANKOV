class Figure:
    def __init__(self,a, b, flag):
        self.a = a
        self.b = b
        self.flag = flag

    def plosh(self):
        if self.flag == 1:
            return self.a * self.b
        elif self.flag == 2:
            return self.a**2
        else:
            return 3.14*(self.a**2)

    def perimetr(self):
        if self.flag == 1:
            return (self.a*2) + (self.b*2)
        elif self.flag == 2:
            return self.a*4
        else:
            return 3.14*2*self.a

class Square(Figure):
    def __init__(self, a, flag):
        self.a = a
        self.flag = flag
    def print(self):
        return "Я квадрат"

class Prom(Figure):
        def __init__(self, a, b, flag):
            self.a = a
            self.b = b
            self.flag = flag
        def print(self):
            return "Я пряугольник"

class Circle(Figure):
    def __init__(self, a, flag):
        self.a = a
        self.flag = flag
    def print(self):
        return "Я круг"

ob = Square(3,2)
print(ob.plosh())
print(ob.perimetr())
print(ob.print())

print()

ob2 = Prom(10, 25, 1)
print(ob2.plosh())
print(ob2.perimetr())
print(ob2.print())

print()

ob3 = Circle(15,3)
print(ob3.plosh())
print(ob3.perimetr())
print(ob3.print())
