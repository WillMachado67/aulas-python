from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
# print(escritor.nome)
print(caneta.marca)
caneta.escrever()

