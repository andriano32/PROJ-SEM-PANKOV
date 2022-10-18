try:
    A = float(input("Введите число>> "))
    B = float(input("Введите следующее число>> "))
    C = float(input("Введите ещё одно число>> "))
    if A < B < C:
        print(A*2, B*2, C*2)
    else:
        print(A*-1, B*-1, C*-1)
except:
    print("error")
