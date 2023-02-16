import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DIR_BD = ROOT_DIR / 'basededados.db'

conexao = sqlite3.connect(DIR_BD)
cursor = conexao.cursor()

# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {'nome': 'Rafael', 'id': 3}
# )
cursor.execute(
    'DELETE FROM clientes WHERE id=:id',
    {'id': 4}
)
conexao.commit()

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():  # Busca e entrega todos os valores que estão na tabela
    id_, nome, peso = linha
    print(id_, nome, peso)

cursor.close()
conexao.close()
