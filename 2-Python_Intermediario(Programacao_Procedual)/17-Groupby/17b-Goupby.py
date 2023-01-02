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


for agrumento, valores_agrupados in alunos_agupados:
    print(f'agrupamentos: {agrumento}')

    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} alunos titaram a nota {agrumento}')
