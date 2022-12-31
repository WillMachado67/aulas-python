from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 3, lista)
# nova_lista = [x for x in lista if x > 5]

print(list(nova_lista))
