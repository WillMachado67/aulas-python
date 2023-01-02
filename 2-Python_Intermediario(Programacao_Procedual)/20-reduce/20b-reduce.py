from dados import produtos, pessoas, lista
from functools import reduce


soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)

print(soma_preco)
