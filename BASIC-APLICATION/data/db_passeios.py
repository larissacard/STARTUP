import sqlite3


conexao = sqlite3.connect('crajubar.db')
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS passeios (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT NOT NULL,
                tipo TEXT NOT NULL,
                vagas INTEGER NOT NULL,
                vagas_ocupadas INTEGER NOT NULL,
                empresa TEXT NOT NULL,
                alcance INTEGER NOT NULL,
                valor REAL NOT NULL,
                avaliacao REAL NOT NULL,
                descricao TEXT NOT NULL,
                categoria TEXT NOT NULL      
                )''')
conexao.commit()
conexao.close()

def adicionar_passeio(nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria):
    conexao = sqlite3.connect("crajubar.db")
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO passeios(nome, tipo, vagas, vagas_ocupadas, empresa, alca valor, avaliacao, descricao, categoria) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria))
    conexao.commit()
    conexao.close()

def listar_passeios():
    conexao = sqlite3.connect("crajubar.db")
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM passeios''')
    passeios = cursor.fetchall()
    return passeios
    conexao.close