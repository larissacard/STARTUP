import tkinter as tk
from tkinter import StringVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime, timedelta
import pandas as pd

# Função para obter os dados dos relatórios
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

# Função para processar os dados de acordo com o intervalo
def processar_dados_intervalos(dados, intervalo):
    df = pd.DataFrame(dados, columns=['nome', 'faturamento_mes', 'listagens_mes', 'clientes_mes', 'agendamentos_mes', 'crescimento'])
    
    hoje = datetime.now()
    df['data'] = hoje  # Simulando que todos os dados são de hoje (ajuste para incluir datas reais)
    
    data_limite = hoje - timedelta(days=intervalo)
    dados_intervalo = df[df['data'] >= data_limite]
    
    resultados = {
        'faturamento': dados_intervalo['faturamento_mes'].sum(),
        'agendamentos': dados_intervalo['agendamentos_mes'].sum(),
        'dados_intervalo': dados_intervalo
    }
    
    return resultados

# Função para abreviar os nomes
def abreviar_nome(nome):
    partes = nome.split()
    if len(partes) > 1:
        return f"{partes[0][0]}. {' '.join(partes[1:])}"
    return nome

# Função para criar o gráfico de faturamento por passeio
def criar_grafico_faturamento():
    dados = obter_dados_relatorios()
    nomes_passeios = [abreviar_nome(dado[0]) for dado in dados]
    faturamentos = [dado[1] for dado in dados]

    fig, ax = plt.subplots()
    ax.bar(nomes_passeios, faturamentos)
    ax.set_title('Faturamento por Passeio')
    ax.set_xlabel('Passeio')
    ax.set_ylabel('Faturamento (R$)')
    return fig

# Função para criar o gráfico de agendamentos por passeio
def criar_grafico_agendamentos():
    dados = obter_dados_relatorios()
    nomes_passeios = [abreviar_nome(dado[0]) for dado in dados]
    agendamentos = [dado[4] for dado in dados]

    fig, ax = plt.subplots()
    ax.barh(nomes_passeios, agendamentos)
    ax.set_title('Agendamentos por Passeio')
    ax.set_xlabel('Nº Agendamentos')
    ax.set_ylabel('Passeio')
    return fig

# Função para criar o gráfico de crescimento de faturamento
def criar_grafico_crescimento(intervalo):
    dados = obter_dados_relatorios()
    resultados = processar_dados_intervalos(dados, intervalo)
    dados_intervalo = resultados['dados_intervalo']
    
    nomes_passeios = [abreviar_nome(nome) for nome in dados_intervalo['nome']]
    faturamentos = dados_intervalo['faturamento_mes']
    
    fig, ax = plt.subplots()
    ax.plot(nomes_passeios, faturamentos, marker='o', linestyle='-', color='#012E40')
    ax.set_title(f'Crescimento de Faturamento nos últimos {intervalo} dias')
    ax.set_xlabel('Passeio')
    ax.set_ylabel('Faturamento (R$)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig

# Função para atualizar o gráfico de crescimento com o intervalo selecionado
def atualizar_grafico_crescimento(canvas, frame, intervalo):
    # Limpa o gráfico atual
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Cria o gráfico atualizado
    fig = criar_grafico_crescimento(intervalo)
    canvas = FigureCanvasTkAgg(fig, frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side="left", fill="both", expand=True)

# Função para gerar a janela root e exibir os gráficos ocupando todo o espaço
def gerar_dashboard():
    root = tk.Tk()
    root.title("Dashboard")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))

    charts_frame = tk.Frame(root)
    charts_frame.pack(fill="both", expand=True)

    upper_frame = tk.Frame(charts_frame)
    upper_frame.pack(fill="both", expand=True)

    canvas1 = FigureCanvasTkAgg(criar_grafico_faturamento(), upper_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

    canvas2 = FigureCanvasTkAgg(criar_grafico_agendamentos(), upper_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

    lower_frame = tk.Frame(charts_frame)
    lower_frame.pack(fill="both", expand=True)

    # Dropdown para seleção do intervalo
    intervalo_var = StringVar()
    intervalo_var.set("7")  # Intervalo padrão de 7 dias

    intervalos = {"7 dias": 7, "15 dias": 15, "30 dias": 30}
    dropdown = tk.OptionMenu(root, intervalo_var, *intervalos.keys(), command=lambda val: atualizar_grafico_crescimento(canvas3, lower_frame, intervalos[val]))
    dropdown.pack(side="top", pady=10)

    # Criação do gráfico de crescimento inicial
    canvas3 = FigureCanvasTkAgg(criar_grafico_crescimento(7), lower_frame)
    canvas3.draw()
    canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

    # Ajusta as proporções dos gráficos dentro dos frames
    upper_frame.grid_columnconfigure(0, weight=1)
    upper_frame.grid_rowconfigure(0, weight=1)
    lower_frame.grid_columnconfigure(0, weight=1)
    lower_frame.grid_rowconfigure(0, weight=1)

    root.mainloop()
