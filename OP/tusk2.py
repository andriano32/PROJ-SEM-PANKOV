# 2 задача
class TriangleChecker:
    def __init__(self, st1, st2, st3):
        self.st1 = st1
        self.st2 = st2
        self.st3 = st3

    def is_triangle(self):
        if type(self.st1) == int and type(self.st2) == int and type(self.st3) == int:
            if self.st1 < 0 or self.st2 < 0 or self.st3 < 0:
                print("С отрицательными числами ничего не выйдет!")
            elif self.st1 + self.st2 > self.st3 or self.st2 + self.st3 > self.st1 or self.st3 + self.st1 > self.st2:
                print("Ура трекугольник можно построить")
        else:
            print("Нужно вводить только числа")
t = TriangleChecker(1, 4, 6)
print(t.is_triangle())



