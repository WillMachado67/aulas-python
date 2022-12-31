import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 4: ['Willian', 'Machado']}

# v = d1.copy()
#
# v[1] = 'Will'
# v[4][0] = 'Luiz'
#
# print(d1)
# print(v)

#############################################

v = copy.deepcopy(d1)

v[1] = 'Will'
v[4][0] = 'Luiz'

print(d1)
print(v)
