#Вариант 17
#Дана строка. Преобразовать в ней все строчные буквы (как латинские, так и русские)
#в прописные.


word = str(input("Введите строку: ")) # ввод строки
try:
    if int(word):
        print("error")
except:
    print(word.upper())