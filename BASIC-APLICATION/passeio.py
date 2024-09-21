from database.db_passeios import adicionar_passeio, listar_passeios, listar_passeios_empresa, listar_por_categoria, adicionar_passeio_agendado, registrar_participacao, achar_avaliacoes
from database.bd_empresa import listar_empresas
from rich.console import Console
from rich.table import Table
from datetime import datetime
import qrcode
import sqlite3

def formatar_avaliação(avaliacao, avaliadores):
    if(avaliadores != 0):
        media_avaliacao = avaliacao / avaliadores
        avaliacao_star = formatar_avaliacao_stars(media_avaliacao)
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
    
    for passeio in passeios:
        avaliacao = formatar_avaliação(passeio[9], passeio[12])

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
                    str(passeio[11])) #CATEGORIA

    if(len(passeios) == 0):
        print('Não há passeios!')
    else:
        console.print(table, justify="left")

def mostrar_passeios(id, tipo):
    if(tipo == 'empresa'):
        passeios = listar_passeios_empresa(id)
    else:
        passeios = listar_passeios()
    
    montar_tabela(passeios)

def listar_categoria():
        print("Selecione a categoria de Passeio Desejada:")
        print('1. História e Cultura \n2. Aventura e Natureza \n3. Lazer e Entretenimento \n4. Gastronomia e Bebidas')

        select = input("\033[1;34mDigite o número da opção deseja:\033[m ")
        
        passeios = listar_por_categoria(select)
        montar_tabela(passeios)
        

def agendar_passeios(usuario_id):
    passeios = listar_passeios()
    montar_tabela(passeios) 
        
    escolha = input("Escolha o número do passeio: ")
    if escolha.isdigit():
        indice = int(escolha) - 1
        if 0 <= indice < len(passeios):
            passeio_selecionado = passeios[indice]
            exibir_detalhes_passeio(passeio_selecionado, passeio_selecionado[0])  # Adicione o ID do passeio
            
            opcao = input("Deseja agendar este passeio? [1] Sim [2] Voltar: ")
            if opcao == '1':
                realizar_agendamento(passeio_selecionado, usuario_id)
            elif opcao == '2':
                agendar_passeios(usuario_id)
            else:
                print("Opção inválida.")
        else:
            print("Número de passeio inválido.")
    else:
        print("Entrada inválida.")

def realizar_agendamento(passeio, usuario_id):
    if passeio:
        quantidade = int(input("Informe a quantidade de agendamentos: "))
        total = quantidade * passeio[8]  # Preço do passeio
        
        print("Escolha a forma de pagamento:")
        print("[1] Pix")
        print("[2] Cartão")
        opcao_pagamento = input("Digite o número da opção desejada: ")
        processar_pagamento(opcao_pagamento, total)
        print("Obrigado por agendar conosco!")
        
        registrar_participacao(usuario_id, passeio[0])
    else:
        print("Erro ao realizar o agendamento.")

def processar_pagamento(opcao, valor):
    float(valor)
    if opcao == '1':
        print(f"Gerando QR Code para pagamento via Pix no valor de R${valor:.2f}...")
        qr = qrcode.make(f'Pix - Valor: R${valor:.2f}')
        qr.show()
        print("Pagamento via Pix gerado com sucesso!")
    elif opcao == '2':
        print(f"Processando pagamento de R${valor:.2f} via Cartão...")
        print("Pagamento via Cartão realizado com sucesso!")
    else:
        print("Opção de pagamento inválida.")

def exibir_detalhes_passeio(passeio, passeio_id):
    console = Console()
    table = Table(show_header=True, header_style="bold blue", title="DETALHES PASSEIO")
    table.add_column("NOME", justify="center")
    table.add_column("TIPO", justify="center")
    table.add_column("VAGAS", justify="center")
    table.add_column("EMPRESA", justify="center")
    table.add_column("VALOR", justify="center")
    table.add_column("AVALIAÇÃO", justify="center")
    table.add_column("DESCRIÇÃO", justify="center")
    table.add_column("CATEGORIA", justify="center")


    table.add_row(
        str(passeio[2]), #NOME
        str(passeio[3]), #TIPO
        str(passeio[4]), #VAGAS
        str(passeio[6]), #EMPRESA
        str(f"${passeio[8]:.2f}"), #VALOR
        str(passeio[9]), #AVALIACAO
        str(passeio[10]), #DESCRICAO
        str(passeio[11]))#CATEGORIA

    console.print(table, justify="left")
    buscar_avaliacoes(passeio_id)

    

def buscar_avaliacoes(passeio_id):
    avaliacoes = achar_avaliacoes(passeio_id)

    if avaliacoes:
        print("==" * 100)

        console = Console()

        for avaliacao in avaliacoes:
            nome_usuario = avaliacao[0]
            texto_avaliacao = avaliacao[1]
            valor_avaliacao = avaliacao[2]
            estrelas = formatar_avaliacao_stars(valor_avaliacao)

            table = Table(show_header=True, header_style="bold blue", title="Avaliações")
            table.add_column("USUARIO", justify="center")
            table.add_column("AVALIAÇÃO", justify="center")
            table.add_column("COMENTÁRIO", justify="center")
            table.add_row(
                str(nome_usuario), 
                str(estrelas), 
                str(texto_avaliacao)) 

            console.print(table, justify="left")
            
    else:
        print("Nenhuma avaliação disponível para este passeio.")

def formatar_avaliacao_stars(media_avaliacao):
    if(media_avaliacao >= 0 and media_avaliacao<= 1):
        avaliacao_star = "✰"
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
    

def avaliar_passeio(passeio_id, cliente_id, nova_avaliacao, avaliacao_texto):
    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT avaliacao, avaliadores FROM passeios WHERE id = ?', (passeio_id,))
    resultado = cursor.fetchone()
    
    if resultado:
        avaliacao_atual, avaliadores = resultado
        avaliadores += 1  # Incrementa o número de avaliadores
        nova_media = ((avaliacao_atual * (avaliadores - 1)) + nova_avaliacao) / avaliadores
        cursor.execute('UPDATE passeios SET avaliacao = ?, avaliadores = ? WHERE id = ?', 
                       (nova_media, avaliadores, passeio_id))
        cursor.execute('UPDATE participacoes SET avaliado = 1 WHERE passeio_id = ? AND cliente_id = ?', 
                       (passeio_id, cliente_id))
        cursor.execute('INSERT INTO avaliacoes (passeio_id, cliente_id, avaliacao_texto, avaliacao) VALUES (?, ?, ?, ?)', 
                       (passeio_id, cliente_id, avaliacao_texto, nova_avaliacao))
        conexao.commit()
        print(f"Avaliação atualizada para {nova_media:.2f} com {avaliadores} avaliadores.")
    else:
        print(f"Passeio com ID {passeio_id} não encontrado!")
    
    conexao.close()

def sistema_avaliacao(cliente_id):
    passeios_agendados = listar_passeios_agendados_para_avaliacao(cliente_id)
    
    if passeios_agendados:
        escolha = input("Escolha o número do passeio que deseja avaliar: ")
        
        if escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < len(passeios_agendados):
                passeio_selecionado = passeios_agendados[indice]
                while True:
                    try:
                        nova_avaliacao = float(input(f"Informe sua nova avaliação (0 a 5) para o passeio {passeio_selecionado[1]}: "))
                        if 0 <= nova_avaliacao <= 5:
                            break
                        else:
                            print("A avaliação deve ser entre 0 e 5.")
                    except ValueError:
                        print("Por favor, insira um número válido.")
                avaliacao_texto = ""
                while True:
                    avaliacao_texto = input("Digite sua avaliação textual (máximo 250 caracteres): ")
                    if len(avaliacao_texto) <= 250:
                        print(f"Caracteres digitados: {len(avaliacao_texto)}/250")
                        print("Avaliação concluída!")
                        break
                    else:
                        print("O texto ultrapassou o limite de 250 caracteres, tente novamente.")
                avaliar_passeio(passeio_selecionado[0], cliente_id, nova_avaliacao, avaliacao_texto)
            else:
                print("Número de passeio inválido.")
        else:
            print("Entrada inválida.")

def listar_passeios_agendados_para_avaliacao(cliente_id):
    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT p.id, p.nome, p.avaliacao
        FROM passeios p
        JOIN participacoes pa ON p.id = pa.passeio_id
        WHERE pa.cliente_id = ? AND pa.avaliado = 0
    ''', (cliente_id,))
    passeios_agendados = cursor.fetchall()
    conexao.close()
    
    if passeios_agendados:
        print("Passeios que podem ser avaliados:")
        for idx, passeio in enumerate(passeios_agendados, start=1):
            print(f"[{idx}] {passeio[1]} - Avaliação Atual: {passeio[2]:.2f}")
        return passeios_agendados
    else:
        print("Você já avaliou todos os passeios disponíveis.")
        return []
