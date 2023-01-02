lista = [0, 1, 2, 3, 4, 5]
lista = iter(lista)

print('Iteravel = ', hasattr(lista, '__iter__'))  # saber se um valor tem tal metodo
print('Iterador = ', hasattr(lista, '__next__'))

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
