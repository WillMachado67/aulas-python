from dados import produtos, pessoas, lista

nova_lista = map(lambda x: x * 2, lista)
# nova_lista = [x * 2 for x in lista]
print(lista)
print(list(nova_lista))
