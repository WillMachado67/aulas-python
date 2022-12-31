"""

* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerate elementos da listas # iteráveis
"""
'''
string = 'O Brasil é penta.'
lista_1 = string.split(' ')

for indice, valor in enumerate(lista_1):
    print(indice, valor, lista_1[indice])
'''
'''
lista = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria'],
]

for indice, valor in lista:
    print(indice, valor)
'''

lista = ['Luiz', 'João', 'Maria']
for indice, valor in enumerate(lista):
    print(indice, valor)
