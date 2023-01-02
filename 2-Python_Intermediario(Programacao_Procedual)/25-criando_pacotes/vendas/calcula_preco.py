from vendas.formata import moeda


def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))
    if formata:
        return moeda.real(r)
    else:
        return r


def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * (porcentagem / 100))
    if formata:
        return moeda.real(r)
    else:
        return r
