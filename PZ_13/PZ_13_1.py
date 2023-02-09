import random

def matrix():
    s = random.randint(2, 8)
    lst  = [[random.randint(s, 10) for i in range(random.randint(s, s+1))]]
    return lst
def matrix_pt(lst):
    for k in lst:
        print(k)

matr_x = matrix()

matrix_pt(matr_x)