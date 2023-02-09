import random

def generate_matrix():
    a = random.randint(2, 8)
    lst = [[random.randint(a, 10) for i in range(a)] for l in range(random.randint(a, a+1))]
    return lst

def sum_matrix(m):
    chet = 0
    for l in m[:2]:
        for i in l:
            chet += i
    yield chet

def print_matrix(m):
    print("Матрица")
    for l in m:
        print(l)

matrix = generate_matrix()


print(f"Сумма элементов первых двух строк: {list(sum_matrix(matrix))}")

print_matrix(matrix)