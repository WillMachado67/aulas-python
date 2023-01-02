from dados import produtos, pessoas, lista
from functools import reduce

lista = [2, 2]

acumula = 1
for item in lista:
    acumula /= item

print(acumula)

########################

soma_lista = reduce(lambda ac, i: i / ac, lista, 1)

print(soma_lista)
