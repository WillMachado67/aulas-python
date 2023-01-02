lista = [
    ('chave', 'valor'),
    ('chave2', 'Valor2')
]

d1 = {x: y for x, y in lista}

print(d1)

#################################

# d1 = {x: y for x, y in enumerate(range(5))}
#
# print(d1)

##################################

d1 = {f'chave_{x}': x*2 for x in range(5)}

print(d1)
