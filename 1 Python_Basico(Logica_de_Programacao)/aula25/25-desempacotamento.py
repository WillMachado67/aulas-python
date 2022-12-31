"""
lista = ['Luis', 'João', 'Maria']

n1, n2, n3 = lista

print(n1, n2, outra_lista)
"""


lista = ['Luis', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, n3, *_, N4 = lista

print(n1, n2, _, N4)


'''
lista = ['Luis', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista

print(outra_lista, ultimo_da_lista)
'''