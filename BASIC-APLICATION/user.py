import os
from data.bd_user import adicionarUsuario, checar_usuario

def cadastroUser():
        print("[Informe os dados para cadastro]")

        user_dados = {}
        
        user_nome = input("Nome: ")
        user_email = input("E-mail: ")
        user_senha = input("Senha: ")
        adicionarUsuario(user_nome, user_email, user_senha)


def login():
    print("[Informe os dados para login]")

    login = {}

    login_email = input("E-mail: ")
    login_senha = input("Senha: ")

    autenticado = checar_usuario(login_email, login_senha)

    if(autenticado):
        menu_user()

def menu_user():
    nome_logo = '\033[1;34mCRAJUBAR360\033[m'
    print("=" * 50)
    print(f"{nome_logo:^60}")
    print("=" * 50)
    print("1 - LISTAR PASSEIOS \n2 - LISTAR PASSEIOS POR CATEGORIA \n3 - AGENDAR PASSEIOS \n4 - AVALIAR PASSEIO")
    opcao = int(input("\033[1;34mDigite a opção desejada:\033[m "))
    return opcao


def limpar_menu():
    return os.system('cls' if os.name == 'nt' else 'clear')

cadastroUser()
login()
