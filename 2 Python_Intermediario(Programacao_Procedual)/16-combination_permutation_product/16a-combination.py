"""
Combinations, permutatioins e Product - Itertools
Combinação - Ordem não importa
Permutation - Ordem importa
Ambos nao repetem valores único
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations
pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']
for index, grupo in enumerate(combinations(pessoas, 2)):
    print(index, grupo)
