from database.db_passeios import adicionar_passeio, listar_passeios, listar_passeios_empresa, listar_por_categoria, adicionar_passeio_agendado
from database.bd_empresa import listar_empresas
from rich.console import Console
from rich.table import Table
from datetime import datetime

def cadastra_passeio():
    print("[Informe os dados para cadastro]")

    nome = input("Nome: ")
    tipo = input("Tipo: ")
    vagas = int(input("Vagas: "))
    vagas_ocupadas = 0
    empresa = input("Nome da empresa: ")
    valor = input("Valor: ")
    avaliacao = 0
    alcance = 0
    descricao = input("Escreva uma descrição: ")
    print("Selecione a categoria de Passeio Desejada:")
    print("1. História e Cultura \n2. Aventura e Natureza \n3. Lazer e Entretenimento \n4. Gastronomia e Bebidas")
    categoria = int(input("Categoria: "))
    adicionar_passeio(nome, tipo, vagas, vagas_ocupadas,
 empresa, alcance, valor, avaliacao, descricao, categoria)
    

def formatar_avaliação(passeios):
    soma_avaliacao = 0
    cont_avaliacao = 0
    avaliacao_star = ""
    for passeio in passeios:

        soma_avaliacao += passeio[9]
        cont_avaliacao += passeio[5]

    if(cont_avaliacao != 0):
        media_avaliacao = soma_avaliacao / cont_avaliacao

        if(media_avaliacao >= 0 and media_avaliacao<= 1):
            avaliacao_star = "Sem avaliação"
        elif(media_avaliacao == 1):
            avaliacao_star = ":star:"
        elif(media_avaliacao == 2):
            avaliacao_star = ":star: :star:"
        elif(media_avaliacao == 3):
            avaliacao_star = ":star: :star: :star:"
        elif(media_avaliacao == 4):
            avaliacao_star = ":star: :star: :star: :star:"
        elif(media_avaliacao == 5):
            avaliacao_star = ":star: :star: :star: :star: :star:"
    else:
        avaliacao_star = "Sem avaliação"

    return avaliacao_star

def montar_tabela(passeios):
    console = Console()
    table = Table(show_header=True, header_style="bold blue", title="PASSEIOS")
    table.add_column("ID", justify="center")
    table.add_column("NOME", justify="center")
    table.add_column("TIPO", justify="center")
    table.add_column("VAGAS", justify="center")
    table.add_column("VAGAS OCUPADAS", justify="center")
    table.add_column("EMPRESA", justify="center")
    table.add_column("VALOR", justify="center")
    table.add_column("AVALIAÇÃO", justify="center")
    table.add_column("DESCRIÇÃO", justify="center")
    table.add_column("CATEGORIA", justify="center")

    avaliacao = formatar_avaliação(passeios)
    for passeio in passeios:
        table.add_row(
                    str(passeio[0]), #ID
                    str(passeio[2]), #NOME
                    str(passeio[3]), #TIPO
                    str(passeio[4]), #VAGAS
                    str(passeio[5]), #VAGAS OCUPADAS
                    str(passeio[6]), #EMPRESA
                    str(f"${passeio[8]:.2f}"), #VALOR
                    str(avaliacao), #AVALIACAO
                    str(passeio[10]), #DESCRICAO
                    str(passeio[11]))#CATEGORIA

    console.print(table, justify="left")

def mostrar_passeios(id, tipo):
    if(tipo == 'empresa'):
        passeios = listar_passeios_empresa(id)
    else:
        passeios = listar_passeios()
    
    montar_tabela(passeios)

def listar_categoria():
    print("Selecione a categoria de Passeio Desejada:")
    print("1. História e Cultura")
    print("2. Aventura e Natureza")
    print("3. Lazer e Entretenimento")
    print("4. Gastronomia e Bebidas")

    selec = input("Digite o número da opção deseja: ")

    listar_por_categoria(selec)

def agendar_passeio(id):
    passeios = listar_passeios()
    id_user = id
    hoje = datetime.now()

    montar_tabela(passeios)

    id_passeio = input("Digite o ID do passeio que deseja agendar: ")

    adicionar_passeio_agendado(id_user, id_passeio, hoje)
