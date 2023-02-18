import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso)' \
            ' VALUES (%s, %s, %s, %s)'
        dados = [
            ('Jack', 'Castanho', 19, 55),
            ('Jakeline', 'Figueiredo', 23, 62.1),
            ('Pamela', 'dias', 51, 98.56),
        ]

        cursor.executemany(sql, dados)
        conexao.commit()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
