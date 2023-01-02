


variavel = ['Willian', 'João', 'Maria']


for valor in variavel:

    if valor.lower().startswith('j'):
        break
        #pass
        #continue
    print(valor)
else:
    print('Não existe uma palavra que começa com J.')
