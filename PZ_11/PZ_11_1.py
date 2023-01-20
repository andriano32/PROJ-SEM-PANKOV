# Вариант 17.
# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Произведение элементов:
# Количество пар, для которых произведение элементов делится на 3 (элементы пары в
# последовательности являются соседними)


import random

my_file = open('pankovFile.txt', 'w', encoding="UTF-8")
lst = [random.randint(-10,20) for i in range(10)]
my_file.write(f"Содержимое>> {lst}")
my_file.close()

wester_f = open('pankovFile.txt' , 'w' , encoding="UTF=8")
lst = [random.randint(-10,20) for i in range(10)]
lst_2 = 1
for i in lst:
    lst_2 *= i
a = 1
b = 0
c = 0
for d in range(0, len(lst)):
    number = lst[d]*lst[d+1]
    if number % 3 == 0:
        print(lst[d])
        print(c)
        c += 1



wester_f.write(f"Исходные данные>> {lst}\n")
wester_f.write(f"Количество элементов>> {len(lst)}\n")
wester_f.write(f"Произведение элементов>> {lst_2}\n")
wester_f.write(f"Количество пар, для которых произведение элементов делится на 3>> {c-1}\n")

