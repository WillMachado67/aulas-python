# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

s1 = {1, 2, 3, 4, 5, 6}

# for v in s1:
#     print(v)

################################

# # s1 = {}
# s1 = set()
# s1.add(1)
# s1.add(2)
#
# print(s1)

################################

s1.discard(2)

print(s1)

###############################

# s1 = set()
# # s1.update('Python')
# s1.update([1, 2, 3, 4, 5], {5, 6, 7, 2, 8, 9})
#
# print(s1)
