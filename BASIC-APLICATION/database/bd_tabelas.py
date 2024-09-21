import sqlite3

conexao = sqlite3.connect('crajubar.db')
cursor = conexao.cursor()

#CLIENTES
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               email TEXT NOT NULL UNIQUE,
               password TEXT NOT NULL
               )''')

#EMPRESAS
cursor.execute('''CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
            )''')

#PASSEIOS
cursor.execute('''CREATE TABLE IF NOT EXISTS passeios (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                empresa_id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                tipo TEXT NOT NULL,
                vagas INTEGER NOT NULL,
                vagas_ocupadas INTEGER NOT NULL,
                empresa TEXT NOT NULL,
                alcance INTEGER NOT NULL,
                valor REAL NOT NULL,
                avaliacao REAL NOT NULL,
                descricao TEXT NOT NULL,
                categoria TEXT NOT NULL,
                avaliadores INTEGER NOT NULL,
                FOREIGN KEY (empresa_id) REFERENCES empresas (id)     
                )''')

#PASSEIOS AGENDADOS
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passeios_agendados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        passeio_id INTEGER NOT NULL,
        data_agendamento TEXT,
        FOREIGN KEY (cliente_id) REFERENCES usuarios (id),
        FOREIGN KEY (passeio_id) REFERENCES passeios (id)
    )
''')

# RELATÓRIOS
cursor.execute('''
    CREATE TABLE IF NOT EXISTS relatorios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passeio_id INTEGER NOT NULL,
        faturamento_mes REAL,
        listagens_mes INTEGER,
        clientes_mes INTEGER,
        agendamentos_mes INTEGER,
        crescimento TEXT,
        data_relatorio TEXT,
        FOREIGN KEY (passeio_id) REFERENCES passeios (id)
    )
''')

# Tabela de participações
cursor.execute('''CREATE TABLE IF NOT EXISTS participacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        passeio_id INTEGER NOT NULL,
        avaliado INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY (cliente_id) REFERENCES usuarios(id),
        FOREIGN KEY (passeio_id) REFERENCES passeios(id)
    );''')



cursor.execute('''CREATE TABLE IF NOT EXISTS avaliacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passeio_id INTEGER NOT NULL,
        cliente_id INTEGER NOT NULL,
        avaliacao_texto TEXT,
        avaliacao REAL NOT NULL,
        FOREIGN KEY (passeio_id) REFERENCES passeios(id),
        FOREIGN KEY (cliente_id) REFERENCES usuarios(id)
    );''')

conexao.commit()
conexao.close()