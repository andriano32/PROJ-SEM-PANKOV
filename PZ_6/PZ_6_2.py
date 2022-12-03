# Вариант 17
#Дан список размера N. Найти номера двух ближайших элементов из этого списка (то
#есть элементов с наименьшим модулем разности) и вывести эти номера в порядке
#возрастания.



import random
number = int(input("Введите число>> "))
a = [] # пустой список
m = 1
l = 1
p = 0
list1 = [random.randint(1,100) for i in range(number)] # список с диапазоном о 1 до 100 с условием не превышая знаение больше чем 100
print(list1)
for i in list1:
    if m >= number:
        break
    else:
        b = i - list1[m]
        a.append(b)
    m += 1

w = []
for f in a:
    if f > 0:
        w.append(f)

for k in list1:
    if l >= number:
        break
    else:
        b = k - list1[l]
        if b == min(w):
            if k < list1[l]:
                print(k, list1[l])
                break
            else:
                print(list1[l], k)
                break
    l += 1
