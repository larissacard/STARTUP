import os
from database.bd_relatorios import criar_relatorios
from datetime import datetime, timedelta
import passeio
from database.bd_empresa import adicionar_empresa, checar_empresa
from dashboard import gerar_dashboard

def menu_empresa_cadastro():
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
        menu_empresa_cadastro()

def menu_empresa():
    nome_logo = '\033[1;34mCRAJUBAR360 - EMPRESA\033[m'
    print("=" * 50)
    print(f"{nome_logo:^60}")
    print("=" * 50)
    print("1 - Relatório \n2 - Passeios Cadastrados \n3 - Cadastrar Passeios \n4 - Sair")
    opcao = int(input("\033[1;34mDigite a opção desejada:\033[m"))

    if opcao == 1:
        limpar_menu()
        criar_relatorio()
    elif opcao == 2:
        limpar_menu()
        passeios_cadastrados()
    elif opcao == 3:
        limpar_menu()
        cadastrar_passeios()
    elif opcao == 4:
        limpar_menu()
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
    
    adicionar_empresa(nome, email, password)
    login_empresa()

def login_empresa():
    print("=" * 50)
    print(f"{'LOGIN EMPRESA':^50}")
    print("=" * 50)

    global id

    email = input("E-mail: ")
    senha = input("Senha: ")

    resultado_id = checar_empresa(email, senha)

    if(resultado_id):
        id = resultado_id
        print("Login realizado com sucesso!")
        menu_empresa()


def criar_relatorio():
    gerar_dashboard()

def passeios_cadastrados():
    passeio.mostrar_passeios(id, 'empresa')

def cadastrar_passeios():
    passeio.cadastra_passeio()

