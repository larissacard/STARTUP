import os
import bd_user

def cadastroUser():
        print("[Informe os dados para cadastro]")

        user_dados = {}
        
        user_dados["nome"] = input("Nome: ")
        user_dados["email"] = input("E-mail: ")
        user_dados["senha"] = input("Senha: ")
        bd_user.adicionarUsuario(user_dados["nome"], user_dados["email"], user_dados["senha"])


def login():
    print("[Informe os dados para login]")

    login = {}

    login["email"] = input("E-mail: ")
    login["senha"] = input("Senha: ")

    autenticado = bd_user.checar_usuario(login["email"], login["senha"])

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
