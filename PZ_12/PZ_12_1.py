# Вариант 17.
# 1.В последовательности на n целых чисел умножить все элементы на последний
# минимальный элемент.

import random #Импортирование библиотеки

#Создание списка из случайных значений
lst = [random.randint(1, 30) for i in range(random.randint(3, 12))]
print("Изначальный список:", lst)
print("Перемноженный список:", list(map(lambda x: x*min(lst), lst)))
