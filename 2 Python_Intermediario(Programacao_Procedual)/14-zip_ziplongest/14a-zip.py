"""
zip - Unindo iteráveis
zip_longest - Itertools
"""

### Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

### Código

estados = ['SP', 'MG', 'BA']

cidades_estados = zip(estados, cidades)

for valor in cidades_estados:
    print(valor)

# print(cidades_estados)
# print(list(cidades_estados))
print(dict(cidades_estados))
