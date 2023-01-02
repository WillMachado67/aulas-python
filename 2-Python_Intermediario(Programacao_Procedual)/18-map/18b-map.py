from dados import produtos, pessoas, lista


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


# for produto in produtos:
#     print(produto)

################################

# precos = map(lambda p: p['preco'], produtos)
#
# for preco in precos:
#     print(preco)

#####################################

novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)
