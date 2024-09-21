import sqlite3
import hashlib

conexao = sqlite3.connect('crajubar.db')
cursor = conexao.cursor()
    

def adicionar_empresa(nome, email, password):
    hashlib.sha256(password.encode()).hexdigest()
    
    try:
        conexao = sqlite3.connect('crajubar.db')
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO empresas(nome, email, password) VALUES (?, ?, ?)''', (nome, email, password))
        conexao.commit()
    
        print("Empresa cadastrada com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: O email já está cadastrado.")
    finally:
        conexao.close()    
    conexao.close()

def checar_empresa(email, password):
    hashlib.sha256(password.encode()).hexdigest()

    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()

    cursor.execute('''Select * FROM empresas WHERE email = ? AND password = ?''', (email, password))
    empresa = cursor.fetchone()
    conexao.close()

    if empresa:
        return empresa[0]
    else:
        return False



def listar_empresas():
    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM empresas''',)
    empresas = cursor.fetchall()
    conexao.close()
    
    return empresas
