class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_de_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa.por_ano_de_nascimento('Willian', 1993)
# p1 = Pessoa('willian', 29)
# print(p1)
print(p1.nome, p1.idade)
# p1.get_ano_nascimento()
