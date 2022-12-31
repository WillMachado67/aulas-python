"""
* Criar variaveis para nome(str), idade(int),
* altura(foat) e peso(float) de uma pessoa
* criar variavel com ano atual(int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valore na tela usando F-Strings (com as chaves)
"""
nome = 'Willian'
idade = 29
altura = 1.83
peso = 72.5
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / altura**2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
