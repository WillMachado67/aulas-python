import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DIR_BD = ROOT_DIR / 'basededados.db'

conexao = sqlite3.connect(DIR_BD)
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('  # Cria tabela se ela não existir
               # Coluna id de numero inteiro, chave primaria, auto incrementada
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Willian", 73.3)')
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Suelen', 62.1))
cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {'nome': 'Joãozinho', 'peso': 43.2}
)
cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': 'Daniel', 'peso': 113}
)
conexao.commit()

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():  # Busca e entrega todos os valores que estão na tabela
    id_, nome, peso = linha
    print(id_, nome, peso)

cursor.close()
conexao.close()
