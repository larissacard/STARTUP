import sqlite3
import hashlib

conexao = sqlite3.connect('crajubar.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               email TEXT NOT NULL UNIQUE,
               password TEXT NOT NULL
               )''')

conexao.commit()
conexao.close()


def adicionar_usuario(nome, email, password):
   hashlib.sha256(password.encode()).hexdigest()

   try:
       conexao = sqlite3.connect('crajubar.db')
       cursor = conexao.cursor()

       cursor.execute('''INSERT INTO usuarios(nome, email, password) VALUES (?, ?, ?)''', (nome, email, password))
       conexao.commit()


       print("Usuário cadastrado com sucesso!")
   except sqlite3.IntegrityError:
       print("Erro: O email já está cadastrado.")
   finally:
       conexao.close()


def checar_usuario(email, password):
   hashlib.sha256(password.encode()).hexdigest()

   conexao = sqlite3.connect('crajubar.db')
   cursor = conexao.cursor()

   cursor.execute('''SELECT * FROM usuarios WHERE email = ? AND password = ?''', (email, password))
   user = cursor.fetchone()

   conexao.close()

   if user:
       return True
   else:
       return False


def listar_usuarios():
   conexao = sqlite3.connect('crajubar.db')
   cursor = conexao.cursor()

   cursor.execute('''SELECT * FROM usuarios''')
   usuarios = cursor.fetchall()

   for user in usuarios:
       print(user)

   conexao.close()
