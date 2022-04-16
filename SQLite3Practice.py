import sqlite3

connection = sqlite3.connect('Resources/TestDB.db')
cursor = connection.cursor()
# cursor.execute('''CREATE TABLE users (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         username TEXT NOT NULL,
#         created TEXT NOT NULl)''')
# add_users = [(2, 'Lesley', 'lsly01', '04/01/2022'),(3, 'Nina', 'tiny1', '04/15/2022')]
# cursor.executemany('''INSERT INTO users VALUES (?,?,?,?)''', add_users)
# cursor.execute('''INSERT INTO users VALUES (1, 'Carlos', 'los1234', '04/16/2022')''')
# connection.commit()

cursor.execute("SELECT * FROM users").fetchall()