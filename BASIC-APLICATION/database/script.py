import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('crajubar.db')
cursor = conn.cursor()

# Inserir dados na tabela usuarios
cursor.executemany('''
    INSERT INTO usuarios (nome, email, password) VALUES (?, ?, ?)
''', [
    ('João Silva', 'joao.silva@email.com', 'senha123'),
    ('Maria Oliveira', 'maria.oliveira@email.com', 'senha456'),
    ('Pedro Santos', 'pedro.santos@email.com', 'senha789'),
    ('Ana Costa', 'ana.costa@email.com', 'senha101'),
    ('Lucas Lima', 'lucas.lima@email.com', 'senha102'),
    ('Beatriz Melo', 'beatriz.melo@email.com', 'senha103'),
    ('Paulo César', 'paulo.cesar@email.com', 'senha104'),
    ('Carla Rocha', 'carla.rocha@email.com', 'senha105'),
    ('Marcos Souza', 'marcos.souza@email.com', 'senha106'),
    ('Fernanda Duarte', 'fernanda.duarte@email.com', 'senha107')
])

# Inserir dados na tabela empresa
cursor.executemany('''
    INSERT INTO empresa (nome, email, password) VALUES (?, ?, ?)
''', [
    ('Aventuras Ltda', 'contato@aventuras.com', 'senha123'),
    ('ExploraTour', 'contato@exploratour.com', 'senha456'),
    ('Trilhas e Passeios', 'contato@trilhas.com', 'senha789'),
    ('EcoTurismo BR', 'contato@ecoturismo.com', 'senha101'),
    ('Natureza Viva', 'contato@naturezaviva.com', 'senha102'),
    ('Aventura X', 'contato@aventurax.com', 'senha103'),
    ('Turismo Seguro', 'contato@turismoseguro.com', 'senha104'),
    ('Montanha e Mar', 'contato@montanhaemar.com', 'senha105'),
    ('Vida ao Ar Livre', 'contato@vidaolivre.com', 'senha106'),
    ('Paisagens Extremas', 'contato@paisagensextremas.com', 'senha107')
])

# Inserir dados na tabela passeios
cursor.executemany('''
    INSERT INTO passeios (empresa_id, nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', [
    (1, 'Cachoeira do Sol', 'Ecoturismo', 20, 5, 'Aventuras Ltda', 100, 150.0, 4.5, 'Passeio para a cachoeira mais bonita da região', 'Natureza'),
    (2, 'Passeio de Barco', 'Aventura', 15, 10, 'ExploraTour', 150, 200.0, 4.7, 'Passeio de barco pelo rio local', 'Aventura'),
    (3, 'Trilha das Pedras', 'Ecoturismo', 25, 8, 'Trilhas e Passeios', 120, 100.0, 4.6, 'Trilha com vistas incríveis e pontos de observação', 'Natureza'),
    (4, 'Mergulho Profundo', 'Aventura', 10, 7, 'EcoTurismo BR', 90, 300.0, 4.8, 'Experiência de mergulho em águas profundas', 'Aventura'),
    (5, 'Rapel na Montanha', 'Aventura', 8, 4, 'Natureza Viva', 80, 250.0, 4.2, 'Rapel em montanha com vistas impressionantes', 'Aventura'),
    (6, 'Camping na Floresta', 'Ecoturismo', 12, 6, 'Aventura X', 110, 180.0, 4.4, 'Camping em meio à floresta com atividades ao ar livre', 'Natureza'),
    (7, 'Passeio a Cavalo', 'Aventura', 15, 9, 'Turismo Seguro', 130, 100.0, 4.3, 'Passeio a cavalo em trilhas naturais', 'Natureza'),
    (8, 'Espeleologia', 'Aventura', 20, 12, 'Montanha e Mar', 70, 220.0, 4.9, 'Exploração de cavernas e grutas', 'Aventura'),
    (9, 'Trilha da Serra', 'Ecoturismo', 18, 11, 'Vida ao Ar Livre', 95, 120.0, 4.5, 'Trilha pela serra com belas paisagens', 'Natureza'),
    (10, 'Rafting no Rio Bravo', 'Aventura', 12, 10, 'Paisagens Extremas', 140, 210.0, 4.7, 'Rafting em um dos rios mais desafiadores', 'Aventura')
])

# Inserir dados na tabela passeios_agendados
cursor.executemany('''
    INSERT INTO passeios_agendados (cliente_id, passeio_id, data_agendamento) VALUES (?, ?, ?)
''', [
    (1, 1, '2024-09-20'),
    (2, 2, '2024-09-22'),
    (3, 3, '2024-09-25'),
    (4, 4, '2024-09-26'),
    (5, 5, '2024-09-28'),
    (6, 6, '2024-09-30'),
    (7, 7, '2024-10-02'),
    (8, 8, '2024-10-03'),
    (9, 9, '2024-10-05'),
    (10, 10, '2024-10-07')
])

# Inserir dados na tabela avaliacoes
cursor.executemany('''
    INSERT INTO avaliacoes (cliente_id, passeio_id, nota) VALUES (?, ?, ?)
''', [
    (1, 1, 5),
    (2, 2, 4),
    (3, 3, 3),
    (4, 4, 5),
    (5, 5, 4),
    (6, 6, 5),
    (7, 7, 4),
    (8, 8, 5),
    (9, 9, 4),
    (10, 10, 5)
])

# Inserir dados na tabela relatorios
cursor.executemany('''
    INSERT INTO relatorios (passeio_id, faturamento_mes, listagens_mes, clientes_mes, agendamentos_mes, crescimento) VALUES (?, ?, ?, ?, ?, ?)
''', [
    (1, 3000.0, 200, 50, 20, '5%'),
    (2, 4000.0, 300, 60, 25, '7%'),
    (3, 2500.0, 150, 40, 15, '4%'),
    (4, 3500.0, 180, 45, 18, '6%'),
    (5, 4500.0, 220, 55, 22, '8%'),
    (6, 2800.0, 170, 42, 16, '5%'),
    (7, 3700.0, 190, 48, 19, '7%'),
    (8, 5000.0, 250, 65, 30, '9%'),
    (9, 3200.0, 160, 43, 17, '5%'),
    (10, 4100.0, 210, 58, 24, '6%')
])

# Atualizar a tabela de relatórios com datas fictícias
cursor.executemany('''
    UPDATE relatorios SET data_relatorio = ? WHERE id = ?
''', [
    ('2024-09-01', 1),
    ('2024-09-02', 2),
    ('2024-09-03', 3),
    ('2024-09-04', 4),
    ('2024-09-05', 5),
    ('2024-09-06', 6),
    ('2024-09-07', 7),
    ('2024-09-08', 8),
    ('2024-09-09', 9),
    ('2024-09-10', 10)
])


# Confirmar as alterações e fechar a conexão
conn.commit()
conn.close()

print("Dados inseridos com sucesso.")
