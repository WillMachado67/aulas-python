d1 = {
    'str': 'String',
    123: 'número',
    (1, 2, 3, 4): 'Tupla',
}

print(d1[(1, 2, 3, 4)])

######################################

# d1['nao existe'] = 'agora existe'

# if 'nao existe' in d1:
#     print(d1['nao existe'])
# else:
#     print('Não existe.')

#######################################

# d1['nomedachave'] = 'agora existe'

# if d1.get('nomedachave') is not None:
#     print(d1.get('nomedachave'))
# else:
#     print('Não existe.')

######################################

# d1['str'] = 'agora existe'
# d1.update({'nova_chave': 'novo_valor'})
#
# print(d1)
