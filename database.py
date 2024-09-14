import sqlite3

conn = sqlite3.connect('lchumi.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')

conn.commit() #Confirmar Cambios 
conn.close() #Cerrar conexion

def insertar_usuario(nombre, edad):
    conn = sqlite3.connect('lchumi.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', (nombre, edad))
    conn.commit()
    conn.close()

def consultar_usuarios():
    conn = sqlite3.connect('lchumi.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Insertar usuarios
insertar_usuario('Alice', 30)
insertar_usuario('Bob', 25)

# Consultar y mostrar usuarios
usuarios = consultar_usuarios()
for usuario in usuarios:
    print(usuario)