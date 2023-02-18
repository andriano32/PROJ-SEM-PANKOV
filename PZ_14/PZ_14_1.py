import re

with open("experience.txt", encoding="UTF-8") as f1:
    f2 = f1.read()
    find_line = re.findall(r"[0-9]+.*\w+", f2)
    print(f"Количество элементов: {len(find_line)}")