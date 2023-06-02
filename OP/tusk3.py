class Nikola:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_edit(self):
        if len(self.name.split(" ")) > 1:
            return "Нужно имя"
        else:
            if self.name.title() != 'Николай':
                self.name = "Я не {}, a Николай". format(self.name)
            return "Имя {} | Возраст: {}".format(self.name, self.age)

tet_1 = Nikola("Николай", 10)
tet_2 = Nikola("Даня Пеп", 10)

print(tet_1.name_edit())
print()
print(tet_2.name_edit())