import json
import os
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'endereços': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'save.json')

# with open(JSON_FILE, 'w') as arquivo:
    # json.dump(pessoa, arquivo)
    # json.dump(pessoa, arquivo, ensure_ascii=False)
    # json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

with open(JSON_FILE, 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)

# os.remove(JSON_FILE)