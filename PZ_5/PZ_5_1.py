# Вариант 17
# 1. Составить программу, в которой функция построит изображение, в котором в первой
# строке 1 звездочка, во второй - 2, в третьей -3, ..., в строке с номером m - m звездочек.

def Grip(a):  # функция, в которой задается переменная a
    b = 1 # переменная b, которой присвоено значение 1, чтобы отсчет начался с 1 до 5
    c = '*'  # символ, который будет выводится в терминале
    while b <= a:  # цикл работает пока, b меньше либо равно переменной a
        print(c) # вывод конечной переменной c
        c += '*'  # символ, который будет выводится в терминале
        b += 1 # цикл будет работать, пока b не станет равно a

l = int(input('Введите число>> '))  # ввод числа пользователем с клавиатуры
Grip(l)  # вызов функции и введенного ей числа



