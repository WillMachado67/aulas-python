"""
https://openpyxl.readthedocs.io/en/stable/
pip install openpyxl
pipenv install openpyxl
"""
import openpyxl
from pathlib import Path

CAMINHO_PEDIDOS = Path(__file__).parent / 'pedidos.xlsx'

pedidos = openpyxl.load_workbook(filename=CAMINHO_PEDIDOS)
nome_planilhas = pedidos.sheetnames

planilha1 = pedidos['Página1']

for linha in planilha1:
    print(linha[0].value, linha[1].value, linha[2].value, linha[3].value, )

# for linha in planilha1:
#     cont = 0
#     if linha[cont].value is not None:
#         print(linha[cont].value, linha[cont + 1].value,
#               linha[cont + 2].value, sep=' | ')
#         cont += 1

