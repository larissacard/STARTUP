from data.db_passeios import adicionar_passeio, listar_passeios

def cadastra_passeio():
    print("[Informe os dados para cadastro]")

    nome = input("Nome: ")
    tipo = input("Tipo: ")
    vagas = int(input("Vagas: "))
    vagas_ocupadas = 0
    empresa = input("Nome da empresa: ")
    valor = input("Valor: ")
    avaliacao = 0
    descricao = input("Escreva uma descrição: ")
    categoria = input("Categoria: ")
    adicionar_passeio(nome, tipo, vagas, vagas_ocupadas,
 empresa, valor, avaliacao, descricao, categoria)

def mostrar_passeios():
    listar_passeios()