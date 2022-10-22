try:
    A = int(input("Введите положительное число A >> "))
    B = int(input("Введите положительное число B >> "))
    c = 0
    if A>B:
        while A>B:
            A = A-B
            c = A
            print(c)
            break
    else:
        print("error")
except:
    print("error >> Число B не может превышать значение A или введено некорректное значение")
