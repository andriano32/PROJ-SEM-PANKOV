import random
class Matrix:
    def __init__(self, stroks, stolbs):
        self.stroks = stroks
        self.stolbs = stolbs

        self.matrix_1 = [[random.randint(1, 30) for i in range(self.stolbs)] for k in range(self.stroks)]
        self.matrix_2 = [[random.randint(1, 30) for i in range(self.stolbs)] for k in range(self.stroks)]

    def addition_matrix(self):
            answer_matrix = []
            itogo_matrix = []
            for i in range(len(self.matrix_1)):
                for k in range(len(self.matrix_1[0])):
                    answer_matrix.append(self.matrix_1[i][k] + self.matrix_2[i][k])
                    while len(answer_matrix) > 0:
                        itogo_matrix.append([i for i in answer_matrix[:len(answer_matrix)]])
                        del answer_matrix[:self.stolbs-1]
                        if len(answer_matrix) == 0:
                            break
            return itogo_matrix

    def subtraction_matrix(self):
            answer_matrix = []
            itogo_matrix = []
            for i in range(len(self.matrix_1)):
                for k in range(len(self.matrix_1)):
                    answer_matrix.append(self.matrix_1[i][k] - self.matrix_2[i][k])
                    while len(answer_matrix) > 0:
                        itogo_matrix.append([i for i in answer_matrix[:self.stolbs]])
                        del answer_matrix[:self.stolbs]
                        if len(answer_matrix) == 0:
                            break
            return itogo_matrix

    def multiple_matrix(self):
        if self.stolbs == self.stroks:
            itogo_matrix = [[0 for k in range(self.stolbs)] for i in range(self.stroks)]
            for i in range(len(self.matrix_1)):
             for k in range(len(self.matrix_2[0])):
                for j in range(len(self.matrix_2)):
                 itogo_matrix[i][k] += self.matrix_1[i][j] * self.matrix_2[j][k]
            return itogo_matrix
        else:
            return "Построение невозможно"

ob = Matrix(4,4)
print(ob.matrix_1)
print(ob.matrix_2)
print()
print(ob.addition_matrix())
print(ob.subtraction_matrix())
print(ob.multiple_matrix())


