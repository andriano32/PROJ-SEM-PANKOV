import random
number = int(input("Введите число"))
N = random.randrange(2,20)
a = [random.randrange(1,100) for i in range(N)]

print("N:" ,N)
print("Array:\n",a)

d_min = abs(a[0] - a[1])
i_min = 0
j_min = 1
for i in range(0,N-1):
    for j in range(i+1,N):

