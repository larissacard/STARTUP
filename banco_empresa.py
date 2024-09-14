import sqlite3

def criar_tabela():
    with sqlite3.connect('empresa.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS passeios (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           empresa TEXT NOT NULL,
                           local TEXT NOT NULL,
                           vagas INTEGER NOT NULL,
                           data TEXT NOT NULL,
                           valor INTEGER NOT NULL
                           )''')
        conexao.commit()

def adicionar_passeio(empresa, local, vagas, data, valor):
    try:
        with sqlite3.connect('empresa.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute('''INSERT INTO passeios (empresa, local, vagas, data, valor) VALUES (?, ?, ?, ?, ?)''',
                           (empresa, local, vagas, data, valor))
            conexao.commit()
            print("Passeio cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar passeio: {e}")

def listar_passeios():
    try:
        with sqlite3.connect('empresa.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute('''SELECT * FROM passeios''')
            passeios = cursor.fetchall()

            if passeios:
                for passeio in passeios:
                    print(passeio)
            else:
                print("Nenhum passeio encontrado.")
    except sqlite3.Error as e:
        print(f"Erro ao listar passeios: {e}")

def editar_passeio(id_passeio, empresa=None, local=None, vagas=None, data=None, valor=None):
    try:
        with sqlite3.connect('empresa.db') as conexao:
            cursor = conexao.cursor()
            
            campos = []
            parametros = []
            
            if empresa is not None:
                campos.append("empresa = ?")
                parametros.append(empresa)
            if local is not None:
                campos.append("local = ?")
                parametros.append(local)
            if vagas is not None:
                campos.append("vagas = ?")
                parametros.append(vagas)
            if data is not None:
                campos.append("data = ?")
                parametros.append(data)
            if valor is not None:
                campos.append("valor = ?")
                parametros.append(valor)
            
            if not campos:
                print("Nenhum dado para atualizar.")
                return
            
            parametros.append(id_passeio)
            
            consulta_sql = f"UPDATE passeios SET {', '.join(campos)} WHERE id = ?"
            cursor.execute(consulta_sql, parametros)
            conexao.commit()
            
            if cursor.rowcount > 0:
                print("Passeio atualizado com sucesso!")
            else:
                print("Passeio não encontrado ou nenhum dado atualizado.")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar passeio: {e}")

criar_tabela()

