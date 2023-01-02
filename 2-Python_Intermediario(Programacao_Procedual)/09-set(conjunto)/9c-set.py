# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

s1 = {1, 2, 3, 4, 5, 8, 7}
s2 = {1, 2, 3, 4, 5, 6}


# s3 = s1 | s2             # union
# s3 = s1.union(s2)        # union

# s3 = s1 & s2             # intersection

s3 = s2 - s1             # difference
# s3 = s1 ^ s2             # difference

print(s3)
