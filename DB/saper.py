from data_users import info_users

import sqlite3 as sq
with sq.connect('saper.db') as con:
    con.cursor()
#cur.execute("DROP TABLE IF EXISTS users")
con.execute("""CREATE TABLE IF NOT EXISTS users (
 user_id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 sex INTEGER NOT NULL DEFAULT 1,
 old INTEGER,
 score INTEGER
 )""")
#добавление в таблицу данных
# con.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (None, 'Евгений', 1, 16, 1000))
# con.commit()

# con.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (3, 'Гена', 1, 20, 25652))
# con.commit()
con.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)
con.commit()