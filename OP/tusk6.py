class Person:
    def __init__(self, name):
        self.__name = name

        def get_name(self):
            return self.__name

        def set_name(self, x):
            self.__name = x
            return self.__name


odv_1 = Person("Гена")
print(odv_1.get_name())
print(odv_1.set_name("Вишня"))