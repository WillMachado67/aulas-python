from dados import produtos, pessoas, lista
from functools import reduce


soma_idade = reduce(lambda ac, p: p['Idade'] + ac, pessoas, 0)

print(soma_idade / len(pessoas))
