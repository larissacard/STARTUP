import os
import bd

def menu_empresa():
    nome_logo = '\033[1;34mCRAJUBAR360 - EMPRESA\033[m'
    print("=" * 50)
    print(f"{nome_logo:^60}")
    print("=" * 50)
    print("1 - LOGIN \n2 - CADASTRO \n3 - SAIR")
    opcao = int(input("\033[1;34mDigite a opção desejada:\033[m "))

    if opcao == 1:
        limpar_menu()
        login_empresa()
    elif opcao == 2:
        limpar_menu()
        cadastro_empresa()
    elif opcao == 3:
        print("PROGRAMA ENCERRADO!")
    else:
        limpar_menu()
        print("Opção inválida! Tente novamente.")
        menu_empresa()

def limpar_menu():
    return os.system('cls' if os.name == 'nt' else 'clear')

def cadastro_empresa():
    print("=" * 50)
    print(f"{'CADASTRAR EMPRESA':^50}")
    print("=" * 50)

    nome = input("Nome: ")
    email = input("E-mail: ")
    password = input("Senha: ")
    tipoEmp = input("Tipo da Empresa: ")

    # bd.adicionarEmp(nome, email, password, tipoEmp)

def login_empresa():
    print("=" * 50)
    print(f"{'LOGIN EMPRESA':^50}")
    print("=" * 50)

    email = input("E-mail: ")
    senha = input("Senha: ")
    
    # bd.loginEmp(email, senha)    
