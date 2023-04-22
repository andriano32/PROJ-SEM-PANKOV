import sqlite3 as sq
from data_bibliary import info_a_b, info_avtors, info_book, info_izd, info_raz

# with sq.connect('bibliary.db') as con:
#     cur = con.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS avtors (
# id_avtor INTEGER PRIMARY KEY,
# familie TEXT NOT NULL,
# name TEXT NOT NULL
# )""")

# with sq.connect('bibliary.db') as con:
#     cur = con.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS razdel (
# id_raz INTEGER PRIMARY KEY
# )""")

# with sq.connect('bibliary.db') as con:
#     cur = con.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS izdatelstvo (
# id_izd INTEGER PRIMARY KEY,
# city TEXT NOT NULL
# )""")

# with sq.connect('bibliary.db') as con:
#     con.execute('PRAGMA foreign_keys = ON')
# cur = con.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS books (
# id_book INTEGER PRIMARY KEY,
# title TEXT NOT NULL,
# id_raz INTEGER,
# id_izd INTEGER,
# god_izdan INTEGER NOT NULL,
# mesto_hranen TEXT NOT NULL,
# FOREIGN KEY (id_raz) REFERENCES razdel(id_raz) ON DELETE CASCADE ON UPDATE CASCADE,
# FOREIGN KEY (id_izd) REFERENCES izdatelstvo(id_izd) ON DELETE CASCADE ON UPDATE CASCADE
# )""")

# with sq.connect('bibliary.db') as con:
#     con.execute('PRAGMA foreign_keys = ON')
# cur = con.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS avtor_books (
# id_avtor_books INTEGER PRIMARY KEY,
# id_avtor INTEGER,
# id_book INTEGER,
# FOREIGN KEY (id_avtor) REFERENCES avtors(id_avtor) ON DELETE CASCADE ON UPDATE CASCADE,
# FOREIGN KEY (id_book) REFERENCES books(id_book) ON DELETE CASCADE ON UPDATE CASCADE
# )""")

# with sq.connect('bibliary.db') as con:
#     cur = con.cursor()
# con.executemany("INSERT INTO avtors VALUES(?, ?, ?)", info_avtors)
# con.commit()

# with sq.connect('bibliary.db') as con:
#     cur = con.cursor()
# con.executemany("INSERT INTO razdel VALUES(?)", info_raz)
# con.commit()

# with sq.connect('bibliary.db') as con:
#     cur = con.cursor()
# con.executemany("INSERT INTO izdatelstvo VALUES(?, ?)", info_izd)
# con.commit()

# with sq.connect('bibliary.db') as con:
#     cur = con.cursor()
# con.executemany("INSERT INTO books VALUES(?, ?, ?, ?, ?, ?)", info_book)
# con.commit()

# with sq.connect('bibliary.db') as con:
#     cur = con.cursor()
# con.executemany("INSERT INTO avtor_books VALUES(?, ?, ?)", info_a_b)
# con.commit()

# with sq.connect('bibliary.db') as con:
#  cur = con.cursor()
# print("На выборку:\n")
# res1 = con.execute("SELECT title, god_izdan FROM books ORDER BY god_izdan = 2008").fetchall()
# print(f'1:\n{res1}\n')
# res2 = cur.execute("SELECT avtors.name, books.title FROM books JOIN avtor_books ON avtor_books.id_book = books.id_book JOIN avtors ON avtors.id_avtor = avtor_books.id_avtor WHERE avtors.name = 'Александр'").fetchall()
# print(f'2:\n{res2}\n')
# res3 = cur.execute("SELECT razdel.id_raz, books.title FROM books JOIN razdel ON razdel.id_raz = books.id_raz WHERE razdel.id_raz = 7").fetchall()
# print(f'3:\n{res3}\n')
# res4 = cur.execute("SELECT izdatelstvo.city, izdatelstvo.id_izd, books.title FROM books JOIN izdatelstvo ON izdatelstvo.id_izd = books.id_izd  WHERE izdatelstvo.id_izd = 3").fetchall()
# print(f'4:\n{res4}\n')
# res5 = con.execute("SELECT * FROM avtors ORDER BY familie").fetchall()
# print(f'5:\n{res5}\n')
# res6 = con.execute("SELECT title, god_izdan FROM books ORDER BY title, god_izdan").fetchall()
# print(f'6:\n{res6}\n')
# res7 = cur.execute("SELECT avtors.familie, books.title, god_izdan FROM books  JOIN avtor_books ON avtor_books.id_book = books.id_book JOIN avtors ON avtors.id_avtor = avtor_books.id_avtor  WHERE avtors.familie = 'Брайан' ORDER BY god_izdan").fetchall()
# print(f'7:\n{res7}\n')
# res8 = con.execute("SELECT title, god_izdan FROM books WHERE god_izdan = 2005").fetchall()
# print(f'8:\n{res8}\n')
# res9 = cur.execute("SELECT izdatelstvo.id_izd, avtors.familie FROM books JOIN izdatelstvo ON izdatelstvo.id_izd = books.id_izd JOIN avtor_books ON avtor_books.id_book = books.id_book JOIN avtors ON avtors.id_avtor = avtor_books.id_avtor WHERE izdatelstvo.id_izd = 2").fetchall()
# print(f'9:\n{res9}\n')
# res10 = con.execute("SELECT title FROM books WHERE title LIKE '%и%'").fetchall()
# print(f'10:\n{res10}\n')

# with sq.connect('bibliary.db') as con:
#  cur = con.cursor()
# # Запрос 1
# cur.execute("UPDATE books SET god_izdan = ? WHERE id_book IN (SELECT id_book FROM avtor_books WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE familie = ?))", (2022, 'Иванов'))
# con.commit()
# # Запрос 2
# cur.execute("UPDATE books SET title = 'Новая книга', god_izdan = 2023 WHERE mesto_hranen LIKE 'Москва'")
# con.commit()
# # ЗАДАНИЕ 3 НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# # Запрос 4
# cur.execute("UPDATE books SET title = 'Старое название' WHERE god_izdan >= 2010 AND god_izdan <= 2015")
# con.commit()
# # Запрос 5
# cur.execute("UPDATE books SET mesto_hranen = ? WHERE id_book IN (SELECT id_book FROM avtor_books WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE id_avtor = ?))", ('Библиотека №2', 7))
# con.commit()
# # ЗАДАНИЕ 6 НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# # Запрос 7
# cur.execute("UPDATE avtor_books SET id_avtor = 14 WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE id_avtor = 13)")
# con.commit()
#     # ЗАДАНИЕ 8 НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
#     # ЗАДАНИЕ 9 НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
#     # ЗАДАНИЕ 10 НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# # Запрос 11
# cur.execute("UPDATE avtors SET familie = 'Клименко' WHERE id_avtor IN (SELECT id_avtor FROM avtor_books WHERE id_avtor = 6)")
# con.commit()
# # Запрос 12
# cur.execute("UPDATE books SET god_izdan = 2022 WHERE id_izd IN (SELECT id_izd FROM izdatelstvo WHERE city = 'Москва')")
# con.commit()
# # Запрос 13
# cur.execute("UPDATE books SET mesto_hranen = 'Книжный шкаф 1' WHERE id_book IN (SELECT id_book FROM avtor_books WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE familie = 'Иванов'))")
# con.commit()
# # Запрос 14
# cur.execute("UPDATE books SET god_izdan = 2023 WHERE id_book IN (SELECT id_book FROM avtor_books WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE name = 'Анна'))")
# con.commit()
# # ЗАДАНИЕ 15 НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# # Запрос 16
# cur.execute("UPDATE books SET god_izdan = 2024 WHERE id_book IN (SELECT id_book FROM avtor_books WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE familie = 'Петров'))")
# con.commit()

# DELET'ы
with sq.connect('bibliary.db') as con:
    cur = con.cursor()
# DELETE 2
cur.execute("DELETE FROM books WHERE god_izdan < 2000")
con.commit()
# DELETE 3
cur.execute("DELETE FROM avtor_books WHERE id_avtor = 1")
con.commit()
# DELETE 4
cur.execute("DELETE FROM avtors WHERE familie LIKE 'А%'")
con.commit()  # Объединен с запросом 15
# DELETE 5
cur.execute("DELETE FROM izdatelstvo WHERE city = 'Москва'")
con.commit()  # Объединен с запросом 14 и 16
# # DELETE 6
cur.execute("DELETE FROM avtor_books WHERE id_book = 10")
con.commit()
# # DELETE 7
cur.execute("DELETE FROM books WHERE mesto_hranen = 'Склад'")
con.commit()
# # ЗАДАНИЕ 8 ПРЕПОДАВАТЕЛЬ СКАЗАЛ НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# DELETE 9
cur.execute("DELETE FROM avtor_books WHERE id_avtor = 2")
con.commit()
# # ЗАДАНИЕ 10 ПРЕПОДАВАТЕЛЬ СКАЗАЛ НЕ ДЕЛАТЬ ИЗ-ЗА ОШИБКИ В ЗАДАНИИ
# # DELETE 11
cur.execute("DELETE FROM books WHERE title LIKE '%Война%'")
con.commit()
# # DELETE 12
cur.execute("DELETE FROM books WHERE god_izdan <= 2000 AND mesto_hranen = 'Библиотека №1'")
con.commit()
# # DELETE 13
cur.execute("DELETE FROM avtors WHERE id_avtor NOT IN (SELECT id_avtor FROM avtor_books)")
con.commit()
# # DELETE 14
cur.execute("DELETE FROM books WHERE id_izd IN (SELECT id_izd FROM izdatelstvo WHERE city = 'Москва')")
con.commit()
# # DELETE 15
cur.execute("DELETE FROM avtor_books WHERE id_avtor IN(SELECT id_avtor FROM avtors WHERE familie LIKE 'А%')")
cur.execute("DELETE FROM avtors WHERE familie LIKE 'А%'")
con.commit()
# # DELETE 16
cur.execute(
    "DELETE FROM avtor_books WHERE id_book IN (SELECT id_book FROM books WHERE id_izd IN (SELECT id_izd FROM izdatelstvo WHERE city = 'Москва'))")
con.commit()
# # DELETE 17
cur.execute(
    "DELETE FROM books WHERE id_book IN (SELECT id_book FROM avtor_books WHERE id_avtor IN (SELECT id_avtor FROM avtors WHERE familie LIKE 'П%'))")
con.commit()
# # DELETE 18
cur.execute("DELETE FROM books WHERE id_izd IN (SELECT id_izd FROM izdatelstvo WHERE city LIKE 'Н%')")
con.commit()
# # DELETE 19
cur.execute(
    "DELETE FROM avtor_books WHERE id_book IN (SELECT id_book FROM books WHERE id_izd IN (SELECT id_izd FROM izdatelstvo WHERE city LIKE 'Н%'))")
con.commit()

