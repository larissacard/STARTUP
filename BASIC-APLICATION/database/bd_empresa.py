import sqlite3
import hashlib

conexao = sqlite3.connect('crajubar.db')
cursor = conexao.cursor()
    

def adicionar_empresa(nome, email, password):
    hashlib.sha256(password.encode()).hexdigest()
    
    try:
        conexao = sqlite3.connect('crajubar.db')
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO empresa(nome, email, password) VAL=UES (?, ?, ?)''', (nome, email, password))
        conexao.commit()
    
        print("Empresa cadastrda com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: O email já está cadastrado.")
    finally:
        conexao.close()    
    conexao.close()

def checar_empresa(email, password):
    hashlib.sha256(password.encode()).hexdigest()

    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()

    cursor.execute('''Select * FROM empresa WHERE email = ? AND password = ?''', (email, password))
    user = cursor.fetchone()

    conexao.close()

    if user:
        return True
    else:
        return False




def listar_empresa():
    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM usuarios''')
    usuarios = cursor.fetchall()

    for user in usuarios:
        print(user)

    conexao.close()


