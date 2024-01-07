import sqlite3

DATABASE = 'user.db'

conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
    ''')

cursor.execute('INSERT INTO Usuarios(nome, idade) VALUES (?, ?)', ('Artur', 24))
cursor.execute('INSERT INTO Usuarios(nome, idade) VALUES (?, ?)', ('Pessoa2', 57))

conn.commit()

cursor.execute('SELECT * FROM Usuarios')
for row in cursor.fetchall():
    print(row)

conn.close()
