# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_rect_pr(self):
#         return 2*(self.h + self.w)
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_sq_pr(self):
#         return 4*self.a

# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
# # print(r1.get_rect_pr(), r2.get_rect_pr())
# # print(s1.get_sq_pr(), s2.get_sq_pr())
# geom = [r1, r2, s1, s2]
# for g in geom:
#     print(g.get_sq_pr())

#
# for g in geom:
#      if isinstance(g, Rectangle):
#          print(g.get_rect_pr())
#      else:
#          print(g.get_sq_pr())

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_pr(self):
#         return 2*(self.h + self.w)
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_pr(self):
#         return 4*self.a
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_pr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
# t1 = Triangle(3, 2, 1)
# t2 = Triangle(4, 3, 2)
#
# geom = [Rectangle(1, 2), Rectangle(3, 4), Square(10), Square(20), Triangle(3, 2, 1), Triangle(4, 3, 2)]
#
# for g in geom:
#     print(g.get_pr())

#  Абстрактный метод

class Geom:
    def get_pr(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод get_pr()")

# class Recangle(Geom)
class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w + self.h)

#class Square(Geom)
class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4*self.a

#class Triangle(Geom)
class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c

nomm = [Rectangle(10, 20), Rectangle(30, 40), Square(3), Square(4), Square(6), Triangle(10, 10, 3), Triangle(20, 40, 1)]

for g in nomm:
    print("Париметр равен: ", g.get_pr())
    print()