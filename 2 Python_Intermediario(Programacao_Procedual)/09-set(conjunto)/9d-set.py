# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

l1 = ['Willia', 'Rafael', 'Suelen']
l2 = ['Willia', 'Willia', 'Willia', 'Willia', 'Willia', 'Suelen', 'Suelen', 'Suelen', 'Rafael', 'Suelen']

l1 = set(l1)  # cast
l2 = set(l2)  # cast

print(l1, l2)
