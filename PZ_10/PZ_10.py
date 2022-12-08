#Вариант 17
#
#

import random

names = {"Даша", "Света", "Ира", "Ина","Лера", "Катя", "Оля", "Лена","Ирина", "Вероника", "Кира"}

#Создание групп второго курса.
IS_23 = {random.choice(list(names)) for i in range(random.randint(1, len(names)))}
IS_24 = {random.choice(list(names)) for i in range(random.randint(1, len(names)))}
IS_26 = {random.choice(list(names)) for i in range(random.randint(1, len(names)))}
IS_27 = {random.choice(list(names)) for i in range(random.randint(1, len(names)))}
IS_28 = {random.choice(list(names)) for i in range(random.randint(1, len(names)))}
name = ((((IS_23 & IS_24) & IS_26) & IS_27) & IS_28)
if name == set():
    name = 0
print("Имена которые встречаются на всех вторых курсах:", name)
name_not = (((((names - IS_23) - IS_24) - IS_26) - IS_27) - IS_28)
if name_not == set():
    name_not = 0
print("Имена которые не встречаются ни в одной из групп:", name_not)
secret_name = ((((IS_23 - IS_24) - IS_26) - IS_27) - IS_28)
secret_name -= ((((IS_24 - IS_23) - IS_26) - IS_27) - IS_28)
secret_name -= ((((IS_26 - IS_23) - IS_24) - IS_27) - IS_28)
secret_name -= ((((IS_27 - IS_23) - IS_24) - IS_26) - IS_28)
secret_name -= ((((IS_28 - IS_23) - IS_24) - IS_26) - IS_27)
if secret_name == set():
    secret_name = 0
print("Имена которые есть только в некоторых группах:", secret_name)