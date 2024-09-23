import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('crajubar.db')
cursor = conn.cursor()

# Inserir dados na tabela usuarios
cursor.executemany('''INSERT INTO usuarios (nome, email, password) VALUES (?, ?, ?)''', [
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

# Inserir dados na tabela empresas
cursor.executemany('''INSERT INTO empresas (nome, email, password) VALUES (?, ?, ?)''', [
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

# Inserir dados na tabela passeios com o campo 'avaliadores'
cursor.executemany('''INSERT INTO passeios (empresa_id, nome, tipo, vagas, vagas_ocupadas, empresa, alcance, valor, avaliacao, descricao, categoria, avaliadores) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', [
    (1, 'Rafting no Rio Azul', 'Aventura', 10, 2, 'Aventuras Ltda', 110, 220.0, 4.6, 'Rafting em um rio com corredeiras emocionantes', 'Aventura e Natureza', 15),
    (1, 'Caminhada na Floresta', 'Ecoturismo', 15, 5, 'Aventuras Ltda', 95, 90.0, 4.5, 'Caminhada por trilhas em meio à floresta', 'Aventura e Natureza', 20),
    (2, 'Tour Gastronômico', 'Gastronomia', 20, 8, 'ExploraTour', 120, 130.0, 4.7, 'Descubra os sabores locais em um tour gastronômico', 'Gastronomia e Bebidas', 30),
    (2, 'Passeio de Barco', 'Aventura', 15, 5, 'ExploraTour', 150, 250.0, 4.8, 'Passeio de barco à noite com vista da cidade', 'Aventura e Natureza', 25),
    (3, 'Trilha do Sol Poente', 'Ecoturismo', 20, 3, 'Trilhas e Passeios', 100, 110.0, 4.4, 'Trilha que termina com vista do pôr do sol', 'Aventura e Natureza', 18),
    (3, 'Oficina de Artesanato', 'Cultural', 10, 2, 'Trilhas e Passeios', 60, 50.0, 4.5, 'Aprenda técnicas de artesanato local', 'História e Cultura', 10),
    (4, 'Mergulho em Recifes', 'Aventura', 8, 1, 'EcoTurismo BR', 80, 350.0, 4.9, 'Mergulho em recifes com vida marinha exuberante', 'Aventura e Natureza', 22),
    (4, 'Caminhada Ecológica', 'Ecoturismo', 15, 6, 'EcoTurismo BR', 100, 75.0, 4.5, 'Caminhada com foco em educação ambiental', 'Aventura e Natureza', 17),
    (5, 'Expedição de Aventura', 'Aventura', 12, 4, 'Natureza Viva', 110, 200.0, 4.6, 'Expedição de aventura em áreas remotas', 'Aventura e Natureza', 19),
    (5, 'Observação de Aves', 'Ecoturismo', 10, 3, 'Natureza Viva', 95, 85.0, 4.7, 'Passeio para observar aves em seu habitat', 'Aventura e Natureza', 15),
    (6, 'Yoga na Natureza', 'Lazer', 15, 5, 'Aventura X', 80, 60.0, 4.5, 'Aula de yoga ao ar livre, em meio à natureza', 'Lazer e Entretenimento', 12),
    (6, 'Acampamento de Verão', 'Ecoturismo', 25, 10, 'Aventura X', 150, 150.0, 4.8, 'Acampamento com atividades ao ar livre', 'Aventura e Natureza', 20),
    (7, 'Bike na Praia', 'Aventura', 20, 5, 'Turismo Seguro', 100, 70.0, 4.5, 'Passeio de bicicleta ao longo da orla', 'Aventura e Natureza', 15),
    (7, 'Caminhada nas Dunas', 'Ecoturismo', 12, 4, 'Turismo Seguro', 130, 90.0, 4.6, 'Caminhada pelas dunas com vistas espetaculares', 'Aventura e Natureza', 18),
    (8, 'Tour de Caverna', 'Aventura', 10, 3, 'Montanha e Mar', 70, 120.0, 4.8, 'Exploração de cavernas com guias experientes', 'Aventura e Natureza', 16),
    (8, 'Passeio Cultural em Grutas', 'Cultural', 15, 2, 'Montanha e Mar', 50, 45.0, 4.4, 'Visita a grutas com valor histórico', 'História e Cultura', 8),
    (9, 'Trilha do Mirante', 'Ecoturismo', 18, 5, 'Vida ao Ar Livre', 100, 80.0, 4.6, 'Trilha que leva a um mirante incrível', 'Aventura e Natureza', 14),
    (9, 'Oficina de Fotografia', 'Cultural', 10, 4, 'Vida ao Ar Livre', 70, 100.0, 4.5, 'Oficina de fotografia na natureza', 'História e Cultura', 10),
    (10, 'Aventura no Parque', 'Aventura', 15, 5, 'Paisagens Extremas', 90, 110.0, 4.7, 'Diversas atividades de aventura em um parque', 'Aventura e Natureza', 13),
    (10, 'Dia de Pesca', 'Lazer', 8, 3, 'Paisagens Extremas', 50, 60.0, 4.4, 'Dia de pesca em um lago tranquilo', 'Lazer e Entretenimento', 9)
])

# Inserir dados na tabela relatorios
cursor.executemany('''INSERT INTO relatorios (passeio_id, faturamento_mes, listagens_mes, clientes_mes, agendamentos_mes, crescimento) VALUES (?, ?, ?, ?, ?, ?)''', [
    (1, 2000.0, 150, 30, 10, 15.0),
    (2, 1350.0, 100, 25, 8, 12.0),
    (3, 2500.0, 200, 40, 15, 20.0),
    (4, 3000.0, 250, 50, 20, 30.0),
    (5, 1900.0, 120, 28, 12, 18.0),
    (6, 800.0, 90, 20, 10, 8.0),
    (7, 950.0, 110, 24, 11, 10.0),
    (8, 1000.0, 140, 32, 14, 17.0),
    (9, 780.0, 95, 18, 9, 6.0),
    (10, 670.0, 85, 16, 7, 5.0)
])

# Inserir dados na tabela passeios_agendados
cursor.executemany('''INSERT INTO passeios_agendados (cliente_id, passeio_id, data_agendamento) VALUES (?, ?, ?)''', [
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
cursor.executemany('''INSERT INTO avaliacoes (cliente_id, passeio_id, avaliacao_texto, avaliacao) VALUES (?, ?, ?, ?)''', [
    (1, 1, 'Experiência incrível!', 5.0),
    (2, 2, 'Gostei muito, recomendo.', 4.5),
    (3, 3, 'Passeio ótimo, porém poderia ter durado mais.', 4.0),
    (4, 4, 'Boa experiência, mas o preço é um pouco elevado.', 4.0),
    (5, 5, 'Natureza espetacular, mas guias pouco preparados.', 3.5),
    (6, 6, 'Um passeio relaxante e cheio de boas energias.', 4.7),
    (7, 7, 'Muito legal, faria de novo com certeza!', 4.8),
    (8, 8, 'Valeu cada centavo!', 4.9),
    (9, 9, 'Bom, mas achei o trajeto muito cansativo.', 3.8),
    (10, 10, 'Uma experiência mediana, esperava mais.', 3.0)
])

# Confirmar as alterações e fechar a conexão
conn.commit()
conn.close()

print("Dados inseridos com sucesso!")
