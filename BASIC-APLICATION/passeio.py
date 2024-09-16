from database.db_passeios import adicionar_passeio, listar_passeios
from rich.console import Console
from rich.table import Table

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
    categoria = input("Categoria: ")
    adicionar_passeio(nome, tipo, vagas, vagas_ocupadas,
 empresa, alcance, valor, avaliacao, descricao, categoria)
    

def formatar_avaliação():
    passeios = listar_passeios()

    for passeio in passeios:
        soma_avaliacao = 0
        cont_avaliacao = 0

        soma_avaliacao += passeio[8]
        cont_avaliacao += passeio[4]

    if(cont_avaliacao != 0):
        media_avaliacao = soma_avaliacao / cont_avaliacao

        if(media_avaliacao == 0):
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

def mostrar_passeios():
    passeios = listar_passeios()
    console = Console()
    table = Table(show_header=True, header_style="bold blue", title="PASSEIOS")
    table.add_column("NOME", justify="center")
    table.add_column("TIPO", justify="center")
    table.add_column("VAGAS", justify="center")
    table.add_column("VAGAS OCUPADAS", justify="center")
    table.add_column("EMPRESA", justify="center")
    table.add_column("VALOR", justify="center")
    table.add_column("AVALIAÇÃO", justify="center")
    table.add_column("DESCRIÇÃO", justify="center")
    table.add_column("CATEGORIA", justify="center")

    avaliacao = formatar_avaliação()
    
    for passeio in passeios:
        table.add_row(str(passeio[1]), #NOME
                      str(passeio[2]), #TIPO
                      str(passeio[3]), #VAGAS
                      str(passeio[4]), #VAGAS OCUPADAS
                      str(passeio[5]), #EMPRESA
                      str(f"${passeio[7]:.2f}"), #VALOR
                      str(avaliacao), #AVALIACAO
                      str(passeio[9]), #DESCRICAO
                      str(passeio[10]))#CATEGORIA

    console.print(table, justify="center")

formatar_avaliação()
mostrar_passeios()
