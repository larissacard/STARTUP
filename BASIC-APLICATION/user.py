import os
from data.bd_user import checar_usuario, adicionar_usuario

def menu_user():
    nome_logo = '\033[1;34mCRAJUBAR360\033[m'
    print("=" * 50)
    print(f"{nome_logo:^60}")
    print("=" * 50)
    print("1 - LOGIN \n2 - CADASTRO \n3 - SAIR")

    opcao = int(input("\033[1;34mDigite a opção desejada:\033[m "))
    
    if opcao == 1:
        limpar_menu()
        login_user()
    elif opcao == 2:
        limpar_menu()
        cadastro_user()
    elif opcao == 3:
        print("Tchau tchau!")
    else:
        limpar_menu()
        print("Opção inválida! Tente novamente.")

def limpar_menu():
    return os.system('cls' if os.name == 'nt' else 'clear')

def login_user():
    print("=" * 50)
    print(f"{'LOGIN':^50}")
    print("=" * 50)

    email = input("Email: ")
    senha = input("Senha: ")

    if checar_usuario(email, senha):
        print("Login realizado com sucesso!")
        limpar_menu()
        menu_user_passeios()
    else:
        print("Email ou senha incorretos. Tente novamente!")
        login_user()

def cadastro_user():
        print("=" * 50)
        print(f"{'CADASTRO':^50}")
        print("=" * 50)
        
        user_nome = input("Nome: ")
        user_email = input("E-mail: ")
        user_senha = input("Senha: ")

        adicionar_usuario(user_nome, user_email, user_senha)


def menu_user_passeios():
    nome_logo = '\033[1;34mCRAJUBAR360\033[m'
    print("=" * 50)
    print(f"{nome_logo:^60}")
    print("=" * 50)
    print("1 - LISTAR PASSEIOS \n2 - LISTAR PASSEIOS POR CATEGORIA \n3 - AGENDAR PASSEIOS \n4 - AVALIAR PASSEIO")

    opcao = int(input("\033[1;34mDigite a opção desejada:\033[m "))

    if opcao == 1:
        print('a')
    elif opcao == 2:
        print('b')
    elif opcao == 3:
        print('c')
    else:
        limpar_menu()
        print("Opção inválida! Tente novamente.")
