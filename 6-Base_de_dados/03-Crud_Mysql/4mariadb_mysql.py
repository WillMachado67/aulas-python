import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='clientes',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with conexao.cursor() as cursor:
    cursor.execute('SELECT * FROM clientes ORDER BY nome ASC LIMIT 100')
    # ASC = crescente | DESC = decrecente
    resultado = cursor.fetchall()

    for linha in resultado:
        print(linha)


conexao.close()
