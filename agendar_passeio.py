import banco_empresa
import os

def limpar_tela():
    os.system("cls")

def menu():
    print("\nBem Vindo!")
    print("Digite a opção escolhida:\n1. Cadastrar Passeio\n2. Editar Passeio\n3. Rendimento\n4. Sair\n")
    
def escolhe_opcao(op):
    if (op==1):
        cadastrar_passeio()
    elif (op==2):
        banco_empresa.listar_passeios()
        print("\n")
        editar_passeio()
    elif (op==3):
        rendimento()
    elif (op==4):
        print("Até Mais!")
    else:
        print("Opção inválida. Tente novamente.")

def cadastrar_passeio():
    empresa = input("Empresa: ")
    local = input("Local: ")
    vagas = int(input("Vagas: "))
    data = input("Data(Ex:27/02/2024): ")
    valor = input("Valor: ")
    banco_empresa.adicionar_passeio(empresa,local,vagas,data,valor)


def editar_passeio():
    id_passeio = int(input("Digite o ID do passeio que deseja editar: "))
    
    empresa = input("Empresa (deixe em branco para não alterar): ")
    local = input("Local (deixe em branco para não alterar): ")
    vagas = input("Vagas (deixe em branco para não alterar): ")
    data = input("Data (Ex: 27/02/2024) (deixe em branco para não alterar): ")
    valor = input("Valor (deixe em branco para não alterar): ")

    banco_empresa.editar_passeio(id_passeio, empresa, local, vagas, data, valor)

opcao = 0
while (opcao!=4):
    limpar_tela()
    menu()
    opcao = int(input("Informe a opcao desejada:"))
    escolhe_opcao(opcao)

    
