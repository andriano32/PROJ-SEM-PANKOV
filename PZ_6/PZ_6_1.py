import random

N = 10 #размер списка
print("N = ", N)

A = [random.randrange(1,10) for i in range(N)] # выдает рандомные значения в в списке от 1 до 10
print(A)

m = [] # пустой список
while True:
    for i in A:
        if i < A[-1]:
            m.append(i) # добавляет новый элемент m в конец списка A
    if len(m) > 0: # len возвращает длину строки
        print(*m) # выводит список
        break # останавливает цикл
    else:
        print(0)


