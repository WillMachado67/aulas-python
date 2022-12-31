from dados import produtos, pessoas, lista

nova_lista = filter(lambda p: p['Idade'] <= 18, pessoas)

for produto in nova_lista:
    print(produto)
