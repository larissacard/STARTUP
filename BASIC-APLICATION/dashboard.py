import matplotlib.pyplot as plt
import sqlite3
import numpy as np
from datetime import datetime, timedelta
import pandas as pd

def gerar_faturamento_diario(passeio, dias):
    np.random.seed(len(passeio)) 
    faturamento_base = np.random.randint(500, 2000)
    variacao_diaria = np.random.normal(0, 100, dias)
    return np.round(np.cumsum(variacao_diaria) + faturamento_base, 2)


def gerar_agendamentos_diarios(passeio, dias):
    np.random.seed(len(passeio))  
    agendamentos_base = np.random.randint(10, 50)  
    variacao_diaria = np.random.normal(0, 5, dias) 
    return np.round(np.cumsum(variacao_diaria) + agendamentos_base, 0)


def obter_dados_relatorios(empresa_id):
    conn = sqlite3.connect('crajubar.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.nome, r.faturamento_mes, r.listagens_mes, r.clientes_mes, r.agendamentos_mes, r.crescimento
        FROM relatorios r
        JOIN passeios p ON r.passeio_id = p.id
        WHERE p.empresa_id = ?
    ''', (empresa_id,))
    dados = cursor.fetchall()
    conn.close()
    return dados

def obter_faturamento_7dias(empresa_id):
    dados = obter_dados_relatorios(empresa_id)
    hoje = datetime.now()

    dias = 7
    datas = [hoje - timedelta(days=i) for i in range(dias)][::-1]
    df = pd.DataFrame({'data': datas})

    for passeio in [dado[0] for dado in dados]:
        df[passeio] = gerar_faturamento_diario(passeio, dias)

    return df

def obter_agendamentos_7dias(empresa_id):
    dados = obter_dados_relatorios(empresa_id)
    hoje = datetime.now()

    dias = 7
    datas = [hoje - timedelta(days=i) for i in range(dias)][::-1]
    df = pd.DataFrame({'data': datas})

    for passeio in [dado[0] for dado in dados]:
        df[passeio] = gerar_agendamentos_diarios(passeio, dias)

    return df

def renderizar_graficos(empresa_id):
    dados = obter_dados_relatorios(empresa_id)
    nomes_passeios = [dado[0] for dado in dados]
    faturamentos = [dado[1] for dado in dados]
    agendamentos = [dado[4] for dado in dados] 

    plt.rcParams["axes.prop_cycle"] = plt.cycler(
        color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))  
    fig.suptitle('Dashboard de Relatórios', fontsize=16)

    axes[0, 0].bar(nomes_passeios, faturamentos)
    axes[0, 0].set_title("Faturamento por Passeio")
    axes[0, 0].set_xlabel("Passeio")
    axes[0, 0].set_ylabel("Faturamento")

    axes[0, 1].barh(nomes_passeios, faturamentos)
    axes[0, 1].set_title("Inventário por Passeio")
    axes[0, 1].set_xlabel("Faturamento")
    axes[0, 1].set_ylabel("Passeio")

    df_faturamento = obter_faturamento_7dias(empresa_id)

    for coluna in df_faturamento.columns[1:]:
        axes[1, 0].plot(df_faturamento['data'], df_faturamento[coluna], marker='o', label=coluna) 
    axes[1, 0].set_title('Crescimento/Decrescimento de Faturamento nos Últimos 7 Dias', fontsize=12)
    axes[1, 0].set_xlabel('Data', fontsize=10)
    axes[1, 0].set_ylabel('Faturamento (R$)')
    axes[1, 0].legend(loc='upper left')

    df_agendamentos = obter_agendamentos_7dias(empresa_id)

    for coluna in df_agendamentos.columns[1:]:  
        axes[1, 1].plot(df_agendamentos['data'], df_agendamentos[coluna], marker='o', label=coluna)  
    axes[1, 1].set_title('Crescimento/Decrescimento de Agendamentos nos Últimos 7 Dias', fontsize=12)
    axes[1, 1].set_xlabel('Data', fontsize=10)
    axes[1, 1].set_ylabel('Agendamentos')
    axes[1, 1].legend(loc='upper left')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    plt.show()