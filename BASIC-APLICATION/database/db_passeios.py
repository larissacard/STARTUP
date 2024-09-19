import sqlite3

def adicionar_passeio(nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria):
    try:
        conexao = sqlite3.connect("crajubar.db")
        cursor = conexao.cursor()

        cursor.execute('''INSERT INTO passeios(empresa_id, nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria))

        conexao.commit()
        conexao.close()
    except sqlite3.Error as error:
        print("Erro ao inserir dados: ", error)

def listar_passeios_empresa(id):
    conexao = sqlite3.connect("crajubar.db")
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM passeios WHERE empresa_id = ?''', (id,))

    passeios = cursor.fetchall()
    conexao.close()

    return passeios

def listar_passeios():
    conexao = sqlite3.connect("crajubar.db")
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM passeios''')

    passeios = cursor.fetchall()
    conexao.close()
    return passeios


def listar_por_categoria(selec):
    categorias = {
        "1": "História e Cultura",
        "2": "Aventura e Natureza",
        "3": "Lazer e Entretenimento",
        "4": "Gastronomia e Bebidas"
    }

    categoria = categorias.get(selec)
    
    if not categoria:
        print("Categoria inválida.")
        return

    try:
        with sqlite3.connect('crajubar.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM passeios WHERE categoria = ?', (categoria,))
            passeios = cursor.fetchall()

            if passeios:
                for passeio in passeios:
                    print(passeio)
            else:
                print("Nenhum passeio encontrado para a categoria selecionada.")
    except sqlite3.Error as e:
        print(f"Erro ao listar passeios: {e}")

def adicionar_passeio_agendado(id_user, id_passeio, data):
   try:
       conexao = sqlite3.connect('crajubar.db')
       cursor = conexao.cursor()

       cursor.execute('''INSERT INTO passeios_agendados(cliente_id, passeio_id, data_agendamento) VALUES (?, ?, ?)''', (id_user, id_passeio, data))
       conexao.commit() 

       print("Passeio agendado com sucesso!")
   except sqlite3.IntegrityError:
       print("Erro: Passeio não encontrado.")
   finally:
       conexao.close()