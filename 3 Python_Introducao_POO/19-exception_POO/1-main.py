# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# Levantando e tratando suas Exceptions (Exceções)
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MeuError(Exception):
    ...

class OutroError(Exception):
    ...


def levantar():
    # raise MeuError('Mensagem error')
    exception_ = MeuError('a', 'b', 'c')
    raise exception_


# levantar()

try:
    5/0
    levantar()

except (MeuError, ZeroDivisionError) as error:
    print(error)
    print(error.__class__.__name__)
    print()
    raise
