from dados import produtos, pessoas, lista

# for pessoa in pessoas:
#     print(pessoa)

#############################

idades_pessoas = map(lambda p: p['Idade'], pessoas)

lista_idade = []

for idade in idades_pessoas:
    lista_idade.append(idade)

print(lista_idade)
############################

