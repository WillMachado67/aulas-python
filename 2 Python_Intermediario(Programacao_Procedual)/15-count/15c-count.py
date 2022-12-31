"""
count - Itertoools
"""
from itertools import count

contador = count()
lista = ['Willian', 'Suelen', 'Rafael']
lista = zip(contador, lista)

print(list(lista))