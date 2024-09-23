import os
from datetime import datetime, timedelta
import passeio
from database.bd_empresa import adicionar_empresa, checar_empresa
from dashboard import renderizar_graficos
from database.db_passeios import adicionar_passeio

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
    while True:
        nome_logo = '\033[1;34mCRAJUBAR360 - EMPRESA\033[m'
        print("=" * 50)
        print(f"{nome_logo:^60}")
        print("=" * 50)
        print("1 - Relatório \n2 - Passeios Cadastrados \n3 - Cadastrar Passeios \n4 - Sair")
        opcao = int(input("\033[1;34mDigite a opção desejada:\033[m"))

        if opcao == 1:
            renderizar_graficos(id)
        elif opcao == 2:
            limpar_menu()
            passeios_cadastrados()
            input("Pressione enter para voltar ao menu.")
        elif opcao == 3:
            limpar_menu()
            cadastra_passeios()
            input("Pressione enter para voltar ao menu.")

        elif opcao == 4:
            limpar_menu()
            print("PROGRAMA ENCERRADO!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione enter para tentar novamente...")
            limpar_menu()

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
    else: 
        print("Email ou senha incorretos. Tente novamente!")
        login_empresa()


def passeios_cadastrados():
    passeio.mostrar_passeios(id, 'empresa')
    
def cadastra_passeios():
    print("[Informe os dados para cadastro]")

    nome = input("Nome: ")
    tipo = input("Tipo: ")
    vagas = int(input("Vagas: "))
    vagas_ocupadas = 0
    empresa = input("Nome da empresa: ")
    alcance = 0
    valor = input("Valor: ")
    avaliacao = 0
    descricao = input("Escreva uma descrição: ")
    avaliadores = 0
    print("Selecione a categoria de Passeio Desejada:")
    print("1. História e Cultura \n2. Aventura e Natureza \n3. Lazer e Entretenimento \n4. Gastronomia e Bebidas")
    categoria = int(input("Categoria: "))
    if(categoria == 1):
        categoria = "História e Cultura"
    elif(categoria == 2):
        categoria = "Aventura e Natureza"
    elif(categoria == 3):
        categoria = "Lazer e Entretenimento"
    elif(categoria == 4):
        categoria = "Gastronomia e Bebidas"
    adicionar_passeio(id, nome, tipo, vagas, vagas_ocupadas,
    empresa, alcance, valor, avaliacao, descricao, categoria, avaliadores)

