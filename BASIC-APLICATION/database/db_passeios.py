import sqlite3

def adicionar_passeio(nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria):
    conexao = sqlite3.connect("crajubar.db")
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO passeios(nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria))
    conexao.commit()
    conexao.close()

def listar_passeios():
    conexao = sqlite3.connect("crajubar.db")
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM passeios''')
    passeios = cursor.fetchall()
    conexao.close()
    return passeios