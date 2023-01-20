# Вариант 17
#Дан список размера N. Найти номера двух ближайших элементов из этого списка (то
#есть элементов с наименьшим модулем разности) и вывести эти номера в порядке
#возрастания.

import random
number = int(input("Введите число>> "))
list1 = [random.randrange(1,100) for i in range(number)]
print(list1)
a = abs(list1[0] - list1[1])
b = 0
c = 1
for i in range(0,number-1) :
    for j in range(i+1,number) :
        d = abs(list1[i] - list1[j])
        if a > d:
            a = d
            b = i
            c = j

print("Индексы:", b,",",c)
print("Разность:", a)

