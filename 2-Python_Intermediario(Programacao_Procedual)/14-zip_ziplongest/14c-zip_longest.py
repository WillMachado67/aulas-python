"""
zip - Unindo iteráveis
zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Ibiúna']
estados = ['SP', 'MG', 'BA',]

cidades_estados = zip(indice, estados, cidades)

for indice, estado, cidade in cidades_estados:
    print(indice, cidade, estado)
