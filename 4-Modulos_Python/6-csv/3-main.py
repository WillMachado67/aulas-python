# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'dados2.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Idade': 31, 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Idade': 20, 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Idade': 25, 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    colunas = lista_clientes[0].keys()
    escritor = csv.writer(arquivo)

    escritor.writerow(colunas)

    for cliente in lista_clientes:
        escritor.writerow(cliente.values())
