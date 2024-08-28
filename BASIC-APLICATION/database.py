import sqlite3

#USUARIO
def criarTabela():
    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL,
                   password TEXT NOT NULL
                   )''')
    conexao.commit()
    conexao.close()

def adicionarUsuario(nome, email, password):
    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuarios(nome, email, password) VALUES (?, ?, ?)''', (nome, email, password))
    conexao.commit()
    conexao.close()

def listar_usuarios():
    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM usuarios''')
    usuarios = cursor.fetchall()
    for user in usuarios:
        print(user)
    conexao.close()

#EMPRESA
