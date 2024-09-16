import sqlite3
from datetime import datetime

def consultar_passeios(inicio, fim):
    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT valor, vagas_ocupadas, alcance
        FROM passeios
        WHERE data BETWEEN ? AND ?
    ''', (inicio.date(), fim.date()))

    return cursor.fetchall()

def inserir_relatorio(conn, faturamento, agendamentos, alcance, data):
    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO relatorios (faturamento, clientes, agendamentos, alcance, data)
        VALUES (?, ?, ?, ?, ?)
    ''', (faturamento, agendamentos, agendamentos, alcance, data))

    conexao.commit()
    conexao.close()

def calcular_metrica(passeios):
    faturamento = sum(valor * vagas_ocupadas for valor, vagas_ocupadas, _ in passeios)
    agendamentos = sum(vagas_ocupadas for _, vagas_ocupadas, _ in passeios)
    alcance = sum(alcance for _, _, alcance in passeios)

    return faturamento, agendamentos, alcance


def criar_relatorios(inicio, fim):
    conexao = sqlite3.connect('crajubar.db')

    passeios = consultar_passeios(conexao, inicio, fim)

    faturamento, agendamentos, alcance = calcular_metrica(passeios)

    inserir_relatorio(conexao, faturamento, agendamentos, alcance, datetime.now().date())

    conexao.commit()
    conexao.close()
