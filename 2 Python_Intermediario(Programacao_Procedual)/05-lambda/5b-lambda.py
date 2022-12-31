# lista = [
#     ['P1', '13'],
#     ['P2', '06'],
#     ['P3', '07'],
#     ['P4', '50'],
#     ['P5', '08'],
# ]
# lista.sort()
# print(lista)

########################################

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]


# def func(item):
#     return item[1]
#
#
# lista.sort(key=func)
# lista.sort(key=func, reverse=True)
# print(lista)

##########################################################

lista.sort(key=lambda item: item[1], reverse=True)

print(lista)
##########################################################

# print(sorted(lista))
# print(sorted(lista, key=lambda i: i[1]))
#########################################################
