"""
public - métodos e atributos que podem ser acessados dentro e fora da classe
protected - atributos que podem ser acessados apenas dentro da classe, ou das filhas da classe
private - atributo ou metodo só está disponivel apenas dentro classe
_ privado/protected
__ privado (_NOMECLASSE__nomeatributo)
"""


class BaseDeDados:
    def __init__(self):  # construtor
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

bd.__dados = "oi"

bd.apaga_cliente(2)

print(bd.dados)
# print(bd._BaseDeDados__dados)
