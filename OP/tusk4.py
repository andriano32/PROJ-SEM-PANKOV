# 4 задача
from random import randint


class List:
    def __init__(self, size):
        self.size = size = [randint(0, size) for i in range(15)]

    def vozvr(self):
        return f'{self.size}'

    def proverka(self, number):
        if number in self.size: print("Число есть")


asds = List(12)
print(asds.vozvr())
print(asds.proverka(2))