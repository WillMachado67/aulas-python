from itertools import groupby


alunos = [
    {'Nome': 'Luiz', 'Nota': 'A'},
    {'Nome': 'Leticia', 'Nota': 'B'},
    {'Nome': 'Fabricio', 'Nota': 'A'},
    {'Nome': 'Rosemary', 'Nota': 'C'},
    {'Nome': 'Joana', 'Nota': 'D'},
    {'Nome': 'João', 'Nota': 'A'},
    {'Nome': 'Eduardo', 'Nota': 'B'},
    {'Nome': 'Andre', 'Nota': 'A'},
    {'Nome': 'Anderson', 'Nota': 'C'},
    {'Nome': 'José', 'Nota': 'B'},
]
ordena = lambda item: item['Nota']
alunos.sort(key=ordena)
alunos_agupados = groupby(alunos, ordena)


# for aluno in alunos:
#     print(aluno)
####################################

# for grupo in alunos_agupados:
#     print(grupo)

###################################
for agrumento, valores_agrupados in alunos_agupados:
    print(f'agrupamentos: {agrumento}')
    for aluno in valores_agrupados:
        print(aluno)
    print()
