import random  # импортирование псевдослучайных чисел
K = random.randrange(2,4) # случайные числа в заданном диапазоне от 2 до 3
N = random.randrange(1,21) # случаные числа в заданном диапазоне от 1 до 20

print("K = ", K)
print("N = ", N)
a = [i+1 for i in range(N)]

print("Массив:\n",a)
b = []
for i in a[K::]:
    b.append(i)
for n in a[0:K]:
    b.append(n)

print("Смещённый массив :\n",b)
