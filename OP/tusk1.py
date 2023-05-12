# 1 задача
class Person:
    def __init__(self, name, surname, qual=1):
        self.name = name
        self.surname = surname
        self.qual = qual

    def vozvr(self):
        return f'{self.name}, {self.surname}, {self.qual}'

    def __del__(self):
        print("До свидания " + str(self.name) + " " + str(self.surname))

chel1 = Person("Петр", "Трищагин", 1)
chel2 = Person("Михаил", "Белый", 2)
chel3 = Person("Прохор", "Середа", 5)

print("Вы уволены > " + min((chel1, chel2, chel3), key = lambda s: int(s.vozvr().split()[-1])).vozvr())