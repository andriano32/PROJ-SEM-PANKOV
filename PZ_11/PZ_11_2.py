#Вариант 17
#2. Из предложенного текстового файла (text18-17.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить текст в
#стихотворной форме предварительно поставив последнюю строку между первой и второй.





p = open("text18-17.txt", "r", encoding='UTF-8')
p2 = p.read()
point = 0
for i in p2:
    print(i, end="")
for i in range(len(p2)):
    if p2[i] in ',.?!:;—':
        point += 1
print(f"\n\nКоличество знаков препинания: {point}\n")
p.close()


p3 = open("novij_tekst", "r",  encoding="UTF-8")
file_1 = p3.readlines()
list_text = [i for i in file_1]
print(list_text)
p3.close()

p4 = open("novij_tekst", "w", encoding='UTF-8')
for k in range(len(list_text)-1):
    if k == 1:
        p4.write(list_text[-1] + "\n")
        del list_text[-1]
    p4.write(list_text[k])
p4.close()
