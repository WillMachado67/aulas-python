from random import randint


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):  # parâmetro de instância
        print(self.ano_atual - self.idade)

    @classmethod  # não é refente a instância em si, mas é referente a classe em si
    def por_ano_de_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod  # ultiliza classe ou intância para chama-lo, não pode ultizar classe ou intância dentro do corpo
    def gera_id():
        rand = randint(10000, 19999)
        return rand


# p1 = Pessoa.por_ano_de_nascimento('Willian', 1993)
p1 = Pessoa('willian', 29)
print(p1)
# print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())

