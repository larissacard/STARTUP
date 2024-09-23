import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd
from matplotlib.gridspec import GridSpec
import numpy as np

def gerar_faturamento_diario(passeio, dias):
    np.random.seed(len(passeio)) 

    faturamento_base = np.random.randint(500, 2000)
    variacao_diaria = np.random.normal(0, 100, dias)
    return np.round(np.cumsum(variacao_diaria) + faturamento_base, 2)

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

def obter_dados_7dias(empresa_id):
    dados = obter_dados_relatorios(empresa_id)
    hoje = datetime.now()

    dias = 7
    datas = [hoje - timedelta(days=i) for i in range(dias)][::-1]
    df = pd.DataFrame({'data': datas})

    for passeio in [dado[0] for dado in dados]:
        df[passeio] = gerar_faturamento_diario(passeio, dias)

    return df

def renderizar_graficos(empresa_id):
    dados = obter_dados_relatorios(empresa_id)
    nomes_passeios = [dado[0] for dado in dados]
    faturamentos = [dado[1] for dado in dados]
    agendamentos = [dado[4] for dado in dados]

    fig = plt.figure(figsize=(12, 8))
    gs = GridSpec(2, 2, height_ratios=[1, 1])

    ax1 = fig.add_subplot(gs[0, 0])
    ax1.bar(nomes_passeios, faturamentos)
    ax1.set_title('Faturamento por Passeio')
    ax1.set_xlabel('Passeio')
    ax1.set_ylabel('Faturamento (R$)')
    plt.setp(ax1.get_xticklabels(), rotation=45, ha="right", fontsize=10)

    ax2 = fig.add_subplot(gs[0, 1])
    barras = ax2.barh(list(nomes_passeios), agendamentos)
    ax2.set_title('Agendamentos por Passeio')
    ax2.set_xlabel('Nº Agendamentos')

    for barra in barras:
        ax2.annotate(f'{int(barra.get_width())}', xy=(barra.get_width(), barra.get_y() + barra.get_height() / 2),
                     xytext=(5, 0), textcoords='offset points', ha='left', va='center')

    plt.setp(ax2.get_yticklabels(), fontsize=10)

    df = obter_dados_7dias(empresa_id)
    ax3 = fig.add_subplot(gs[1, :])
    for coluna in df.columns[1:]:
        ax3.plot(df['data'], df[coluna], marker='o', label=coluna)

    ax3.set_title('Crescimento/Decrescimento de Faturamento nos Últimos 7 Dias')
    ax3.set_xlabel('Data')
    ax3.set_ylabel('Faturamento (R$)')
    ax3.legend(loc='upper left')
    ax3.grid(True)

    fig.autofmt_xdate()

    plt.subplots_adjust(wspace=0.4, hspace=0.4)

 
    plt.tight_layout()
    plt.show()

