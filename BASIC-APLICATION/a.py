import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd

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
    df['data'] = hoje  # Simulando que todos os dados são de hoje (você pode ajustar para incluir datas reais)
    
    data_limite = hoje - timedelta(days=intervalo)
    dados_intervalo = df[df['data'] >= data_limite]
    
    resultados = {
        'faturamento': dados_intervalo['faturamento_mes'].sum(),
        'agendamentos': dados_intervalo['agendamentos_mes'].sum(),
        'dados_intervalo': dados_intervalo
    }
    
    return resultados

resultados = processar_dados_intervalos(obter_dados_relatorios(), 7)
dados = obter_dados_relatorios()
nomes_passeios = [dado[0] for dado in dados]
faturamentos = [dado[1] for dado in dados]

plt.rcParams["axes.prop_cycle"] = plt.cycler(color = ["#012E40", "#026773", "#F2E3D5", "#024959", "#3CA6A6"])

fig1, ax1 = plt.subplots()
ax1.bar(nomes_passeios, faturamentos)
ax1.set_title('Faturamento por Passeio')
ax1.set_xlabel('Passeio')
ax1.set_ylabel('Faturamento (R$)')
plt.show()


#chart 2
agendamentos = [dado[4] for dado in dados]
fig2, ax2 = plt.subplots()
ax2.barh(list(nomes_passeios), agendamentos)
ax2.set_title('Agendamentos por Passeio')
ax2.set_xlabel('Passeio')
ax2.set_ylabel('Nº Agendamentos')
plt.show()

#chart3

dados2 = obter_dados_relatorios()
resultados = processar_dados_intervalos(dados, 7)
dados_intervalo = resultados['dados_intervalo']
    
nomes_passeios = dados_intervalo['nome']
faturamentos = dados_intervalo['faturamento_mes']
    
fig, ax = plt.subplots()
ax.plot(nomes_passeios, faturamentos, marker='o', linestyle='-', color='#012E40')
ax.set_title(f'Crescimento de Faturamento nos últimos {7} dias')
ax.set_xlabel('Passeio')
ax.set_ylabel('Faturamento (R$)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

