try:
    number = int(input('Введите целое число, оно должно быть больше 0: '))
    n = 1
    n_2 = 1
    n_3 = 1/n
    if number <= 0:
        print('Ошибка')
    else:
        while n <= number:
            n_3 *= 1/n
            n_2 += n_3
            n += 1
        print(n_2)
except TypeError:
    print('Ошибка!')
