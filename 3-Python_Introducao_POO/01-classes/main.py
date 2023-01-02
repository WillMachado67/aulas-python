from pessoa import Pessoa

# p1 = estância
p1 = Pessoa('Willian', '29')
p2 = Pessoa('João', '31')

print(p1.nome)
print(p2.ano_atual)
print(p1.get_ano_nascimento())

print(p1.falar('POO'))
