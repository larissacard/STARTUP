import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd
from matplotlib.gridspec import GridSpec
from multiprocessing import Process
import numpy as np

def obter_dados_relatorios():
    conn = sqlite3.connect('crajubar.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.nome, r.faturamento_mes, r.listagens_mes, r.clientes_mes, r.agendamentos_mes, r.crescimento
        FROM relatorios r
        JOIN passeios p ON r.passeio_id = p.id
    ''')
    dados = cursor.fetchall()
    conn.close()
    return dados

def processar_dados_intervalos(dados, intervalo):
    df = pd.DataFrame(dados, columns=['nome', 'faturamento_mes', 'listagens_mes', 'clientes_mes', 'agendamentos_mes', 'crescimento'])
    
    hoje = datetime.now()
    df['data'] = hoje 
    
    data_limite = hoje - timedelta(days=intervalo)
    dados_intervalo = df[df['data'] >= data_limite]
    
    resultados = {
        'faturamento': dados_intervalo['faturamento_mes'].sum(),
        'agendamentos': dados_intervalo['agendamentos_mes'].sum(),
        'dados_intervalo': dados_intervalo
    }
    
    return resultados

def gerar_faturamento_diario(passeio, dias):
    """Função para simular o faturamento diário nos últimos 'dias' dias."""
    np.random.seed(len(passeio)) 

    faturamento_base = np.random.randint(500, 2000)
    variação_diaria = np.random.normal(0, 100, dias)
    return np.round(np.cumsum(variação_diaria) + faturamento_base, 2)

def obter_dados_7dias():
    dados = obter_dados_relatorios()
    hoje = datetime.now()

    
    dias = 7
    datas = [hoje - timedelta(days=i) for i in range(dias)][::-1]
    df = pd.DataFrame({'data': datas})

    
    for passeio in [dado[0] for dado in dados]:
        df[passeio] = gerar_faturamento_diario(passeio, dias)

    return df

def renderizar_graficos():
    dados = obter_dados_relatorios()
    nomes_passeios = [dado[0] for dado in dados]
    faturamentos = [dado[1] for dado in dados]
    agendamentos = [dado[4] for dado in dados]

    print(agendamentos)
    
    fig = plt.figure(figsize=(10, 8))
    gs = GridSpec(2, 2, height_ratios=[1, 1])

    
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.bar(nomes_passeios, faturamentos)
    ax1.set_title('Faturamento por Passeio')
    ax1.set_xlabel('Passeio')
    ax1.set_ylabel('Faturamento (R$)')

    
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.barh(nomes_passeios, agendamentos)
    ax2.set_title('Agendamentos por Passeio')
    ax2.set_xlabel('Nº Agendamentos')
    ax2.set_ylabel('Passeio')

    df = obter_dados_7dias() 

    ax3 = fig.add_subplot(gs[1, :])
    for coluna in df.columns[1:]:
        ax3.plot(df['data'], df[coluna], marker='o', label=coluna)

    ax3.set_title('Crescimento/Decrescimento de Faturamento nos Últimos 7 Dias')
    ax3.set_xlabel('Data')
    ax3.set_ylabel('Faturamento (R$)')
    ax3.legend(loc='upper left')
    ax3.grid(True)
    fig.autofmt_xdate()

    plt.subplots_adjust(wspace=0.336)

    plt.tight_layout()
    plt.show()