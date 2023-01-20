p = open("text18-17.txt", "r")
p2 = p.read()
point = 0
for i in p2:
    print(i, end="")
for i in range(len(p2)):
    if p2[i] in ',.?!:;—':
        point += 1
print(f"\n\nКоличество знаков препинания: {point}\n")
p.close()


p3 = open("novij_tekst.txt", encoding="UTF-8")

