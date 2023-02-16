import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DIR_BD = ROOT_DIR / 'basededados.db'

conexao = sqlite3.connect(DIR_BD)
cursor = conexao.cursor()


cursor.execute('SELECT nome, peso FROM clientes WHERE peso < :peso', {'peso': 50})
for linha in cursor.fetchall():  # Busca e entrega todos os valores que estão na tabela
    nome, peso = linha
    print(nome, peso)

cursor.close()
conexao.close()
