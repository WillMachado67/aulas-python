"""
Interando strings com for
Função range(start=0, stop, step=1)
"""

texto = 'Python'
nova_string = ''
'''
for letra in texto:
    print(letra)
'''
'''
for letra in texto:
    nova_string += letra

    print(nova_string)
'''
'''
for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)
'''

for numero in range(100):
    print(numero)
