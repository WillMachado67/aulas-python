"""
https://openpyxl.readthedocs.io/en/stable/
pip install openpyxl
pipenv install openpyxl
"""
import openpyxl
from pathlib import Path

ROOT = Path(__file__).parent
CAMINHO_PEDIDOS = ROOT / 'pedidos.xlsx'
NOVA_PLANILHAS = ROOT / 'novos_pedidos.xlsx'

pedidos = openpyxl.load_workbook(filename=CAMINHO_PEDIDOS)
nome_planilhas = pedidos.sheetnames
planilha1 = pedidos['Página1']

planilha1['B3'].value = 2200

pedidos.save(NOVA_PLANILHAS)
