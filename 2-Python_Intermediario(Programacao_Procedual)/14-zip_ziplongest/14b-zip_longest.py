"""
zip - Unindo iteráveis
zip_longest - Itertools
"""
from itertools import zip_longest

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Ibiúna']
estados = ['SP', 'MG', 'BA',]

cidades_estados = zip_longest(estados, cidades, fillvalue='?')
print(list(cidades_estados))
