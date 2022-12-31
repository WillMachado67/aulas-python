"""

* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerate elementos da listas # iteráveis
"""
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
# print(lista_2)


for valor in lista_1:
    #print(valor)
    #print(valor.strip().capitalize())
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')


# palavra = ''
# contagem = 0
# for valor in lista_1:
#
#     qtd_vezes = lista_1.count(valor)
#     print(valor, qtd_vezes)
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A pavra que apareceu mais vezes é "{palavra}" ({contagem}x).')
