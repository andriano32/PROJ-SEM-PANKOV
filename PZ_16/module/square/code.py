#Дефолт.значение
default_p = 15

def square_perimeter(st=default_p):
    """Вычисляет периметер квадрата.
    Необходима сторона - 1 значение."""
    print(st*4)

def square_area(st=default_p):
    """Вычисляет площадь квадрата.
    Необходима сторона - 1 значение."""
    print(st**2)