import sqlite3

def adicionar_passeio(empresa_id, nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria, avaliadores):
    try:
        conexao = sqlite3.connect("crajubar.db")
        cursor = conexao.cursor()

        cursor.execute('''INSERT INTO passeios (empresa_id, nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria, avaliadores)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                          (empresa_id, nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria, avaliadores))

        conexao.commit()
        conexao.close()
        print("Passeio adicionado com sucesso!")
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
                return passeios
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
    
def registrar_participacao(cliente_id, passeio_id):
    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO participacoes (cliente_id, passeio_id) VALUES (?, ?)''', 
                   (cliente_id, passeio_id))
    conexao.commit()
    conexao.close()

def achar_avaliacoes(passeio_id):
    conexao = sqlite3.connect('crajubar.db')
    cursor = conexao.cursor()
    
    cursor.execute('''
        SELECT u.nome, a.avaliacao_texto, a.avaliacao, p.nome
        FROM avaliacoes a
        JOIN usuarios u ON a.cliente_id = u.id
        JOIN passeios p ON a.passeio_id = p.id
        WHERE a.passeio_id = ?
    ''', (passeio_id,))
    
    avaliacoes = cursor.fetchall()
    conexao.close()
    return avaliacoes