import sqlite3 as sq

with sq.connect('bibliary.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        family TEXT NOT NULL,
        name TEXT NOT NULL
        )""")


with sq.connect('bibliary.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        chapter TEXT NOT NULL,
        publishing TEXT, 
        year DATE,
        location TEXT
        )""")


with sq.connect('bibliary.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS chapters (
        chapter_id INTEGER PRIMARY KEY AUTOINCREMENT
        )""")

with sq.connect('bibliary.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS publishing  (
        publishing_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT
        )""")

with sq.connect('bibliary.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS authorbook (
        authorbook_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        author_id TEXT
        )""")