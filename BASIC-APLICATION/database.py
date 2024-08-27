import sqlite3

def criarTabela():
    conexao = sqlite3.connect('cajubar360.bd')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                   id INTEGER PRIMARY KEY AUTO_INCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL,
                   password TEXT NOT NULL
                   )''')
    conexao.commit()
    conexao.close()

def adicionarUsuario(nome, email, password):
    conexao = sqlite3.connect('cajubar360.bd')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuarios(nome, email, password) VALUES (?, ?, ?)''', (nome, email, password))
    conexao.commit()
    conexao.close()