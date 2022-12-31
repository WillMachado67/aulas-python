"""
Combinations, permutatioins e Product - Itertools
Combinação - Ordem não importa
Permutation - Ordem importa
Ambos nao repetem valores único
Produto - Ordem importa e repete valores únicos
"""
from itertools import product
pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']
for index, grupo in enumerate(product(pessoas, repeat=4)):
    print(index, grupo)
