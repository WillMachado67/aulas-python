"""
public - métodos e atributos que podem ser acessados dentro e fora da classe
protected - atributos que podem ser acessados apenas dentro da classe, ou das filhas da classe
private - atributo ou metodo só está disponivel apenas dentro classe
"""


class BaseDeDados:
    def __init__(self):  # construtor
        self.dados = {}  # publico

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

bd.apaga_cliente(2)

bd.lista_clientes()

print(bd.dados)