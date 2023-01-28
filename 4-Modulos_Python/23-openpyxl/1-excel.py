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
# print(nome_planilhas)

planilha1 = pedidos['Página1']

print(planilha1['b4'])
print(planilha1['b4'].value)
print(planilha1['b'])

# for campo in planilha1['c']:
#     print(campo.value)


# for linha in planilha1['a1:c2']:
#     for coluna in linha:
#         print(coluna.value)

# for linha in planilha1:
#     for coluna in linha:
#         print(coluna.value)
